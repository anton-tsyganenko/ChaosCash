"""QAbstractTableModel for splits of the selected transaction."""
from __future__ import annotations

from dataclasses import replace
import logging
import math

from PyQt6.QtCore import Qt, QModelIndex, QAbstractTableModel
from PyQt6.QtGui import QColor

from app.repositories.split_repo import SplitRepo
from app.repositories.account_repo import AccountRepo
from app.repositories.currency_repo import CurrencyRepo
from app.models.split import Split
from app.utils.amount_math import format_amount, float_to_quants
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
    __slots__ = (
        "split",
        "row_type",
        "phantom_currency_id",
        "phantom_amount",
        "account_id",
        "currency_id",
        "amount_text",
    )

    def __init__(
        self,
        split: Split | None,
        row_type: str = ROW_REAL,
        phantom_currency_id: int | None = None,
        phantom_amount: int = 0,
    ):
        self.split = split
        self.row_type = row_type
        self.phantom_currency_id = phantom_currency_id
        self.phantom_amount = phantom_amount
        self.account_id = split.account if split else None
        self.currency_id = split.currency if split else phantom_currency_id
        self.amount_text = ""


class SplitModel(QAbstractTableModel):
    """Displays splits for the selected transaction, including helper rows."""

    def __init__(
        self,
        split_repo: SplitRepo,
        account_repo: AccountRepo,
        currency_repo: CurrencyRepo,
        settings,
        parent=None,
    ):
        super().__init__(parent)
        self.split_repo = split_repo
        self.account_repo = account_repo
        self.currency_repo = currency_repo
        self.settings = settings
        self._logger = logging.getLogger("chaoscash.ui.model.split")

        self._rows: list[SplitRow] = []
        self._trans_id: int | None = None
        self._accounts: dict[int, object] = {}
        self._currencies: dict[int, object] = {}
        self._zero_split_ids: set[int] = set()

    def load(self, trans_id: int | None) -> None:
        self._logger.debug("load trans_id=%r", trans_id)
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
        self._logger.debug("set_zero_split_ids count=%s", len(ids))
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

    @staticmethod
    def _enum_value(value) -> object:
        return getattr(value, "value", value)

    @staticmethod
    def _to_checkstate(value) -> Qt.CheckState | None:
        """Normalize Qt checkbox payload from model/view.

        Qt sends CheckStateRole data through QVariant; in PyQt it often arrives as
        plain int (0/1/2) rather than Qt.CheckState enum. This conversion follows
        Qt semantics instead of assuming a Python enum instance.
        """
        try:
            return Qt.CheckState(int(value))
        except (TypeError, ValueError):
            return None

    def headerData(
        self,
        section: int,
        orientation: Qt.Orientation,
        role: int = Qt.ItemDataRole.DisplayRole,
    ):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return [
                tr("ID"),
                tr("Ext. ID"),
                tr("Description"),
                tr("Account"),
                tr("Fixed"),
                tr("Amount"),
                tr("Currency"),
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
            quants,
            cur.denominator,
            self.settings.decimal_sep,
            self.settings.thousands_sep,
        )

    def _edit_amt(self, quants: int, currency_id: int | None) -> str:
        """Return raw editable amount in units (no thousands separators)."""
        if currency_id is None:
            return str(quants)
        cur = self._currencies.get(currency_id)
        denom = cur.denominator if cur and cur.denominator > 0 else 1
        decimal_places = max(0, math.ceil(math.log10(denom))) if denom > 1 else 0
        value = quants / denom
        return f"{value:.{decimal_places}f}"

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole):
        if not index.isValid() or index.row() >= len(self._rows):
            return None

        row_obj = self._rows[index.row()]
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if row_obj.row_type == ROW_PHANTOM:
                if col == COL_AMOUNT:
                    return self._format_amt(row_obj.phantom_amount, row_obj.phantom_currency_id)
                if col == COL_CURRENCY:
                    return self._currency_code(row_obj.phantom_currency_id)
                if col == COL_ACCOUNT:
                    return self._account_name(row_obj.account_id)
                if col == COL_DESC:
                    return tr("(imbalanced — select account)")
                return ""

            if row_obj.row_type == ROW_NEW:
                if col == COL_ACCOUNT:
                    return self._account_name(row_obj.account_id)
                if col == COL_AMOUNT:
                    return row_obj.amount_text
                if col == COL_CURRENCY:
                    return self._currency_code(row_obj.currency_id)
                if col == COL_DESC:
                    return tr("(new split — fill account, amount, currency)")
                return ""

            s = row_obj.split
            if s is None:
                return None
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
                    # EditRole must be raw editable value, without UI formatting.
                    return self._edit_amt(s.amount, s.currency)
            if row_obj.row_type == ROW_NEW and col == COL_AMOUNT:
                return row_obj.amount_text
            return None

        if role == Qt.ItemDataRole.CheckStateRole:
            if col == COL_FIXED and row_obj.row_type == ROW_REAL and row_obj.split:
                return (
                    Qt.CheckState.Checked
                    if row_obj.split.amount_fixed
                    else Qt.CheckState.Unchecked
                )

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
            if row_obj.row_type in (ROW_PHANTOM, ROW_NEW):
                if col == COL_ACCOUNT:
                    return row_obj.account_id
                if col == COL_CURRENCY:
                    return row_obj.currency_id
            return None

        if role == Qt.ItemDataRole.ForegroundRole:
            if row_obj.row_type in (ROW_PHANTOM, ROW_NEW):
                return QColor(140, 140, 140)

        if role == Qt.ItemDataRole.BackgroundRole:
            if row_obj.row_type == ROW_PHANTOM:
                return QColor(255, 230, 180)
            if row_obj.row_type == ROW_NEW:
                return QColor(230, 240, 255)
            if (
                row_obj.row_type == ROW_REAL
                and row_obj.split
                and row_obj.split.id in self._zero_split_ids
            ):
                return QColor(255, 255, 180)

        return None

    def setData(
        self,
        index: QModelIndex,
        value,
        role: int = Qt.ItemDataRole.EditRole,
    ) -> bool:
        self._logger.debug(
            "setData row=%s col=%s role=%s value=%r valid=%s",
            index.row() if index.isValid() else -1,
            index.column() if index.isValid() else -1,
            self._enum_value(role),
            value,
            index.isValid(),
        )
        if not index.isValid() or index.row() >= len(self._rows):
            return False

        if not (self.flags(index) & (Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsUserCheckable)):
            return False

        row_obj = self._rows[index.row()]
        col = index.column()
        changed = False
        changed_roles: list[Qt.ItemDataRole] = []

        if row_obj.row_type == ROW_REAL and row_obj.split is not None:
            split = row_obj.split
            if col == COL_FIXED and role == Qt.ItemDataRole.CheckStateRole:
                state = self._to_checkstate(value)
                if state is None:
                    self._logger.debug(
                        "setData invalid checkstate row=%s col=%s value=%r type=%s",
                        index.row(),
                        col,
                        value,
                        type(value).__name__,
                    )
                    return False
                new_fixed = state == Qt.CheckState.Checked
                if new_fixed != split.amount_fixed:
                    row_obj.split = replace(split, amount_fixed=new_fixed)
                    changed = True
                    changed_roles = [Qt.ItemDataRole.CheckStateRole]

            elif col == COL_EXTID and role in (Qt.ItemDataRole.EditRole, Qt.ItemDataRole.DisplayRole):
                new_ext_id = str(value).strip() or None
                if new_ext_id != split.external_id:
                    row_obj.split = replace(split, external_id=new_ext_id)
                    changed = True
                    changed_roles = [Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole]

            elif col == COL_DESC and role in (Qt.ItemDataRole.EditRole, Qt.ItemDataRole.DisplayRole):
                new_desc = str(value).strip() or None
                if new_desc != split.description:
                    row_obj.split = replace(split, description=new_desc)
                    changed = True
                    changed_roles = [Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole]

            elif col == COL_ACCOUNT and role == Qt.ItemDataRole.UserRole:
                try:
                    new_account = int(value) if value is not None else None
                except (TypeError, ValueError):
                    return False
                if new_account is not None and new_account != split.account:
                    row_obj.split = replace(split, account=new_account)
                    changed = True
                    changed_roles = [Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.UserRole]

            elif col == COL_CURRENCY and role == Qt.ItemDataRole.UserRole:
                try:
                    new_currency = int(value) if value is not None else None
                except (TypeError, ValueError):
                    return False
                if new_currency is not None and new_currency != split.currency:
                    row_obj.split = replace(split, currency=new_currency)
                    changed = True
                    changed_roles = [Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.UserRole]

            elif col == COL_AMOUNT and role in (Qt.ItemDataRole.EditRole, Qt.ItemDataRole.DisplayRole):
                try:
                    value_float = float(str(value).strip())
                except (TypeError, ValueError):
                    return False
                currency_id = split.currency
                cur = self._currencies.get(currency_id)
                denom = cur.denominator if cur else 100
                new_amount = float_to_quants(value_float, denom)
                if new_amount != split.amount:
                    row_obj.split = replace(split, amount=new_amount)
                    changed = True
                    changed_roles = [Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole]

        elif row_obj.row_type in (ROW_PHANTOM, ROW_NEW):
            if col == COL_ACCOUNT and role == Qt.ItemDataRole.UserRole:
                try:
                    new_account = int(value) if value is not None else None
                except (TypeError, ValueError):
                    return False
                if new_account != row_obj.account_id:
                    row_obj.account_id = new_account
                    changed = True
                    changed_roles = [Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.UserRole]

            elif row_obj.row_type == ROW_NEW and col == COL_CURRENCY and role == Qt.ItemDataRole.UserRole:
                try:
                    new_currency = int(value) if value is not None else None
                except (TypeError, ValueError):
                    return False
                if new_currency != row_obj.currency_id:
                    row_obj.currency_id = new_currency
                    changed = True
                    changed_roles = [Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.UserRole]

            elif row_obj.row_type == ROW_NEW and col == COL_AMOUNT and role in (
                Qt.ItemDataRole.EditRole,
                Qt.ItemDataRole.DisplayRole,
                Qt.ItemDataRole.UserRole,
            ):
                new_amount_text = str(value).strip()
                if new_amount_text != row_obj.amount_text:
                    row_obj.amount_text = new_amount_text
                    changed = True
                    changed_roles = [
                        Qt.ItemDataRole.DisplayRole,
                        Qt.ItemDataRole.EditRole,
                        Qt.ItemDataRole.UserRole,
                    ]

        if not changed:
            self._logger.debug(
                "setData no changes applied row=%s col=%s role=%s",
                index.row(),
                col,
                self._enum_value(role),
            )
            return False

        self._logger.debug(
            "setData changed row=%s col=%s roles=%s",
            index.row(),
            col,
            [self._enum_value(r) for r in changed_roles],
        )
        self.dataChanged.emit(index, index, changed_roles)
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
        self._logger.debug("sort column=%s order=%s", column, self._enum_value(order))
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
        self.layoutChanged.emit()

    def set_filter(self, filter_text: str = "") -> None:
        """Placeholder for future filtering support."""
        self._logger.debug("set_filter filter_text=%r", filter_text)
        pass
