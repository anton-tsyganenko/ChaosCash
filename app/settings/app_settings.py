"""Application settings stored in QSettings."""
from PyQt6.QtCore import QSettings

_ORG = "chaoscash"
_APP = "chaoscash"

_DEFAULTS = {
    "date_format": "yyyy-MM-dd HH:mm:ss",
    "timezone": "",           # empty = system timezone
    "decimal_sep": ".",
    "thousands_sep": " ",
    "show_thousands": True,
    "account_path_sep": ":",
    "account_sort": "name",   # name | code | name_code | code_name
    "show_hidden_accounts": False,
    "show_balances": True,
    "transaction_view_mode": "verbose",  # verbose | summary
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
    def show_thousands(self) -> bool:
        return bool(self.thousands_sep)

    @property
    def account_path_sep(self) -> str:
        return str(self.get("account_path_sep"))

    @property
    def account_sort(self) -> str:
        return str(self.get("account_sort"))

    @property
    def show_hidden_accounts(self) -> bool:
        v = self.get("show_hidden_accounts")
        return v if isinstance(v, bool) else v == "true"

    @show_hidden_accounts.setter
    def show_hidden_accounts(self, value: bool) -> None:
        self.set("show_hidden_accounts", value)

    @property
    def show_balances(self) -> bool:
        v = self.get("show_balances")
        return v if isinstance(v, bool) else v == "true"

    @show_balances.setter
    def show_balances(self, value: bool) -> None:
        self.set("show_balances", value)

    @property
    def transaction_view_mode(self) -> str:
        return str(self.get("transaction_view_mode"))

    @transaction_view_mode.setter
    def transaction_view_mode(self, value: str) -> None:
        self.set("transaction_view_mode", value)
