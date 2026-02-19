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

COL_EXTID = 0
COL_DESC = 1
COL_ACCOUNT = 2
COL_FIXED = 3
COL_AMOUNT = 4
COL_CURRENCY = 5
NUM_COLS = 6

# Sentinel row type
ROW_REAL = "real"
ROW_PHANTOM = "phantom"


class SplitRow:
    __slots__ = ("split", "row_type", "phantom_currency_id", "phantom_amount")

    def __init__(self, split: Split | None, row_type: str = ROW_REAL,
                 phantom_currency_id: int | None = None, phantom_amount: int = 0):
        self.split = split
        self.row_type = row_type
        self.phantom_currency_id = phantom_currency_id
        self.phantom_amount = phantom_amount


class SplitModel(QAbstractTableModel):
    """
    Displays splits for the currently selected transaction.
    Includes phantom rows for imbalance.
    """

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

    def load(self, trans_id: int | None) -> None:
        self.beginResetModel()
        self._trans_id = trans_id
        self._accounts = {a.id: a for a in self.account_repo.get_all()}
        self._currencies = {c.id: c for c in self.currency_repo.get_all()}

        if trans_id is None:
            self._rows = []
            self.endResetModel()
            return

        splits = self.split_repo.get_by_transaction(trans_id)
        self._rows = [SplitRow(s) for s in splits]

        # Add phantom rows for imbalanced currencies
        self._add_phantom_rows(splits)

        self.endResetModel()

    def _add_phantom_rows(self, splits: list[Split]) -> None:
        from collections import defaultdict
        totals: dict[int, int] = defaultdict(int)
        for s in splits:
            totals[s.currency] += s.amount
        for cid, total in totals.items():
            if total != 0:
                self._rows.append(SplitRow(
                    None, ROW_PHANTOM, cid, -total
                ))

    def set_zero_split_ids(self, ids: set[int]) -> None:
        self._zero_split_ids = ids
        if self._rows:
            self.dataChanged.emit(
                self.index(0, 0),
                self.index(len(self._rows) - 1, NUM_COLS - 1),
                [Qt.ItemDataRole.BackgroundRole]
            )

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return len(self._rows) if not parent.isValid() else 0

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return NUM_COLS

    def headerData(self, section: int, orientation: Qt.Orientation,
                   role: int = Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return [tr("Ext. ID"), tr("Description"), tr("Account"),
                    tr("Fixed"), tr("Amount"), tr("Currency")][section]
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
        row = self._rows[index.row()]
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if row.row_type == ROW_PHANTOM:
                if col == COL_AMOUNT:
                    return self._format_amt(row.phantom_amount, row.phantom_currency_id)
                elif col == COL_CURRENCY:
                    return self._currency_code(row.phantom_currency_id)
                elif col == COL_DESC:
                    return tr("(imbalance — select account)")
                return ""
            s = row.split
            if col == COL_EXTID:
                return s.external_id or ""
            elif col == COL_DESC:
                return s.description or ""
            elif col == COL_ACCOUNT:
                return self._account_name(s.account)
            elif col == COL_AMOUNT:
                return self._format_amt(s.amount, s.currency)
            elif col == COL_CURRENCY:
                return self._currency_code(s.currency)
            return None

        elif role == Qt.ItemDataRole.CheckStateRole:
            if col == COL_FIXED and row.row_type == ROW_REAL and row.split:
                return Qt.CheckState.Checked if row.split.amount_fixed else Qt.CheckState.Unchecked

        elif role == Qt.ItemDataRole.TextAlignmentRole:
            if col == COL_AMOUNT:
                return int(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        elif role == Qt.ItemDataRole.UserRole:
            if row.row_type == ROW_REAL and row.split:
                return row.split.id
            if row.row_type == ROW_PHANTOM:
                return None

        elif role == Qt.ItemDataRole.BackgroundRole:
            if row.row_type == ROW_PHANTOM:
                return QColor(255, 230, 180)
            if row.row_type == ROW_REAL and row.split:
                if row.split.id in self._zero_split_ids:
                    return QColor(255, 255, 180)  # Yellow warning for zero splits

        return None

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        row = self._rows[index.row()]
        base = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
        if row.row_type == ROW_PHANTOM:
            if index.column() == COL_ACCOUNT:
                return base | Qt.ItemFlag.ItemIsEditable
            return base
        # Real row
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

    def set_filter(self, filter_text: str = "") -> None:
        """Placeholder for future filtering support."""
        pass
