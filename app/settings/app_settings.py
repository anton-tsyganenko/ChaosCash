"""Application settings stored in QSettings."""
from PyQt6.QtCore import QSettings

_ORG = "chaoscash"
_APP = "chaoscash"

_DEFAULTS = {
    "date_format": "yyyy-MM-dd HH:mm:ss",
    "timezone": "",           # empty = system timezone
    "decimal_sep": ".",
    "thousands_sep": " ",
    "account_path_sep": ":",
    "show_hidden_accounts": False,
    "allow_grouping_accounts_for_splits": False,
    "transaction_view_mode": "detailed",  # detailed | aggregated
}


class AppSettings:
    """Thin wrapper around QSettings for typed access to app settings."""

    def __init__(self):
        self._s = QSettings(_ORG, _APP)

    def get(self, key: str):
        return self._s.value(key, _DEFAULTS.get(key))

    def set(self, key: str, value) -> None:
        self._s.setValue(key, value)

    # Convenience properties
    @property
    def date_format(self) -> str:
        return str(self.get("date_format"))

    @property
    def decimal_sep(self) -> str:
        return str(self.get("decimal_sep"))

    @property
    def thousands_sep(self) -> str:
        return str(self.get("thousands_sep"))

    @property
    def account_path_sep(self) -> str:
        return str(self.get("account_path_sep"))

    @property
    def show_hidden_accounts(self) -> bool:
        v = self.get("show_hidden_accounts")
        return v if isinstance(v, bool) else v == "true"

    @show_hidden_accounts.setter
    def show_hidden_accounts(self, value: bool) -> None:
        self.set("show_hidden_accounts", value)


    @property
    def allow_grouping_accounts_for_splits(self) -> bool:
        v = self.get("allow_grouping_accounts_for_splits")
        return v if isinstance(v, bool) else v == "true"

    @allow_grouping_accounts_for_splits.setter
    def allow_grouping_accounts_for_splits(self, value: bool) -> None:
        self.set("allow_grouping_accounts_for_splits", value)
    @property
    def transaction_view_mode(self) -> str:
        return str(self.get("transaction_view_mode"))

    @transaction_view_mode.setter
    def transaction_view_mode(self, value: str) -> None:
        self.set("transaction_view_mode", value)
