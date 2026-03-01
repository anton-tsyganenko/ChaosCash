import sqlite3

from app.database.queries import transactions as Q
from app.models.transaction import Transaction


def _row_to_trans(row) -> Transaction:
    return Transaction(
        id=row["ID"],
        date=row["Date"],
        description=row["Description"],
    )


class TransactionRepo:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def _fetch_dicts_with_ids(self, query_template: str, ids: list[int]) -> list[dict]:
        if not ids:
            return []
        placeholders = ",".join("?" * len(ids))
        sql = query_template.format(placeholders=placeholders)
        rows = self.conn.execute(sql, ids).fetchall()
        return [dict(r) for r in rows]

    def get_by_id(self, trans_id: int) -> Transaction | None:
        row = self.conn.execute(Q.GET_BY_ID, (trans_id,)).fetchone()
        return _row_to_trans(row) if row else None

    def insert(self, date: str, description: str | None) -> int:
        cur = self.conn.execute(Q.INSERT, (date, description))
        self.conn.commit()
        return cur.lastrowid

    def update(self, trans_id: int, date: str, description: str | None) -> None:
        self.conn.execute(Q.UPDATE, (date, description, trans_id))
        self.conn.commit()

    def delete(self, trans_id: int) -> None:
        self.conn.execute(Q.DELETE, (trans_id,))
        self.conn.commit()

    def get_verbose_by_accounts(self, account_ids: list[int]) -> list[dict]:
        return self._fetch_dicts_with_ids(Q.GET_VERBOSE_BY_ACCOUNTS, account_ids)

    def get_summary_by_accounts(self, account_ids: list[int]) -> list[dict]:
        return self._fetch_dicts_with_ids(Q.GET_SUMMARY_BY_ACCOUNTS, account_ids)

    def get_summary_by_ids(self, trans_ids: list[int]) -> list[dict]:
        return self._fetch_dicts_with_ids(Q.GET_SUMMARY_BY_IDS, trans_ids)

    def get_imbalanced(self) -> list[dict]:
        rows = self.conn.execute(Q.GET_IMBALANCED).fetchall()
        return [dict(r) for r in rows]

    def get_empty(self) -> list[Transaction]:
        rows = self.conn.execute(Q.GET_EMPTY).fetchall()
        return [_row_to_trans(r) for r in rows]

    def get_total_imbalance(self) -> dict[int, int]:
        """Return total imbalance per currency as dict {currency_id: imbalance_amount}."""
        rows = self.conn.execute(Q.GET_TOTAL_IMBALANCE).fetchall()
        return {row["Currency"]: row["Imbalance"] for row in rows}
