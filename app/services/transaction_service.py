"""Business logic for creating, duplicating, and reversing transactions."""
from datetime import datetime, timezone
from app.repositories.transaction_repo import TransactionRepo
from app.repositories.split_repo import SplitRepo

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

    def delete_split_and_rebalance(self, split_id: int) -> bool:
        """Delete split and rebalance remaining unfixed splits if possible."""
        split = self.split_repo.get_by_id(split_id)
        if split is None:
            return False

        trans_id = split.trans
        currency_id = split.currency
        self.split_repo.delete(split_id)

        currency_splits = self.split_repo.get_by_transaction_and_currency(trans_id, currency_id)
        imbalance = sum(s.amount for s in currency_splits)
        return self.recalculate_flexible_splits(imbalance, currency_id, trans_id)

    def duplicate_transaction(self, trans_id: int) -> int:
        """Create a copy of the transaction with today's date. Returns new ID."""
        return self._copy_transaction(
            trans_id,
            description_builder=lambda original: original.description,
            amount_transform=lambda amount: amount,
        )

    def reverse_transaction(self, trans_id: int) -> int:
        """Create a reversal transaction (all amounts negated). Returns new ID."""
        return self._copy_transaction(
            trans_id,
            description_builder=lambda original: (
                f"Reversal: {original.description}" if original.description else "Reversal"
            ),
            amount_transform=lambda amount: -amount,
        )

    def _copy_transaction(self, trans_id: int, description_builder,
                          amount_transform) -> int:
        """Copy transaction and its splits with optional transformations."""
        original = self.trans_repo.get_by_id(trans_id)
        if original is None:
            raise ValueError(f"Transaction {trans_id} not found")

        splits = self.split_repo.get_by_transaction(trans_id)
        new_id = self.trans_repo.insert(_utc_now(), description_builder(original))
        for split in splits:
            self.split_repo.insert(
                new_id,
                split.account,
                split.currency,
                split.description,
                None,
                amount_transform(split.amount),
                split.amount_fixed,
            )
        return new_id

    def recalculate_flexible_splits(self, delta_amount: int,
                                    currency_id: int, trans_id: int) -> bool:
        """Distribute ``delta_amount`` across unfixed splits in a currency.

        Use cases:
        - amount edit: pass changed_amount_delta = new_amount - old_amount
        - existing imbalance: pass current imbalance sum for the currency

        Returns True if distribution happened, False when there are no unfixed splits
        (or delta is zero).
        """
        if delta_amount == 0:
            return False

        splits = self.split_repo.get_by_transaction_and_currency(trans_id, currency_id)
        flexible = [s for s in splits if not s.amount_fixed]
        if not flexible:
            return False

        distribute_total = -delta_amount
        flexible_total = sum(s.amount for s in flexible)
        if flexible_total == 0:
            per_split = distribute_total // len(flexible)
            leftover = distribute_total - per_split * len(flexible)
            for i, s in enumerate(flexible):
                self.split_repo.update_amount(s.id, s.amount + per_split + (leftover if i == 0 else 0))
        else:
            distributed = 0
            for s in flexible[:-1]:
                delta = round(s.amount * distribute_total / flexible_total)
                self.split_repo.update_amount(s.id, s.amount + delta)
                distributed += delta
            self.split_repo.update_amount(
                flexible[-1].id,
                flexible[-1].amount + (distribute_total - distributed),
            )
        return True
