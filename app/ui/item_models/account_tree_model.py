"""QAbstractItemModel for the account hierarchy tree."""
from __future__ import annotations
from PyQt6.QtCore import Qt, QModelIndex, QAbstractItemModel
from PyQt6.QtGui import QFont
from app.models.account import Account
from app.repositories.account_repo import AccountRepo
from app.services.balance_service import BalanceService
from app.repositories.currency_repo import CurrencyRepo
from app.i18n import tr

COL_NAME = 0
COL_BALANCE = 1
COL_CODE = 2
NUM_COLS = 3

VIRTUAL_IMBALANCE_ID = -1
VIRTUAL_EMPTY_ID = -2


class AccountNode:
    """Tree node wrapping an Account (or virtual node)."""
    __slots__ = ("account", "parent_node", "children", "virtual_id")

    def __init__(self, account: Account | None, parent_node: "AccountNode | None",
                 virtual_id: int | None = None):
        self.account = account
        self.parent_node = parent_node
        self.children: list[AccountNode] = []
        self.virtual_id = virtual_id  # for virtual nodes

    @property
    def is_virtual(self) -> bool:
        return self.virtual_id is not None

    @property
    def account_id(self) -> int | None:
        if self.account:
            return self.account.id
        return None


class AccountTreeModel(QAbstractItemModel):
    """
    Hierarchical model of accounts with optional virtual nodes.
    Columns: Name, Balance, Code
    """

    def __init__(self, account_repo: AccountRepo, balance_service: BalanceService,
                 currency_repo: CurrencyRepo, settings, parent=None):
        super().__init__(parent)
        self.account_repo = account_repo
        self.balance_service = balance_service
        self.currency_repo = currency_repo
        self.settings = settings

        self._root = AccountNode(None, None)
        self._id_to_node: dict[int, AccountNode] = {}
        self._show_imbalance = False
        self._show_empty = False
        self._currencies: dict[int, object] = {}
        self.reload()

    def reload(self) -> None:
        """Rebuild the tree from the database."""
        self.beginResetModel()
        self._root = AccountNode(None, None)
        self._id_to_node = {}
        currencies = self.currency_repo.get_all()
        self._currencies = {c.id: c for c in currencies}
        self._build_tree()
        self._add_virtual_nodes()
        self.endResetModel()

    def _build_tree(self) -> None:
        show_hidden = self.settings.show_hidden_accounts
        all_accounts = self.account_repo.get_all()
        nodes: dict[int, AccountNode] = {}

        for acc in all_accounts:
            if acc.status == "HID" and not show_hidden:
                continue
            node = AccountNode(acc, None)
            nodes[acc.id] = node

        for acc_id, node in nodes.items():
            acc = node.account
            if acc.parent is None or acc.parent not in nodes:
                node.parent_node = self._root
                self._root.children.append(node)
            else:
                parent_node = nodes[acc.parent]
                node.parent_node = parent_node
                parent_node.children.append(node)

        self._id_to_node = nodes

        # Sort children
        sort = self.settings.account_sort
        def sort_key(n: AccountNode):
            a = n.account
            name = (a.name or "").lower()
            code = (a.code or "").lower()
            if sort == "code":
                return (code, name)
            elif sort == "name_code":
                return (name, code)
            elif sort == "code_name":
                return (code, name)
            return (name,)

        def sort_recursive(node: AccountNode):
            node.children.sort(key=sort_key)
            for child in node.children:
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

    def get_account_id(self, index: QModelIndex) -> int | None:
        node = self.get_node(index)
        if node and node.account:
            return node.account.id
        if node and node.virtual_id is not None:
            return node.virtual_id
        return None

    # --- QAbstractItemModel interface ---

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
            child = parent_node.children[row]
            return self.createIndex(row, col, child)
        return QModelIndex()

    def parent(self, index: QModelIndex) -> QModelIndex:
        if not index.isValid():
            return QModelIndex()
        node: AccountNode = index.internalPointer()
        parent_node = node.parent_node
        if parent_node is None or parent_node is self._root:
            return QModelIndex()
        grandparent = parent_node.parent_node
        if grandparent is None:
            return QModelIndex()
        row = grandparent.children.index(parent_node)
        return self.createIndex(row, 0, parent_node)

    def data(self, index: QModelIndex, role: int = Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None
        node: AccountNode = index.internalPointer()
        acc = node.account
        if acc is None:
            return None
        col = index.column()

        if role == Qt.ItemDataRole.DisplayRole:
            if col == COL_NAME:
                return acc.name
            elif col == COL_CODE:
                return acc.code or ""
            elif col == COL_BALANCE:
                if not self.settings.show_balances or node.is_virtual:
                    return ""
                return self._format_balance(acc.id if not node.is_virtual else None)
            return None

        elif role == Qt.ItemDataRole.UserRole:
            return acc.id if not node.is_virtual else node.virtual_id

        elif role == Qt.ItemDataRole.FontRole:
            if acc.status == "GRP":
                font = QFont()
                font.setBold(True)
                return font

        elif role == Qt.ItemDataRole.ForegroundRole:
            from PyQt6.QtGui import QColor
            if acc.status == "HID":
                return QColor(150, 150, 150)

        return None

    def _format_balance(self, account_id: int | None) -> str:
        if account_id is None or account_id < 0:
            return ""
        balance = self.balance_service.get_balance(account_id)
        parts = []
        for cid, quants in balance.items():
            if quants == 0:
                continue
            cur = self._currencies.get(cid)
            if cur is None:
                continue
            from app.utils.amount_math import format_amount
            formatted = format_amount(
                quants, cur.denominator,
                self.settings.decimal_sep,
                self.settings.thousands_sep,
                self.settings.show_thousands,
            )
            parts.append(f"{formatted} {cur.code}")
        return ", ".join(parts)

    def headerData(self, section: int, orientation: Qt.Orientation,
                   role: int = Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return [tr("Account"), tr("Balance"), tr("Code")][section]
        return None

    def flags(self, index: QModelIndex) -> Qt.ItemFlag:
        if not index.isValid():
            return Qt.ItemFlag.ItemIsDropEnabled
        node: AccountNode = index.internalPointer()
        base = Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
        if not node.is_virtual:
            base |= Qt.ItemFlag.ItemIsDragEnabled | Qt.ItemFlag.ItemIsDropEnabled
            if index.column() in (COL_NAME, COL_CODE):
                base |= Qt.ItemFlag.ItemIsEditable
        return base

    def setData(self, index: QModelIndex, value, role: int = Qt.ItemDataRole.EditRole) -> bool:
        if not index.isValid() or role != Qt.ItemDataRole.EditRole:
            return False
        node: AccountNode = index.internalPointer()
        if node.is_virtual:
            return False
        acc = node.account
        col = index.column()
        if col == COL_NAME:
            new_name = str(value).strip()
            if not new_name:
                return False
            self.account_repo.update(
                acc.id, acc.parent, new_name, acc.code,
                acc.description, acc.external_id, acc.status
            )
        elif col == COL_CODE:
            self.account_repo.update(
                acc.id, acc.parent, acc.name, str(value).strip() or None,
                acc.description, acc.external_id, acc.status
            )
        # Refresh node
        updated = self.account_repo.get_by_id(acc.id)
        if updated:
            node.account = updated
            self._id_to_node[acc.id] = node
        self.dataChanged.emit(index, index, [role])
        return True

    def get_node_by_account_id(self, account_id: int) -> AccountNode | None:
        return self._id_to_node.get(account_id)

    def get_index_for_account(self, account_id: int) -> QModelIndex:
        node = self._id_to_node.get(account_id)
        if node is None:
            return QModelIndex()
        parent_node = node.parent_node
        if parent_node is None:
            return QModelIndex()
        row = parent_node.children.index(node)
        return self.createIndex(row, 0, node)

    def get_all_descendants(self, account_id: int, include_hidden: bool) -> list[int]:
        """Return all descendant account IDs recursively."""
        result = []
        node = self._id_to_node.get(account_id)
        if node is None:
            return result
        for child in node.children:
            if child.account and child.account.status == "HID" and not include_hidden:
                continue
            if child.account:
                result.append(child.account.id)
            result.extend(self.get_all_descendants(child.account.id if child.account else -1, include_hidden))
        return result


def _make_virtual_account(virtual_id: int, name: str) -> Account:
    return Account(
        id=virtual_id, parent=None, name=name,
        code=None, description=None, external_id=None, status="GRP"
    )
