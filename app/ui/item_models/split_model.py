"""QAbstractTableModel for splits of the selected transaction."""
from __future__ import annotations
from PyQt6.QtCore import Qt, QModelIndex, QAbstractTableModel
from PyQt6.QtGui import QColor
from app.repositories.split_repo import SplitRepo
from app.repositories.account_repo import AccountRepo
from app.repositories.currency_repo import CurrencyRepo
from app.models.split import Split
from app.utils.amount_math import format_amount
from app.i18n import tr

COL_ID = 0
COL_EXTID = 1
COL_DESC = 2
COL_ACCOUNT = 3
COL_FIXED = 4
COL_AMOUNT = 5
COL_CURRENCY = 6
NUM_COLS = 7

# Sentinel row type
ROW_REAL = "real"
ROW_PHANTOM = "phantom"
ROW_NEW = "new"


class SplitRow:
    __slots__ = ("split", "row_type", "phantom_currency_id", "phantom_amount")

    def __init__(self, split: Split | None, row_type: str = ROW_REAL,
                 phantom_currency_id: int | None = None, phantom_amount: int = 0):
        self.split = split
        self.row_type = row_type
        self.phantom_currency_id = phantom_currency_id
        self.phantom_amount = phantom_amount


class SplitModel(QAbstractTableModel):
    """Displays splits for the selected transaction, including helper rows."""

    def __init__(self, split_repo: SplitRepo, account_repo: AccountRepo,
                 currency_repo: CurrencyRepo, settings, parent=None):
        super().__init__(parent)
        self.split_repo = split_repo
        self.account_repo = account_repo
        self.currency_repo = currency_repo
        self.settings = settings

        self._rows: list[SplitRow] = []
        self._trans_id: int | None = None
        self._accounts: dict[int, object] = {}
        self._currencies: dict[int, object] = {}
        self._zero_split_ids: set[int] = set()
        self._cell_overrides: dict[tuple[int, int], dict] = {}

    def load(self, trans_id: int | None) -> None:
        self.beginResetModel()
        self._trans_id = trans_id
        self._cell_overrides = {}
        self._accounts = {a.id: a for a in self.account_repo.get_all()}
        self._currencies = {c.id: c for c in self.currency_repo.get_all()}

        if trans_id is None:
            self._rows = []
            self.endResetModel()
            return

        splits = self.split_repo.get_by_transaction(trans_id)
        self._rows = [SplitRow(s) for s in splits]
        self._add_phantom_rows(splits)
        self.endResetModel()

    def _add_phantom_rows(self, splits: list[Split]) -> None:
        from collections import defaultdict
        totals: dict[int, int] = defaultdict(int)
        for s in splits:
            totals[s.currency] += s.amount
        for cid, total in totals.items():
            if total != 0:
                self._rows.append(SplitRow(None, ROW_PHANTOM, cid, -total))
        self._rows.append(SplitRow(None, ROW_NEW))

    def set_zero_split_ids(self, ids: set[int]) -> None:
        self._zero_split_ids = ids
        if self._rows:
            self.dataChanged.emit(
                self.index(0, 0),
                self.index(len(self._rows) - 1, NUM_COLS - 1),
                [Qt.ItemDataRole.BackgroundRole],
            )

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self._rows) if not parent.isValid() else 0

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return NUM_COLS

    def headerData(self, section: int, orientation: Qt.Orientation,
                   role: int = Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return [
                tr("ID"), tr("Ext. ID"), tr("Description"), tr("Account"),
                tr("Fixed"), tr("Amount"), tr("Currency"),
            ][section]
        return None

    def _account_name(self, account_id: int | None) -> str:
        if account_id is None:
            return ""
        acc = self._accounts.get(account_id)
        if acc is None:
            return str(account_id)
        return self._build_path(account_id)

    def _build_path(self, account_id: int) -> str:
        parts = []
        cid = account_id
        while cid is not None:
            acc = self._accounts.get(cid)
            if acc is None:
                break
            parts.insert(0, acc.name)
            cid = acc.parent
        return self.settings.account_path_sep.join(parts)

    def _currency_code(self, currency_id: int | None) -> str:
        if currency_id is None:
            return ""
        cur = self._currencies.get(currency_id)
        return cur.code if cur else str(currency_id)

    def _format_amt(self, quants: int, currency_id: int | None) -> str:
        if currency_id is None:
            return ""
        cur = self._currencies.get(currency_id)
        if cur is None:
            return str(quants)
        return format_amount(
            quants, cur.denominator,
            self.settings.decimal_sep,
            self.settings.thousands_sep,
            self.settings.show_thousands,
        )

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or index.row() >= len(self._rows):
            return None
        row_obj = self._rows[index.row()]
        col = index.column()

        override = self._cell_overrides.get((index.row(), col))
        if override is not None:
            if role in override:
                return override[role]
            if role == Qt.ItemDataRole.DisplayRole and Qt.ItemDataRole.EditRole in override:
                return override[Qt.ItemDataRole.EditRole]

        if role == Qt.ItemDataRole.DisplayRole:
            if row_obj.row_type == ROW_PHANTOM:
                if col == COL_AMOUNT:
                    return self._format_amt(row_obj.phantom_amount, row_obj.phantom_currency_id)
                if col == COL_CURRENCY:
                    return self._currency_code(row_obj.phantom_currency_id)
                if col == COL_DESC:
                    return tr("(imbalance — select account)")
                return ""
            if row_obj.row_type == ROW_NEW:
                if col == COL_DESC:
                    return tr("(new split — fill account, amount, currency)")
                return ""
            s = row_obj.split
            if col == COL_ID:
                return str(s.id)
            if col == COL_EXTID:
                return s.external_id or ""
            if col == COL_DESC:
                return s.description or ""
            if col == COL_ACCOUNT:
                return self._account_name(s.account)
            if col == COL_AMOUNT:
                return self._format_amt(s.amount, s.currency)
            if col == COL_CURRENCY:
                return self._currency_code(s.currency)
            return None

        if role == Qt.ItemDataRole.EditRole:
            if row_obj.row_type == ROW_REAL and row_obj.split:
                s = row_obj.split
                if col == COL_EXTID:
                    return s.external_id or ""
                if col == COL_DESC:
                    return s.description or ""
                if col == COL_AMOUNT:
                    return self._format_amt(s.amount, s.currency)
            return None

        if role == Qt.ItemDataRole.CheckStateRole:
            if col == COL_FIXED and row_obj.row_type == ROW_REAL and row_obj.split:
                return Qt.CheckState.Checked if row_obj.split.amount_fixed else Qt.CheckState.Unchecked

        if role == Qt.ItemDataRole.TextAlignmentRole:
            if col == COL_AMOUNT:
                return int(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        if role == Qt.ItemDataRole.UserRole:
            if row_obj.row_type == ROW_REAL and row_obj.split:
                s = row_obj.split
                if col == COL_ACCOUNT:
                    return s.account
                if col == COL_CURRENCY:
                    return s.currency
                return s.id
            return None

        if role == Qt.ItemDataRole.ForegroundRole:
            if row_obj.row_type in (ROW_PHANTOM, ROW_NEW):
                return QColor(140, 140, 140)

        if role == Qt.ItemDataRole.BackgroundRole:
            if row_obj.row_type == ROW_PHANTOM:
                return QColor(255, 230, 180)
            if row_obj.row_type == ROW_NEW:
                return QColor(230, 240, 255)
            if row_obj.row_type == ROW_REAL and row_obj.split and row_obj.split.id in self._zero_split_ids:
                return QColor(255, 255, 180)

        return None

    def setData(self, index: QModelIndex, value,
                role: int = Qt.ItemDataRole.EditRole) -> bool:
        if not index.isValid() or index.row() >= len(self._rows):
            return False
        f = self.flags(index)
        if not (f & (Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsUserCheckable)):
            return False

        key = (index.row(), index.column())
        if key not in self._cell_overrides:
            self._cell_overrides[key] = {}
        self._cell_overrides[key][role] = value
        self.dataChanged.emit(index, index, [role])
        return True

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        row_obj = self._rows[index.row()]
        base = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
        if row_obj.row_type == ROW_PHANTOM:
            if index.column() == COL_ACCOUNT:
                return base | Qt.ItemFlag.ItemIsEditable
            return base
        if row_obj.row_type == ROW_NEW:
            if index.column() in (COL_ACCOUNT, COL_AMOUNT, COL_CURRENCY):
                return base | Qt.ItemFlag.ItemIsEditable
            return base
        col = index.column()
        if col == COL_FIXED:
            return base | Qt.ItemFlag.ItemIsUserCheckable
        if col in (COL_EXTID, COL_DESC, COL_ACCOUNT, COL_AMOUNT, COL_CURRENCY):
            return base | Qt.ItemFlag.ItemIsEditable
        return base

    def get_split(self, row: int) -> Split | None:
        if 0 <= row < len(self._rows):
            return self._rows[row].split
        return None

    def get_row_type(self, row: int) -> str | None:
        if 0 <= row < len(self._rows):
            return self._rows[row].row_type
        return None

    def get_phantom_info(self, row: int) -> tuple[int | None, int]:
        r = self._rows[row]
        return r.phantom_currency_id, r.phantom_amount

    def sort(self, column: int, order: Qt.SortOrder = Qt.SortOrder.AscendingOrder) -> None:
        """Sort only editable split rows; keep phantom/new rows at the bottom."""
        reverse = order == Qt.SortOrder.DescendingOrder
        real_rows = [r for r in self._rows if r.row_type == ROW_REAL]
        extra_rows = [r for r in self._rows if r.row_type != ROW_REAL]

        def key(row_obj: SplitRow):
            s = row_obj.split
            if s is None:
                return 0
            if column == COL_ID:
                return s.id
            if column == COL_EXTID:
                return (s.external_id or "").lower()
            if column == COL_DESC:
                return (s.description or "").lower()
            if column == COL_ACCOUNT:
                return self._account_name(s.account).lower()
            if column == COL_FIXED:
                return int(bool(s.amount_fixed))
            if column == COL_AMOUNT:
                return s.amount
            if column == COL_CURRENCY:
                # keep amount as secondary key for currency sorting
                return (self._currency_code(s.currency).lower(), s.amount)
            return 0

        self.layoutAboutToBeChanged.emit()
        real_rows.sort(key=key, reverse=reverse)
        self._rows = real_rows + extra_rows
        self._cell_overrides = {}
        self.layoutChanged.emit()

    def set_filter(self, filter_text: str = "") -> None:
        """Placeholder for future filtering support."""
        pass
