"""Balance calculation service with lazy-loading cache."""
from collections import defaultdict
from app.repositories.account_repo import AccountRepo
from app.repositories.split_repo import SplitRepo


class BalanceService:
    """
    Calculates and caches account balances.

    Cache key: (account_id, currency_id) -> amount_in_quants
    GRP accounts are computed recursively from children.
    """

    def __init__(self, account_repo: AccountRepo, split_repo: SplitRepo):
        self.account_repo = account_repo
        self.split_repo = split_repo
        # {(account_id, currency_id): quants}
        self._cache: dict[tuple[int, int], int] = {}
        # {account_id: {currency_id: quants}}  — leaf balances only
        self._leaf_cache: dict[int, dict[int, int]] = {}

    def invalidate(self, account_id: int, currency_id: int | None = None) -> None:
        """Invalidate account and all its ancestors up to root."""
        current_id: int | None = account_id
        while current_id is not None:
            if currency_id is not None:
                self._cache.pop((current_id, currency_id), None)
            else:
                # Invalidate all currencies for this account
                keys = [k for k in self._cache if k[0] == current_id]
                for k in keys:
                    del self._cache[k]
            self._leaf_cache.pop(current_id, None)
            current_id = self.account_repo.get_parent_id(current_id)

    def invalidate_account_tree(self, account_id: int) -> None:
        """Invalidate account, all its ancestors, and all its descendants."""
        self.invalidate(account_id)
        for child in self.account_repo.get_children(account_id):
            self.invalidate_account_tree(child.id)

    def get_balance(self, account_id: int) -> dict[int, int]:
        """Return {currency_id: total_quants} for account (recursive for GRP)."""
        children = self.account_repo.get_children(account_id)
        if not children:
            return self._get_leaf_balance(account_id)
        else:
            result: dict[int, int] = defaultdict(int)
            for child in children:
                for cid, quants in self.get_balance(child.id).items():
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
        self._cache.clear()
        self._leaf_cache.clear()
