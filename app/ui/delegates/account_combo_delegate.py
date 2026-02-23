"""Searchable account combo delegate."""

from app.repositories.account_repo import AccountRepo
from app.ui.account_selection import get_selectable_account_items
from app.ui.delegates.searchable_combo_delegate import SearchableComboDelegate


class AccountComboDelegate(SearchableComboDelegate):
    """Searchable combobox for account selection in splits."""

    def __init__(self, account_repo: AccountRepo, settings, parent=None):
        super().__init__(parent)
        self.account_repo = account_repo
        self.settings = settings

    def _get_items(self) -> list[tuple[str, int]]:
        """Return list of (path, id) for selectable accounts."""
        return get_selectable_account_items(self.account_repo, self.settings)
