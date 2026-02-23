"""Balance calculation service."""
from collections import defaultdict
from app.repositories.account_repo import AccountRepo
from app.repositories.split_repo import SplitRepo


class BalanceService:
    """Calculates and caches account balances."""

    def __init__(self, account_repo: AccountRepo, split_repo: SplitRepo):
        self.account_repo = account_repo
        self.split_repo = split_repo
        # {account_id: {currency_id: quants}}  — leaf balances only
        self._leaf_cache: dict[int, dict[int, int]] = {}

    def invalidate(self, account_id: int, currency_id: int | None = None) -> None:
        """Invalidate account and all its ancestors up to root."""
        current_id: int | None = account_id
        while current_id is not None:
            self._leaf_cache.pop(current_id, None)
            current_id = self.account_repo.get_parent_id(current_id)

    def invalidate_account_tree(self, account_id: int) -> None:
        """Invalidate account, all its ancestors, and all its descendants."""
        self.invalidate(account_id)
        for child in self.account_repo.get_children(account_id):
            self.invalidate_account_tree(child.id)

    def get_balance(self, account_id: int, include_children: bool = True) -> dict[int, int]:
        """Return {currency_id: total_quants} for account."""
        if not include_children:
            return self._get_leaf_balance(account_id)

        result: dict[int, int] = defaultdict(int)
        for cid, quants in self._get_leaf_balance(account_id).items():
            result[cid] += quants

        for child in self.account_repo.get_children(account_id):
            for cid, quants in self.get_balance(child.id, include_children=True).items():
                result[cid] += quants
        return dict(result)

    def _get_leaf_balance(self, account_id: int) -> dict[int, int]:
        if account_id in self._leaf_cache:
            return self._leaf_cache[account_id]
        raw = self.split_repo.get_balance_by_account(account_id)
        balance = {cid: quants for cid, (quants, _) in raw.items()}
        self._leaf_cache[account_id] = balance
        return balance

    def clear(self) -> None:
        self._leaf_cache.clear()
