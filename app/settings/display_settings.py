"""Per-panel display settings (column visibility, order, widths, sort)."""
from PyQt6.QtCore import QSettings

_ORG = "chaoscash"
_APP = "chaoscash"


class DisplaySettings:
    """Stores display configuration for a named panel."""

    def __init__(self, panel_name: str):
        self._s = QSettings(_ORG, _APP)
        self._panel = panel_name

    def _key(self, name: str) -> str:
        return f"display/{self._panel}/{name}"

    def get_column_order(self, default: list[int]) -> list[int]:
        v = self._s.value(self._key("column_order"), None)
        if v is None:
            return default
        return [int(x) for x in v]

    def set_column_order(self, order: list[int]) -> None:
        self._s.setValue(self._key("column_order"), order)

    def get_column_widths(self, default: dict[int, int]) -> dict[int, int]:
        v = self._s.value(self._key("column_widths"), None)
        if v is None:
            return default
        return {int(k): int(w) for k, w in v.items()}

    def set_column_widths(self, widths: dict[int, int]) -> None:
        self._s.setValue(self._key("column_widths"), widths)

    def get_hidden_columns(self, default: list[int]) -> list[int]:
        v = self._s.value(self._key("hidden_columns"), None)
        if v is None:
            return default
        return [int(x) for x in v]

    def set_hidden_columns(self, cols: list[int]) -> None:
        self._s.setValue(self._key("hidden_columns"), cols)

    def get_sort_column(self, default: int = -1) -> int:
        return int(self._s.value(self._key("sort_column"), default))

    def set_sort_column(self, col: int) -> None:
        self._s.setValue(self._key("sort_column"), col)

    def get_sort_order(self, default: int = 0) -> int:
        return int(self._s.value(self._key("sort_order"), default))

    def set_sort_order(self, order: int) -> None:
        self._s.setValue(self._key("sort_order"), order)
