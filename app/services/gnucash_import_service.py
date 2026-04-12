"""Import data from GnuCash SQLite database into ChaosCash schema."""
from __future__ import annotations

import sqlite3


def import_gnucash_sqlite(source_db_path: str, target_conn: sqlite3.Connection) -> None:
    """Import a GnuCash SQLite file into current ChaosCash database.

    All GUID keys from GnuCash are converted to sequential integer IDs.
    Existing target data is preserved.
    """
    source_conn = sqlite3.connect(source_db_path)
    source_conn.row_factory = sqlite3.Row
    source_conn.execute("PRAGMA foreign_keys = ON;")

    try:
        _validate_gnucash_schema(source_conn)

        with target_conn:
            currency_map = _import_currencies(source_conn, target_conn)

        target_conn.commit()
        target_conn.execute("PRAGMA foreign_keys = OFF;")
        with target_conn:
            account_map = _import_accounts(source_conn, target_conn)
        target_conn.commit()
        target_conn.execute("PRAGMA foreign_keys = ON;")

        with target_conn:
            transaction_map = _import_transactions(source_conn, target_conn)
            _import_splits(source_conn, target_conn, account_map, currency_map, transaction_map)
            _import_prices(source_conn, target_conn, currency_map)
    finally:
        target_conn.execute("PRAGMA foreign_keys = ON;")
        source_conn.close()


def _validate_gnucash_schema(conn: sqlite3.Connection) -> None:
    required_tables = {
        "commodities",
        "accounts",
        "prices",
        "transactions",
        "splits",
    }
    rows = conn.execute("SELECT name FROM sqlite_master WHERE type='table';")
    actual = {r[0] for r in rows}
    missing = required_tables - actual
    if missing:
        raise ValueError(f"Invalid GnuCash database. Missing tables: {', '.join(sorted(missing))}")


def _next_id(conn: sqlite3.Connection, table: str) -> int:
    row = conn.execute(f"SELECT COALESCE(MAX(ID), 0) + 1 FROM {table}").fetchone()
    return int(row[0])


def _import_currencies(source: sqlite3.Connection, target: sqlite3.Connection) -> dict[str, int]:
    rows = source.execute(
        """
        SELECT guid, namespace, mnemonic, fullname, fraction
        FROM commodities
        ORDER BY guid
        """
    )
    guid_to_id: dict[str, int] = {}
    next_id = _next_id(target, "Currency")
    for row in rows:
        guid_to_id[row["guid"]] = next_id
        target.execute(
            "INSERT INTO Currency (ID, Code, Type, Name, Denominator) VALUES (?, ?, ?, ?, ?)",
            (next_id, row["mnemonic"], row["namespace"], row["fullname"], row["fraction"]),
        )
        next_id += 1
    return guid_to_id


def _import_accounts(source: sqlite3.Connection, target: sqlite3.Connection) -> dict[str, int]:
    rows = source.execute(
        """
        SELECT guid, parent_guid, name, code, description, hidden
        FROM accounts
        ORDER BY guid
        """
    )

    raw_rows: list[sqlite3.Row] = []
    guid_to_id: dict[str, int] = {}
    next_id = _next_id(target, "Account")

    for row in rows:
        raw_rows.append(row)
        guid_to_id[row["guid"]] = next_id
        next_id += 1

    for row in raw_rows:
        parent_guid = row["parent_guid"]
        parent_id = guid_to_id.get(parent_guid) if parent_guid else None
        target.execute(
            """
            INSERT INTO Account (ID, Parent, Name, Code, Description, IsHidden)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                guid_to_id[row["guid"]],
                parent_id,
                row["name"],
                row["code"],
                row["description"],
                row["hidden"],
            ),
        )
    return guid_to_id


def _import_transactions(source: sqlite3.Connection, target: sqlite3.Connection) -> dict[str, int]:
    rows = source.execute(
        """
        SELECT guid, post_date, description
        FROM transactions
        ORDER BY post_date, guid
        """
    )

    guid_to_id: dict[str, int] = {}
    next_id = _next_id(target, "Trans")
    for row in rows:
        guid_to_id[row["guid"]] = next_id
        target.execute(
            "INSERT INTO Trans (ID, Date, Description) VALUES (?, ?, ?)",
            (next_id, row["post_date"] or "1970-01-01 00:00:00", row["description"]),
        )
        next_id += 1
    return guid_to_id


def _import_splits(
    source: sqlite3.Connection,
    target: sqlite3.Connection,
    account_map: dict[str, int],
    currency_map: dict[str, int],
    transaction_map: dict[str, int],
) -> None:
    rows = source.execute(
        """
        SELECT
            s.guid,
            s.tx_guid,
            s.account_guid,
            s.memo,
            s.quantity_num,
            a.commodity_guid AS currency_guid
        FROM splits s
        JOIN accounts a ON a.guid = s.account_guid
        ORDER BY s.guid
        """
    )

    next_id = _next_id(target, "Split")
    unresolved: list[str] = []
    for row in rows:
        trans_id = transaction_map.get(row["tx_guid"])
        account_id = account_map.get(row["account_guid"])
        currency_id = currency_map.get(row["currency_guid"])

        if trans_id is None or account_id is None or currency_id is None:
            unresolved.append(
                f"split_guid={row['guid']}, tx_guid={row['tx_guid']}, "
                f"account_guid={row['account_guid']}, currency_guid={row['currency_guid']}"
            )
            continue

        target.execute(
            """
            INSERT INTO Split (ID, Trans, Account, Currency, Description, Amount, AmountFixed)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                next_id,
                trans_id,
                account_id,
                currency_id,
                row["memo"],
                row["quantity_num"],
                0,
            ),
        )
        next_id += 1

    if unresolved:
        details = "\n".join(unresolved)
        raise ValueError(f"Unresolved split links found during import:\n{details}")


def _import_prices(source: sqlite3.Connection, target: sqlite3.Connection, currency_map: dict[str, int]) -> None:
    rows = source.execute(
        """
        SELECT commodity_guid, currency_guid, date, source, value_num, value_denom
        FROM prices
        ORDER BY date
        """
    )

    next_id = _next_id(target, "Price")
    unresolved: list[str] = []
    for row in rows:
        of_curr = currency_map.get(row["commodity_guid"])
        in_curr = currency_map.get(row["currency_guid"])
        if of_curr is None or in_curr is None:
            unresolved.append(
                f"price commodity_guid={row['commodity_guid']}, currency_guid={row['currency_guid']}, date={row['date']}"
            )
            continue

        value = row["value_num"] / row["value_denom"]
        target.execute(
            "INSERT INTO Price (ID, OfCurr, Value, InCurr, Date, Source) VALUES (?, ?, ?, ?, ?, ?)",
            (next_id, of_curr, value, in_curr, row["date"], row["source"]),
        )
        next_id += 1

    if unresolved:
        details = "\n".join(unresolved)
        raise ValueError(f"Unresolved price currency links found during import:\n{details}")
