"""Business logic for creating, duplicating, and reversing transactions."""
from datetime import datetime, timezone
from app.repositories.transaction_repo import TransactionRepo
from app.repositories.split_repo import SplitRepo
from app.models.transaction import Transaction
from app.models.split import Split


UTC = timezone.utc


def _utc_now() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")


class TransactionService:
    def __init__(self, trans_repo: TransactionRepo, split_repo: SplitRepo):
        self.trans_repo = trans_repo
        self.split_repo = split_repo

    def create_transaction(self, description: str | None, date: str | None = None) -> int:
        """Create a new transaction. Returns new ID."""
        if date is None:
            date = _utc_now()
        return self.trans_repo.insert(date, description)

    def update_transaction(self, trans_id: int, date: str, description: str | None) -> None:
        self.trans_repo.update(trans_id, date, description)

    def delete_transaction(self, trans_id: int) -> None:
        self.trans_repo.delete(trans_id)

    def add_split(self, trans_id: int, account_id: int, currency_id: int,
                  description: str | None = None, external_id: str | None = None,
                  amount: int = 0, amount_fixed: bool = False) -> int:
        return self.split_repo.insert(trans_id, account_id, currency_id,
                                       description, external_id, amount, amount_fixed)

    def update_split(self, split_id: int, account_id: int, currency_id: int,
                     description: str | None, external_id: str | None,
                     amount: int, amount_fixed: bool) -> None:
        self.split_repo.update(split_id, account_id, currency_id,
                                description, external_id, amount, amount_fixed)

    def update_split_fixed(self, split_id: int, amount_fixed: bool) -> None:
        self.split_repo.update_amount_fixed(split_id, amount_fixed)

    def delete_split(self, split_id: int) -> None:
        self.split_repo.delete(split_id)

    def duplicate_transaction(self, trans_id: int) -> int:
        """Create a copy of the transaction with today's date. Returns new ID."""
        original = self.trans_repo.get_by_id(trans_id)
        if original is None:
            raise ValueError(f"Transaction {trans_id} not found")
        splits = self.split_repo.get_by_transaction(trans_id)
        new_id = self.trans_repo.insert(_utc_now(), original.description)
        for s in splits:
            self.split_repo.insert(new_id, s.account, s.currency,
                                    s.description, None, s.amount, s.amount_fixed)
        return new_id

    def reverse_transaction(self, trans_id: int) -> int:
        """Create a reversal transaction (all amounts negated). Returns new ID."""
        original = self.trans_repo.get_by_id(trans_id)
        if original is None:
            raise ValueError(f"Transaction {trans_id} not found")
        splits = self.split_repo.get_by_transaction(trans_id)
        desc = f"Reversal: {original.description}" if original.description else "Reversal"
        new_id = self.trans_repo.insert(_utc_now(), desc)
        for s in splits:
            self.split_repo.insert(new_id, s.account, s.currency,
                                    s.description, None, -s.amount, s.amount_fixed)
        return new_id

    def recalculate_flexible_splits(self, changed_split_id: int, new_amount: int,
                                    currency_id: int, trans_id: int) -> bool:
        """
        Proportionally recalculate flexible splits after one split's amount changes.
        Returns True if recalculation was possible, False if phantom row is needed.
        """
        splits = self.split_repo.get_by_transaction_and_currency(trans_id, currency_id)
        flexible = [s for s in splits if not s.amount_fixed and s.id != changed_split_id]

        if not flexible:
            return False  # No flexible splits, caller should show phantom row

        fixed_total = new_amount + sum(
            s.amount for s in splits if s.amount_fixed and s.id != changed_split_id
        )
        remaining = -fixed_total

        flexible_total = sum(s.amount for s in flexible)
        if flexible_total == 0:
            per_split = remaining // len(flexible)
            leftover = remaining - per_split * len(flexible)
            for i, s in enumerate(flexible):
                self.split_repo.update_amount(s.id, per_split + (leftover if i == 0 else 0))
        else:
            distributed = 0
            for i, s in enumerate(flexible[:-1]):
                new_val = round(s.amount * remaining / flexible_total)
                self.split_repo.update_amount(s.id, new_val)
                distributed += new_val
            # Last one gets the remainder to avoid rounding errors
            self.split_repo.update_amount(flexible[-1].id, remaining - distributed)
        return True
