"""QAbstractItemModel for the account hierarchy tree."""
from __future__ import annotations

from PyQt6.QtCore import QAbstractItemModel, QModelIndex, Qt
from PyQt6.QtGui import QColor

from app.i18n import tr
from app.models.account import Account
from app.repositories.account_repo import AccountRepo
from app.repositories.currency_repo import CurrencyRepo
from app.services.amount_formatter import AmountFormatter
from app.services.balance_service import BalanceService
from app.utils.account_hierarchy import compute_hidden_account_ids

COL_NAME = 0
COL_TOTAL_BALANCE = 1
COL_OWN_BALANCE = 2
COL_HIDDEN = 3
COL_CODE = 4
COL_EXTERNAL_ID = 5
COL_DESCRIPTION = 6
NUM_COLS = 7

VIRTUAL_IMBALANCE_ID = -1
VIRTUAL_EMPTY_ID = -2


class AccountNode:
    __slots__ = ("account", "parent_node", "children", "virtual_id")

    def __init__(self, account: Account | None, parent_node: "AccountNode | None",
                 virtual_id: int | None = None):
        self.account = account
        self.parent_node = parent_node
        self.children: list[AccountNode] = []
        self.virtual_id = virtual_id

    @property
    def is_virtual(self) -> bool:
        return self.virtual_id is not None


class AccountTreeModel(QAbstractItemModel):
    """Hierarchical model of accounts with optional virtual nodes."""

    def __init__(self, account_repo: AccountRepo, balance_service: BalanceService,
                 currency_repo: CurrencyRepo, settings, formatter: AmountFormatter,
                 integrity_service, parent=None):
        super().__init__(parent)
        self.account_repo = account_repo
        self.balance_service = balance_service
        self.currency_repo = currency_repo
        self.settings = settings
        self.formatter = formatter
        self.integrity_service = integrity_service

        self._root = AccountNode(None, None)
        self._id_to_node: dict[int, AccountNode] = {}
        self._show_imbalance = False
        self._show_empty = False
        self._currencies: dict[int, object] = {}
        self.reload()

    def reload(self) -> None:
        self.beginResetModel()
        self._root = AccountNode(None, None)
        self._id_to_node = {}
        self._currencies = {c.id: c for c in self.currency_repo.get_all()}
        self._build_tree()
        self._add_virtual_nodes()
        self.endResetModel()

    def _build_tree(self) -> None:
        all_accounts = self.account_repo.get_all()
        nodes: dict[int, AccountNode] = {acc.id: AccountNode(acc, None) for acc in all_accounts}

        if not self.settings.show_hidden_accounts:
            hidden_ids = compute_hidden_account_ids(all_accounts)
            nodes = {aid: n for aid, n in nodes.items() if aid not in hidden_ids}

        for node in nodes.values():
            acc = node.account
            if acc.parent is None or acc.parent not in nodes:
                node.parent_node = self._root
                self._root.children.append(node)
            else:
                parent_node = nodes[acc.parent]
                node.parent_node = parent_node
                parent_node.children.append(node)

        self._id_to_node = nodes

        def sort_recursive(parent: AccountNode):
            parent.children.sort(key=lambda n: (n.account.name or "").lower())
            for child in parent.children:
                sort_recursive(child)

        sort_recursive(self._root)

    def _add_virtual_nodes(self) -> None:
        if self._show_imbalance:
            node = AccountNode(None, self._root, VIRTUAL_IMBALANCE_ID)
            node.account = _make_virtual_account(VIRTUAL_IMBALANCE_ID, tr("Imbalance"))
            self._root.children.append(node)
        if self._show_empty:
            node = AccountNode(None, self._root, VIRTUAL_EMPTY_ID)
            node.account = _make_virtual_account(VIRTUAL_EMPTY_ID, tr("Empty Transactions"))
            self._root.children.append(node)

    def set_virtual_nodes(self, has_imbalance: bool, has_empty: bool) -> None:
        changed = (self._show_imbalance != has_imbalance or self._show_empty != has_empty)
        self._show_imbalance = has_imbalance
        self._show_empty = has_empty
        if changed:
            self.reload()

    def get_node(self, index: QModelIndex) -> AccountNode | None:
        if not index.isValid():
            return None
        return index.internalPointer()

    def rowCount(self, parent: QModelIndex = QModelIndex()) -> int:
        if parent.column() > 0:
            return 0
        parent_node = self._root if not parent.isValid() else parent.internalPointer()
        return len(parent_node.children)

    def columnCount(self, parent: QModelIndex = QModelIndex()) -> int:
        return NUM_COLS

    def index(self, row: int, col: int, parent: QModelIndex = QModelIndex()) -> QModelIndex:
        if not self.hasIndex(row, col, parent):
            return QModelIndex()
        parent_node = self._root if not parent.isValid() else parent.internalPointer()
        if row < len(parent_node.children):
            return self.createIndex(row, col, parent_node.children[row])
        return QModelIndex()

    def parent(self, index: QModelIndex) -> QModelIndex:
        if not index.isValid():
            return QModelIndex()
        node: AccountNode = index.internalPointer()
        parent_node = node.parent_node
        if parent_node is None or parent_node is self._root:
            return QModelIndex()
        grand = parent_node.parent_node
        if grand is None:
            return QModelIndex()
        return self.createIndex(grand.children.index(parent_node), 0, parent_node)

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        node: AccountNode = index.internalPointer()
        acc = node.account
        if acc is None:
            return None
        col = index.column()

        if role in (Qt.ItemDataRole.DisplayRole, Qt.ItemDataRole.EditRole):
            if col == COL_NAME:
                return acc.name
            if col == COL_CODE:
                return acc.code or ""
            if col == COL_EXTERNAL_ID:
                return acc.external_id or ""
            if col == COL_DESCRIPTION:
                return acc.description or ""
            if col == COL_TOTAL_BALANCE:
                if role == Qt.ItemDataRole.EditRole:
                    return None if node.is_virtual else None
                if node.is_virtual and acc.id != VIRTUAL_IMBALANCE_ID:
                    return ""
                return self._format_balance(acc.id, include_children=True)
            if col == COL_OWN_BALANCE:
                if role == Qt.ItemDataRole.EditRole:
                    return None if node.is_virtual else None
                if node.is_virtual and acc.id != VIRTUAL_IMBALANCE_ID:
                    return ""
                return self._format_balance(acc.id, include_children=False)
            return None

        if role == Qt.ItemDataRole.CheckStateRole and col == COL_HIDDEN and not node.is_virtual:
            return Qt.CheckState.Checked if acc.is_hidden else Qt.CheckState.Unchecked

        if role == Qt.ItemDataRole.UserRole:
            return acc.id if not node.is_virtual else node.virtual_id

        if role == Qt.ItemDataRole.ForegroundRole and acc.is_hidden:
            return QColor(150, 150, 150)
        return None

    def _format_balance(self, account_id: int, include_children: bool) -> str:
        if account_id == VIRTUAL_IMBALANCE_ID:
            balance = self.integrity_service.get_total_imbalance()
        elif account_id < 0:
            return ""
        else:
            balance = self.balance_service.get_balance(account_id, include_children=include_children)
        parts = []
        for cid, quants in balance.items():
            if quants == 0:
                continue
            parts.append(self.formatter.format_with_currency(quants, cid))
        return ", ".join(parts)

    def headerData(self, section: int, orientation: Qt.Orientation,
                   role: int = Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return [
                tr("Account"), tr("Total Balance"), tr("Own Balance"), tr("Hidden"),
                tr("Code"), tr("Ext. ID"), tr("Description"),
            ][section]
        return None

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        if not index.isValid():
            return Qt.ItemFlag.ItemIsDropEnabled
        node: AccountNode = index.internalPointer()
        base = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
        if not node.is_virtual:
            base |= Qt.ItemFlag.ItemIsDragEnabled | Qt.ItemFlag.ItemIsDropEnabled
            if index.column() in (COL_NAME, COL_CODE, COL_EXTERNAL_ID, COL_DESCRIPTION):
                base |= Qt.ItemFlag.ItemIsEditable
            if index.column() == COL_HIDDEN:
                base |= Qt.ItemFlag.ItemIsUserCheckable
        return base

    def setData(self, index: QModelIndex, value, role: int = Qt.ItemDataRole.EditRole) -> bool:
        if not index.isValid():
            return False
        node: AccountNode = index.internalPointer()
        if node.is_virtual:
            return False
        acc = node.account
        col = index.column()

        if col == COL_HIDDEN and role == Qt.ItemDataRole.CheckStateRole:
            raw_value = getattr(value, "value", value)
            is_hidden = int(raw_value) == int(Qt.CheckState.Checked.value)
            if bool(acc.is_hidden) == is_hidden:
                return False
            self.account_repo.update_hidden(acc.id, is_hidden)
            updated = self.account_repo.get_by_id(acc.id)
            if updated:
                node.account = updated
                self._id_to_node[acc.id] = node
            if not self.settings.show_hidden_accounts and is_hidden:
                self._remove_node_subtree(node)
                return True
            self.dataChanged.emit(index, index, [role])
            return True

        if role != Qt.ItemDataRole.EditRole:
            return False

        name = acc.name
        code = acc.code
        desc = acc.description
        ext = acc.external_id

        if col == COL_NAME:
            new_name = str(value).strip()
            if not new_name:
                return False
            name = new_name
        elif col == COL_CODE:
            code = str(value).strip() or None
        elif col == COL_EXTERNAL_ID:
            ext = str(value).strip() or None
        elif col == COL_DESCRIPTION:
            desc = str(value).strip() or None
        else:
            return False

        self.account_repo.update(acc.id, acc.parent, name, code, desc, ext, acc.is_hidden)
        updated = self.account_repo.get_by_id(acc.id)
        if updated:
            node.account = updated
            self._id_to_node[acc.id] = node
        self.dataChanged.emit(index, index, [role])
        return True

    def _node_parent_index(self, node: AccountNode) -> QModelIndex:
        parent_node = node.parent_node
        if parent_node is None or parent_node is self._root:
            return QModelIndex()
        grand = parent_node.parent_node
        if grand is None:
            return QModelIndex()
        row = grand.children.index(parent_node)
        return self.createIndex(row, 0, parent_node)

    def _remove_node_subtree(self, node: AccountNode) -> None:
        parent_node = node.parent_node
        if parent_node is None:
            return
        row = parent_node.children.index(node)
        parent_index = self._node_parent_index(node)
        self.beginRemoveRows(parent_index, row, row)
        parent_node.children.pop(row)
        self._remove_node_ids_recursive(node)
        self.endRemoveRows()

    def _remove_node_ids_recursive(self, node: AccountNode) -> None:
        if node.account and not node.is_virtual:
            self._id_to_node.pop(node.account.id, None)
        for child in node.children:
            self._remove_node_ids_recursive(child)

    def supportedDropActions(self):
        return Qt.DropAction.MoveAction

    def mimeTypes(self) -> list[str]:
        return ["application/x-chaoscash-account"]

    def mimeData(self, indexes):
        from PyQt6.QtCore import QByteArray, QMimeData
        ids = []
        for idx in indexes:
            if idx.column() == 0 and idx.isValid():
                node = self.get_node(idx)
                if node and node.account and not node.is_virtual:
                    ids.append(str(node.account.id))
        mime = QMimeData()
        mime.setData("application/x-chaoscash-account", QByteArray(",".join(ids).encode()))
        return mime

    def dropMimeData(self, data, action, row, col, parent) -> bool:
        return False

    def sort(self, column: int, order: Qt.SortOrder = Qt.SortOrder.AscendingOrder) -> None:
        reverse = order == Qt.SortOrder.DescendingOrder

        def sort_key(n: AccountNode):
            a = n.account
            if a is None:
                return ""
            if column == COL_NAME:
                return (a.name or "").lower()
            if column == COL_TOTAL_BALANCE:
                return sum(self.balance_service.get_balance(a.id, include_children=True).values())
            if column == COL_OWN_BALANCE:
                return sum(self.balance_service.get_balance(a.id, include_children=False).values())
            if column == COL_HIDDEN:
                return int(a.is_hidden)
            if column == COL_CODE:
                return (a.code or "").lower()
            if column == COL_EXTERNAL_ID:
                return (a.external_id or "").lower()
            if column == COL_DESCRIPTION:
                return (a.description or "").lower()
            return (a.name or "").lower()

        def sort_recursive(node: AccountNode):
            node.children.sort(key=sort_key, reverse=reverse)
            for child in node.children:
                sort_recursive(child)

        self.layoutAboutToBeChanged.emit()
        sort_recursive(self._root)
        self.layoutChanged.emit()

    def get_index_for_account(self, account_id: int) -> QModelIndex:
        node = self._id_to_node.get(account_id)
        if node is None or node.parent_node is None:
            return QModelIndex()
        row = node.parent_node.children.index(node)
        return self.createIndex(row, 0, node)

    def get_all_descendants(self, account_id: int, include_hidden: bool) -> list[int]:
        result = []
        node = self._id_to_node.get(account_id)
        if node is None:
            return result
        for child in node.children:
            if child.account and child.account.is_hidden and not include_hidden:
                continue
            if child.account:
                result.append(child.account.id)
                result.extend(self.get_all_descendants(child.account.id, include_hidden))
        return result


def _make_virtual_account(virtual_id: int, name: str) -> Account:
    return Account(id=virtual_id, parent=None, name=name, code=None,
                   description=None, external_id=None, is_hidden=False)
