"""Tests for GnuCash importer."""
import os
import sqlite3
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.database.schema import ensure_schema
from app.services.gnucash_import_service import import_gnucash_sqlite


GNUCASH_DDL = """
CREATE TABLE commodities(guid text(32) PRIMARY KEY NOT NULL, namespace text(2048) NOT NULL, mnemonic text(2048) NOT NULL, fullname text(2048), cusip text(2048), fraction integer NOT NULL, quote_flag integer NOT NULL, quote_source text(2048), quote_tz text(2048));
CREATE TABLE accounts(guid text(32) PRIMARY KEY NOT NULL, name text(2048) NOT NULL, account_type text(2048) NOT NULL, commodity_guid text(32), commodity_scu integer NOT NULL, non_std_scu integer NOT NULL, parent_guid text(32), code text(2048), description text(2048), hidden integer, placeholder integer);
CREATE TABLE prices(guid text(32) PRIMARY KEY NOT NULL, commodity_guid text(32) NOT NULL, currency_guid text(32) NOT NULL, date text(19) NOT NULL, source text(2048), type text(2048), value_num bigint NOT NULL, value_denom bigint NOT NULL);
CREATE TABLE transactions(guid text(32) PRIMARY KEY NOT NULL, currency_guid text(32) NOT NULL, num text(2048) NOT NULL, post_date text(19), enter_date text(19), description text(2048));
CREATE TABLE splits(guid text(32) PRIMARY KEY NOT NULL, tx_guid text(32) NOT NULL, account_guid text(32) NOT NULL, memo text(2048) NOT NULL, action text(2048) NOT NULL, reconcile_state text(1) NOT NULL, reconcile_date text(19), value_num bigint NOT NULL, value_denom bigint NOT NULL, quantity_num bigint NOT NULL, quantity_denom bigint NOT NULL, lot_guid text(32));
"""


def _create_gnucash_db(path: str) -> None:
    conn = sqlite3.connect(path)
    conn.executescript(GNUCASH_DDL)

    conn.execute(
        "INSERT INTO commodities(guid, namespace, mnemonic, fullname, fraction, quote_flag) VALUES (?, ?, ?, ?, ?, ?)",
        ("c_usd", "CURRENCY", "USD", "US Dollar", 100, 1),
    )
    conn.execute(
        "INSERT INTO commodities(guid, namespace, mnemonic, fullname, fraction, quote_flag) VALUES (?, ?, ?, ?, ?, ?)",
        ("c_eur", "CURRENCY", "EUR", "Euro", 100, 1),
    )

    conn.execute(
        """
        INSERT INTO accounts(guid, name, account_type, commodity_guid, commodity_scu, non_std_scu, parent_guid, code, description, hidden, placeholder)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        ("a_assets", "Assets", "ASSET", "c_usd", 100, 0, None, "1000", "Assets root", 0, 0),
    )
    conn.execute(
        """
        INSERT INTO accounts(guid, name, account_type, commodity_guid, commodity_scu, non_std_scu, parent_guid, code, description, hidden, placeholder)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        ("a_cash", "Cash", "ASSET", "c_usd", 100, 0, "a_assets", "1010", "Cash account", 0, 0),
    )
    conn.execute(
        """
        INSERT INTO accounts(guid, name, account_type, commodity_guid, commodity_scu, non_std_scu, parent_guid, code, description, hidden, placeholder)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        ("a_exp", "Expenses", "EXPENSE", "c_eur", 100, 0, None, "5000", "Expense account", 1, 0),
    )

    conn.execute(
        "INSERT INTO transactions(guid, currency_guid, num, post_date, enter_date, description) VALUES (?, ?, ?, ?, ?, ?)",
        ("t_1", "c_usd", "1", "2025-01-02 03:04:05", "2025-01-02 03:04:06", "Coffee"),
    )

    conn.execute(
        """
        INSERT INTO splits(guid, tx_guid, account_guid, memo, action, reconcile_state, value_num, value_denom, quantity_num, quantity_denom)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        ("s_1", "t_1", "a_cash", "Debit", "", "n", 1000, 100, 1200, 100),
    )
    conn.execute(
        """
        INSERT INTO splits(guid, tx_guid, account_guid, memo, action, reconcile_state, value_num, value_denom, quantity_num, quantity_denom)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        ("s_2", "t_1", "a_exp", "Credit", "", "n", -1000, 100, -1200, 100),
    )

    conn.execute(
        """
        INSERT INTO prices(guid, commodity_guid, currency_guid, date, source, type, value_num, value_denom)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        ("p_1", "c_eur", "c_usd", "2025-01-01 00:00:00", "manual", "last", 110, 100),
    )

    conn.commit()
    conn.close()


def _create_gnucash_db_parent_after_child(path: str) -> None:
    conn = sqlite3.connect(path)
    conn.executescript(GNUCASH_DDL)

    conn.execute(
        "INSERT INTO commodities(guid, namespace, mnemonic, fullname, fraction, quote_flag) VALUES (?, ?, ?, ?, ?, ?)",
        ("c_usd", "CURRENCY", "USD", "US Dollar", 100, 1),
    )

    conn.execute(
        """
        INSERT INTO accounts(guid, name, account_type, commodity_guid, commodity_scu, non_std_scu, parent_guid, code, description, hidden, placeholder)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        ("a_child", "Child", "ASSET", "c_usd", 100, 0, "z_parent", "1010", "Child account", 0, 0),
    )
    conn.execute(
        """
        INSERT INTO accounts(guid, name, account_type, commodity_guid, commodity_scu, non_std_scu, parent_guid, code, description, hidden, placeholder)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        ("z_parent", "Parent", "ASSET", "c_usd", 100, 0, None, "1000", "Parent account", 0, 0),
    )

    conn.commit()
    conn.close()


def test_import_gnucash_sqlite_maps_ids_and_amounts(tmp_path):
    source_path = tmp_path / "source_gnucash.db"
    _create_gnucash_db(str(source_path))

    target = sqlite3.connect(":memory:")
    target.row_factory = sqlite3.Row
    target.execute("PRAGMA foreign_keys = ON;")
    ensure_schema(target)

    import_gnucash_sqlite(str(source_path), target)

    currencies = target.execute("SELECT ID, Code FROM Currency ORDER BY ID").fetchall()
    assert [r["ID"] for r in currencies] == [1, 2]

    cash = target.execute("SELECT ID FROM Account WHERE Name = 'Cash'").fetchone()
    expense = target.execute("SELECT ID, IsHidden FROM Account WHERE Name = 'Expenses'").fetchone()
    assert cash is not None
    assert expense is not None
    assert expense["IsHidden"] == 1

    split_cash = target.execute(
        "SELECT Amount, Currency FROM Split WHERE Description = 'Debit'"
    ).fetchone()
    split_exp = target.execute(
        "SELECT Amount, Currency FROM Split WHERE Description = 'Credit'"
    ).fetchone()

    assert split_cash is not None
    assert split_exp is not None
    assert split_cash["Amount"] == 1200
    assert split_exp["Amount"] == -1200

    # Currency for split is resolved via split.account_guid -> accounts.commodity_guid
    usd_currency_id = target.execute("SELECT ID FROM Currency WHERE Code = 'USD'").fetchone()["ID"]
    eur_currency_id = target.execute("SELECT ID FROM Currency WHERE Code = 'EUR'").fetchone()["ID"]
    assert split_cash["Currency"] == usd_currency_id
    assert split_exp["Currency"] == eur_currency_id

    price = target.execute("SELECT Value FROM Price").fetchone()
    assert price is not None
    assert price["Value"] == pytest.approx(1.1)


def test_import_gnucash_sqlite_keeps_existing_data(tmp_path):
    source_path = tmp_path / "source_gnucash.db"
    _create_gnucash_db(str(source_path))

    target = sqlite3.connect(":memory:")
    target.row_factory = sqlite3.Row
    target.execute("PRAGMA foreign_keys = ON;")
    ensure_schema(target)

    target.execute("INSERT INTO Currency (Code, Type, Name, Denominator) VALUES ('OLD', 'CURR', 'Old', 100)")
    target.execute("INSERT INTO Account (Parent, Name, Code, Description, ExternalID, IsHidden) VALUES (NULL, 'OldAcc', NULL, NULL, NULL, 0)")
    target.execute("INSERT INTO Trans (Date, Description) VALUES ('2024-01-01 00:00:00', 'OldTrans')")
    target.commit()

    import_gnucash_sqlite(str(source_path), target)

    assert target.execute("SELECT COUNT(*) FROM Currency").fetchone()[0] == 3
    assert target.execute("SELECT COUNT(*) FROM Account").fetchone()[0] == 4
    assert target.execute("SELECT COUNT(*) FROM Trans").fetchone()[0] == 2


def test_import_gnucash_sqlite_raises_on_unresolved_split_links(tmp_path):
    source_path = tmp_path / "source_gnucash_broken.db"
    _create_gnucash_db(str(source_path))

    src = sqlite3.connect(source_path)
    src.execute("DELETE FROM commodities WHERE guid = 'c_eur'")
    src.commit()
    src.close()

    target = sqlite3.connect(":memory:")
    target.row_factory = sqlite3.Row
    target.execute("PRAGMA foreign_keys = ON;")
    ensure_schema(target)

    with pytest.raises(ValueError, match="Unresolved split links found during import"):
        import_gnucash_sqlite(str(source_path), target)


def test_import_gnucash_sqlite_handles_parent_inserted_after_child(tmp_path):
    source_path = tmp_path / "source_gnucash_parent_order.db"
    _create_gnucash_db_parent_after_child(str(source_path))

    target = sqlite3.connect(":memory:")
    target.row_factory = sqlite3.Row
    target.execute("PRAGMA foreign_keys = ON;")
    ensure_schema(target)

    import_gnucash_sqlite(str(source_path), target)

    child = target.execute("SELECT ID, Parent FROM Account WHERE Name = 'Child'").fetchone()
    parent = target.execute("SELECT ID FROM Account WHERE Name = 'Parent'").fetchone()
    assert child is not None
    assert parent is not None
    assert child["Parent"] == parent["ID"]
