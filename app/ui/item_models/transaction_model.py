"""QAbstractTableModel for the transaction list with running balance."""
from __future__ import annotations
import math
from PyQt6.QtCore import Qt, QModelIndex, QAbstractTableModel, pyqtSignal, QTimer
from PyQt6.QtGui import QColor
from app.repositories.transaction_repo import TransactionRepo
from app.repositories.currency_repo import CurrencyRepo
from app.utils.date_utils import qt_format_to_strftime
from app.i18n import tr
from datetime import datetime, timezone, tzinfo as TZInfo

UTC = timezone.utc
FETCH_BLOCK = 500

COL_ID = 0
COL_DATE = 1
COL_DESC = 2
COL_AMOUNT = 3
COL_BALANCE = 4
COL_CURRENCY = 5
NUM_COLS = 6

HEADERS = ["ID", tr("Date"), tr("Description"), tr("Amount"), tr("Balance"), tr("Currency")]


class TransactionModel(QAbstractTableModel):
    """
    Displays transactions for selected accounts.
    Supports detailed (per-split) and aggregated (per-transaction) modes.
    Implements canFetchMore/fetchMore for lazy loading.
    Last row is always a phantom (empty) row for entering new transactions.
    """

    new_transaction_requested = pyqtSignal(str, str)  # description, utc_date

    def __init__(self, trans_repo: TransactionRepo, currency_repo: CurrencyRepo,
                 settings, parent=None):
        super().__init__(parent)
        self.trans_repo = trans_repo
        self.currency_repo = currency_repo
        self.settings = settings
        self._rows: list[dict] = []
        self._all_rows: list[dict] = []
        self._account_ids: list[int] = []
        self._currencies: dict[int, object] = {}
        self._local_tz: TZInfo = datetime.now().astimezone().tzinfo

    def _load_rows(self, rows_data: list[dict], account_ids: list[int]) -> None:
        """Internal method to initialize row data after fetch. Called by load() and load_by_ids()."""
        self._all_rows = rows_data
        self._rows = rows_data[:FETCH_BLOCK]
        self._account_ids = account_ids

    def load(self, account_ids: list[int]) -> None:
        self.beginResetModel()
        self._currencies = {c.id: c for c in self.currency_repo.get_all()}

        if not account_ids:
            self._load_rows([], account_ids)
            self.endResetModel()
            return

        mode = self.settings.transaction_view_mode
        if mode == "detailed":
            raw = self.trans_repo.get_verbose_by_accounts(account_ids)
        else:
            raw = self.trans_repo.get_summary_by_accounts(account_ids)

        self._load_rows(raw, account_ids)
        self.endResetModel()

    def load_by_ids(self, trans_ids: list[int]) -> None:
        """Load specific transactions by ID (for virtual nodes: imbalance, empty)."""
        self.beginResetModel()
        self._currencies = {c.id: c for c in self.currency_repo.get_all()}

        if not trans_ids:
            self._load_rows([], [])  # no phantom row for virtual node views
            self.endResetModel()
            return

        # Virtual views (imbalance, empty) always use aggregated mode: one row per
        # transaction+currency showing the net imbalance.
        raw = self.trans_repo.get_summary_by_ids(trans_ids)

        self._load_rows(raw, [])  # no phantom row for virtual node views
        self.endResetModel()

    def canFetchMore(self, parent: QModelIndex = QModelIndex()) -> bool:
        return len(self._rows) < len(self._all_rows)

    def fetchMore(self, parent: QModelIndex = QModelIndex()) -> None:
        start = len(self._rows)
        remainder = len(self._all_rows) - start
        items_to_fetch = min(FETCH_BLOCK, remainder)
        self.beginInsertRows(QModelIndex(), start, start + items_to_fetch - 1)
        self._rows.extend(self._all_rows[start:start + items_to_fetch])
        self.endInsertRows()

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        if parent.isValid():
            return 0
        # +1 for phantom entry row when accounts are loaded
        return len(self._rows) + (1 if self._account_ids else 0)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return NUM_COLS

    def headerData(self, section: int, orientation: Qt.Orientation,
                   role: int = Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return [tr("ID"), tr("Date"), tr("Description"),
                    tr("Amount"), tr("Balance"), tr("Currency")][section]
        return None

    def _is_phantom_row(self, row: int) -> bool:
        return bool(self._account_ids) and row == len(self._rows)

    def _phantom_date(self) -> str:
        """Current local time formatted per settings."""
        try:
            fmt = qt_format_to_strftime(self.settings.date_format)
            return datetime.now(self._local_tz).strftime(fmt)
        except Exception:
            return datetime.now().strftime("%Y-%m-%d")

    def _format_date(self, utc_str: str) -> str:
        if not utc_str:
            return ""
        try:
            dt = datetime.strptime(utc_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=UTC)
            dt_local = dt.astimezone(self._local_tz)
            fmt = qt_format_to_strftime(self.settings.date_format)
            return dt_local.strftime(fmt)
        except Exception:
            return utc_str

    def _format_amt(self, quants, denominator) -> str:
        if quants is None:
            return ""
        denom = int(denominator) if denominator else 1
        decimal_places = math.ceil(math.log10(denom))
        value = int(quants) / denom
        formatted = f"{value:,.{decimal_places}f}".translate(
            str.maketrans({",": self.settings.thousands_sep,
                          ".": self.settings.decimal_sep})
        )
        return formatted

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or index.row() >= self.rowCount():
            return None
        col = index.column()

        # Phantom entry row
        if self._is_phantom_row(index.row()):
            if role == Qt.ItemDataRole.DisplayRole:
                if col == COL_DATE:
                    return self._phantom_date()
                return ""
            if role == Qt.ItemDataRole.ForegroundRole:
                return QColor(160, 160, 160)
            if role == Qt.ItemDataRole.EditRole:
                if col == COL_DESC:
                    return ""
            return None

        row = self._rows[index.row()]

        if role == Qt.ItemDataRole.DisplayRole:
            if col == COL_ID:
                return str(row.get("ID", ""))
            elif col == COL_DATE:
                return self._format_date(row.get("Date", ""))
            elif col == COL_DESC:
                return row.get("Description") or ""
            elif col == COL_AMOUNT:
                amt = row.get("Amount") if "Amount" in row else row.get("TotalAmount")
                denom = row.get("Denominator", 100)
                return self._format_amt(amt, denom)
            elif col == COL_BALANCE:
                bal = row.get("Balance")
                denom = row.get("Denominator", 100)
                return self._format_amt(bal, denom)
            elif col == COL_CURRENCY:
                return row.get("CurrencyCode", "")

        elif role == Qt.ItemDataRole.EditRole:
            if col == COL_DATE:
                return row.get("Date", "")
            elif col == COL_DESC:
                return row.get("Description") or ""

        elif role == Qt.ItemDataRole.TextAlignmentRole:
            if col in (COL_AMOUNT, COL_BALANCE):
                return int(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        elif role == Qt.ItemDataRole.UserRole:
            if col == COL_ID:
                return row.get("ID")

        return None

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        base = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
        if self._is_phantom_row(index.row()):
            if index.column() == COL_DESC:
                return base | Qt.ItemFlag.ItemIsEditable
            return base
        if index.column() in (COL_DATE, COL_DESC):
            return base | Qt.ItemFlag.ItemIsEditable
        return base

    def setData(self, index: QModelIndex, value, role: int = Qt.ItemDataRole.EditRole) -> bool:
        if not index.isValid() or role != Qt.ItemDataRole.EditRole:
            return False
        if self._is_phantom_row(index.row()) and index.column() == COL_DESC:
            desc = str(value).strip()
            if desc:
                now_utc = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
                QTimer.singleShot(0, lambda d=desc, t=now_utc: self.new_transaction_requested.emit(d, t))
            return True
        row = index.row()
        if 0 <= row < len(self._rows):
            col = index.column()
            if col == COL_DATE:
                new_date = str(value)
                trans_id = self._rows[row].get("ID")

                # Keep all rows for the same transaction in sync (detailed mode has
                # multiple rows per transaction).
                for r in self._all_rows:
                    if r.get("ID") == trans_id:
                        r["Date"] = new_date

                changed_rows = [i for i, r in enumerate(self._rows) if r.get("ID") == trans_id]
                for changed_row in changed_rows:
                    changed_idx = self.index(changed_row, COL_DATE)
                    self.dataChanged.emit(changed_idx, changed_idx, [role])
                return True
            elif col == COL_DESC:
                new_desc = str(value)
                trans_id = self._rows[row].get("ID")

                # Keep all rows for the same transaction in sync (applies to
                # detailed and aggregated modes when one transaction spans rows).
                for r in self._all_rows:
                    if r.get("ID") == trans_id:
                        r["Description"] = new_desc

                changed_rows = [i for i, r in enumerate(self._rows) if r.get("ID") == trans_id]
                for changed_row in changed_rows:
                    changed_idx = self.index(changed_row, COL_DESC)
                    self.dataChanged.emit(changed_idx, changed_idx, [role])
                return True
        return False

    def get_trans_id(self, row: int) -> int | None:
        if 0 <= row < len(self._rows):
            return self._rows[row].get("ID")
        return None  # phantom row or out of bounds

    def find_row_for_trans(self, trans_id: int) -> int:
        for i, row in enumerate(self._rows):
            if row.get("ID") == trans_id:
                return i
        return -1


    def sort(self, column: int, order: Qt.SortOrder = Qt.SortOrder.AscendingOrder) -> None:
        """Sort rows by selected column; keep phantom entry row at the end."""
        reverse = order == Qt.SortOrder.DescendingOrder

        def key(row: dict):
            if column == COL_ID:
                return row.get("ID") or 0
            if column == COL_DATE:
                return row.get("Date") or ""
            if column == COL_DESC:
                return (row.get("Description") or "").lower()
            if column == COL_AMOUNT:
                return row.get("Amount") if "Amount" in row else (row.get("TotalAmount") or 0)
            if column == COL_BALANCE:
                return row.get("Balance") or 0
            if column == COL_CURRENCY:
                return (row.get("CurrencyCode") or "").lower()
            return 0

        self.layoutAboutToBeChanged.emit()
        self._all_rows.sort(key=key, reverse=reverse)
        loaded = len(self._rows)
        self._rows = self._all_rows[:loaded]
        self.layoutChanged.emit()

    def set_filter(self, filter_text: str = "") -> None:
        """Placeholder for future filtering support."""
        pass
