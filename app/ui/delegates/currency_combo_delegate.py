"""Searchable currency combo delegate."""

from app.repositories.currency_repo import CurrencyRepo
from app.ui.delegates.searchable_combo_delegate import SearchableComboDelegate


class CurrencyComboDelegate(SearchableComboDelegate):
    """Searchable combobox for currency selection in splits."""

    def __init__(self, currency_repo: CurrencyRepo, parent=None):
        super().__init__(parent)
        self.currency_repo = currency_repo

    def _get_items(self) -> list[tuple[str, int]]:
        return [(currency.code, currency.id) for currency in self.currency_repo.get_all()]
