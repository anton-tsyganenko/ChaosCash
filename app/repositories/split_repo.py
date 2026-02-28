import sqlite3
from app.models.split import Split
from app.database.queries import splits as Q


def _row_to_split(row) -> Split:
    return Split(
        id=row["ID"],
        trans=row["Trans"],
        account=row["Account"],
        currency=row["Currency"],
        description=row["Description"],
        external_id=row["ExternalID"],
        amount=row["Amount"],
        amount_fixed=bool(row["AmountFixed"]),
    )


class SplitRepo:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def get_by_id(self, split_id: int) -> Split | None:
        row = self.conn.execute(Q.GET_BY_ID, (split_id,)).fetchone()
        return _row_to_split(row) if row else None

    def get_by_transaction(self, trans_id: int) -> list[Split]:
        rows = self.conn.execute(Q.GET_BY_TRANSACTION, (trans_id,)).fetchall()
        return [_row_to_split(r) for r in rows]

    def get_by_transaction_and_currency(self, trans_id: int, currency_id: int) -> list[Split]:
        rows = self.conn.execute(Q.GET_BY_TRANSACTION_AND_CURRENCY, (trans_id, currency_id)).fetchall()
        return [_row_to_split(r) for r in rows]

    def insert(self, trans_id: int, account_id: int, currency_id: int,
               description: str | None, external_id: str | None,
               amount: int, amount_fixed: bool = False) -> int:
        cur = self.conn.execute(Q.INSERT, (trans_id, account_id, currency_id,
                                            description, external_id, amount, int(amount_fixed)))
        self.conn.commit()
        return cur.lastrowid

    def update(self, split_id: int, account_id: int, currency_id: int,
               description: str | None, external_id: str | None,
               amount: int, amount_fixed: bool) -> None:
        self.conn.execute(Q.UPDATE, (account_id, currency_id, description,
                                      external_id, amount, int(amount_fixed), split_id))
        self.conn.commit()

    def update_amount(self, split_id: int, amount: int) -> None:
        self.conn.execute(Q.UPDATE_AMOUNT, (amount, split_id))
        self.conn.commit()

    def update_amount_fixed(self, split_id: int, fixed: bool) -> None:
        self.conn.execute(Q.UPDATE_AMOUNT_FIXED, (int(fixed), split_id))
        self.conn.commit()

    def update_account(self, split_id: int, account_id: int) -> None:
        self.conn.execute(Q.UPDATE_ACCOUNT, (account_id, split_id))
        self.conn.commit()

    def delete(self, split_id: int) -> None:
        self.conn.execute(Q.DELETE, (split_id,))
        self.conn.commit()

    def delete_by_account(self, account_id: int) -> None:
        self.conn.execute(Q.DELETE_BY_ACCOUNT, (account_id,))
        self.conn.commit()

    def get_last_currency_for_account(self, account_id: int) -> int | None:
        row = self.conn.execute(Q.GET_LAST_CURRENCY_FOR_ACCOUNT, (account_id,)).fetchone()
        return row[0] if row else None

    def get_splits_with_zero_amount(self) -> list[int]:
        rows = self.conn.execute(Q.CHECK_ZERO_AMOUNTS).fetchall()
        return [r[0] for r in rows]

    def has_splits_for_account(self, account_id: int) -> bool:
        """Check if an account has any splits."""
        row = self.conn.execute(Q.HAS_SPLITS_FOR_ACCOUNT, (account_id,)).fetchone()
        return row is not None
