import sqlite3
from app.models.transaction import Transaction
from app.database.queries import transactions as Q


def _row_to_trans(row) -> Transaction:
    return Transaction(
        id=row["ID"],
        date=row["Date"],
        description=row["Description"],
    )


class TransactionRepo:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

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
        if not account_ids:
            return []
        placeholders = ",".join("?" * len(account_ids))
        sql = Q.GET_VERBOSE_BY_ACCOUNTS.format(placeholders=placeholders)
        rows = self.conn.execute(sql, account_ids).fetchall()
        return [dict(r) for r in rows]

    def get_summary_by_accounts(self, account_ids: list[int]) -> list[dict]:
        if not account_ids:
            return []
        placeholders = ",".join("?" * len(account_ids))
        sql = Q.GET_SUMMARY_BY_ACCOUNTS.format(placeholders=placeholders)
        rows = self.conn.execute(sql, account_ids).fetchall()
        return [dict(r) for r in rows]

    def get_verbose_by_ids(self, trans_ids: list[int]) -> list[dict]:
        if not trans_ids:
            return []
        placeholders = ",".join("?" * len(trans_ids))
        sql = Q.GET_VERBOSE_BY_IDS.format(placeholders=placeholders)
        rows = self.conn.execute(sql, trans_ids).fetchall()
        return [dict(r) for r in rows]

    def get_summary_by_ids(self, trans_ids: list[int]) -> list[dict]:
        if not trans_ids:
            return []
        placeholders = ",".join("?" * len(trans_ids))
        sql = Q.GET_SUMMARY_BY_IDS.format(placeholders=placeholders)
        rows = self.conn.execute(sql, trans_ids).fetchall()
        return [dict(r) for r in rows]

    def get_imbalanced(self) -> list[dict]:
        rows = self.conn.execute(Q.GET_IMBALANCED).fetchall()
        return [dict(r) for r in rows]

    def get_empty(self) -> list[Transaction]:
        rows = self.conn.execute(Q.GET_EMPTY).fetchall()
        return [_row_to_trans(r) for r in rows]

    def get_autocomplete(self, account_id: int, prefix: str) -> list[Transaction]:
        rows = self.conn.execute(Q.GET_AUTOCOMPLETE, (account_id, prefix + "%")).fetchall()
        return [_row_to_trans(r) for r in rows]

    def get_splits_for_trans(self, trans_id: int) -> list[dict]:
        rows = self.conn.execute(Q.GET_SPLITS_FOR_TRANS, (trans_id,)).fetchall()
        return [dict(r) for r in rows]
