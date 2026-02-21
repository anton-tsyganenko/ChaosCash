"""Searchable account combo delegate."""

from app.repositories.account_repo import AccountRepo
from app.ui.delegates.searchable_combo_delegate import SearchableComboDelegate


class AccountComboDelegate(SearchableComboDelegate):
    """Searchable combobox for account selection in splits."""

    def __init__(self, account_repo: AccountRepo, settings, parent=None):
        super().__init__(parent)
        self.account_repo = account_repo
        self.settings = settings

    def _get_items(self) -> list[tuple[str, int]]:
        """Return list of (path, id) for selectable accounts."""
        all_accounts = self.account_repo.get_all()
        account_map = {account.id: account for account in all_accounts}

        def build_path(account_id: int) -> str:
            parts = []
            current_id = account_id
            while current_id is not None:
                account = account_map.get(current_id)
                if account is None:
                    break
                parts.insert(0, account.name)
                current_id = account.parent
            return self.settings.account_path_sep.join(parts)

        show_hidden = self.settings.show_hidden_accounts
        items: list[tuple[str, int]] = []
        for account in all_accounts:
            if account.status == "GRP":
                continue
            if account.status == "HID" and not show_hidden:
                continue
            items.append((build_path(account.id), account.id))

        items.sort(key=lambda item: item[0].lower())
        return items
