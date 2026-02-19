"""Integrity checks: imbalanced transactions, empty transactions, zero-amount splits."""
import sqlite3
from app.repositories.transaction_repo import TransactionRepo
from app.repositories.split_repo import SplitRepo
from app.models.transaction import Transaction


class IntegrityService:
    def __init__(self, trans_repo: TransactionRepo, split_repo: SplitRepo,
                 conn: sqlite3.Connection):
        self.trans_repo = trans_repo
        self.split_repo = split_repo
        self.conn = conn

    def get_imbalanced_trans_ids(self) -> list[int]:
        """Return IDs of transactions where sum of splits != 0 per currency."""
        rows = self.trans_repo.get_imbalanced()
        return list({r["Trans"] for r in rows})

    def get_empty_transactions(self) -> list[Transaction]:
        """Return transactions with no splits."""
        return self.trans_repo.get_empty()

    def get_zero_split_ids(self) -> list[int]:
        """Return IDs of splits with Amount=0."""
        return self.split_repo.get_splits_with_zero_amount()

    def check_foreign_keys(self) -> list[str]:
        """Run PRAGMA foreign_key_check and return any violations as strings."""
        rows = self.conn.execute("PRAGMA foreign_key_check").fetchall()
        return [str(dict(r)) for r in rows]

    def has_imbalance(self) -> bool:
        return bool(self.get_imbalanced_trans_ids())

    def has_empty_transactions(self) -> bool:
        return bool(self.get_empty_transactions())
