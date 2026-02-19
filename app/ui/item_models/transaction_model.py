"""QAbstractTableModel for the transaction list with running balance."""
from __future__ import annotations
from PyQt6.QtCore import Qt, QModelIndex, QAbstractTableModel
from app.repositories.transaction_repo import TransactionRepo
from app.repositories.currency_repo import CurrencyRepo
from app.utils.amount_math import format_amount
from app.i18n import tr
from datetime import datetime, timezone, tzinfo as TZInfo
import zoneinfo

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
    Supports verbose (per-split) and summary (per-transaction) modes.
    Implements canFetchMore/fetchMore for lazy loading.
    """

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
        self._local_tz: TZInfo | None = None

    def load(self, account_ids: list[int]) -> None:
        self.beginResetModel()
        self._account_ids = account_ids
        self._currencies = {c.id: c for c in self.currency_repo.get_all()}
        try:
            import datetime as dt
            self._local_tz = dt.datetime.now().astimezone().tzinfo
        except Exception:
            self._local_tz = UTC

        if not account_ids:
            self._all_rows = []
            self._rows = []
            self.endResetModel()
            return

        mode = self.settings.transaction_view_mode
        if mode == "verbose":
            raw = self.trans_repo.get_verbose_by_accounts(account_ids)
        else:
            raw = self.trans_repo.get_summary_by_accounts(account_ids)

        self._all_rows = raw
        self._rows = raw[:FETCH_BLOCK]
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
        return len(self._rows)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return NUM_COLS

    def headerData(self, section: int, orientation: Qt.Orientation,
                   role: int = Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return [tr("ID"), tr("Date"), tr("Description"),
                    tr("Amount"), tr("Balance"), tr("Currency")][section]
        return None

    def _format_date(self, utc_str: str) -> str:
        if not utc_str:
            return ""
        try:
            dt = datetime.strptime(utc_str, "%Y-%m-%d %H:%M:%S").replace(tzinfo=UTC)
            dt_local = dt.astimezone(self._local_tz)
            fmt = self.settings.date_format.replace("yyyy", "%Y").replace("MM", "%m").replace("dd", "%d")
            fmt = fmt.replace("HH", "%H").replace("mm", "%M").replace("ss", "%S")
            return dt_local.strftime(fmt)
        except Exception:
            return utc_str

    def _format_amt(self, quants, denominator) -> str:
        if quants is None:
            return ""
        return format_amount(
            int(quants), int(denominator),
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
            if col == COL_ID:
                return str(row.get("ID", ""))
            elif col == COL_DATE:
                return self._format_date(row.get("Date", ""))
            elif col == COL_DESC:
                return row.get("Description") or ""
            elif col == COL_AMOUNT:
                # verbose uses "Amount", summary uses "TotalAmount"
                amt = row.get("Amount") if "Amount" in row else row.get("TotalAmount")
                denom = row.get("Denominator", 100)
                return self._format_amt(amt, denom)
            elif col == COL_BALANCE:
                bal = row.get("Balance")
                denom = row.get("Denominator", 100)
                return self._format_amt(bal, denom)
            elif col == COL_CURRENCY:
                return row.get("CurrencyCode", "")

        elif role == Qt.ItemDataRole.TextAlignmentRole:
            if col in (COL_AMOUNT, COL_BALANCE):
                return int(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        elif role == Qt.ItemDataRole.UserRole:
            if col == COL_ID:
                return row.get("ID")

        return None

    def get_trans_id(self, row: int) -> int | None:
        if 0 <= row < len(self._rows):
            return self._rows[row].get("ID")
        return None

    def find_row_for_trans(self, trans_id: int) -> int:
        for i, row in enumerate(self._rows):
            if row.get("ID") == trans_id:
                return i
        return -1

    def set_filter(self, filter_text: str = "") -> None:
        """Placeholder for future filtering support."""
        pass
