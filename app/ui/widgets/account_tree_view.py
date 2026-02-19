"""Account tree view with context menu and drag-and-drop."""
from PyQt6.QtWidgets import (
    QTreeView, QMenu, QMessageBox
)
from PyQt6.QtCore import Qt, pyqtSignal, QModelIndex
from PyQt6.QtGui import QAction
from app.i18n import tr
from app.ui.item_models.account_tree_model import AccountTreeModel, VIRTUAL_IMBALANCE_ID, VIRTUAL_EMPTY_ID
from app.repositories.account_repo import AccountRepo
from app.repositories.transaction_repo import TransactionRepo
from app.repositories.split_repo import SplitRepo
from app.services.balance_service import BalanceService
from app.ui.dialogs.delete_account_dialog import DeleteAccountDialog


class AccountTreeView(QTreeView):
    """Tree view for accounts with context menu actions."""

    account_selected = pyqtSignal(list)  # list of account IDs
    virtual_node_selected = pyqtSignal(int)  # virtual node ID

    def __init__(self, account_repo: AccountRepo, trans_repo: TransactionRepo,
                 split_repo: SplitRepo, balance_service: BalanceService,
                 settings, parent=None):
        super().__init__(parent)
        self.account_repo = account_repo
        self.trans_repo = trans_repo
        self.split_repo = split_repo
        self.balance_service = balance_service
        self.settings = settings

        self.setSelectionMode(QTreeView.SelectionMode.ExtendedSelection)
        self.setDragDropMode(QTreeView.DragDropMode.InternalMove)
        self.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_context_menu)
        self.clicked.connect(self._on_clicked)

    def setModel(self, model):
        super().setModel(model)
        if model is not None:
            self.selectionModel().selectionChanged.connect(self._on_selection_changed)

    def _on_clicked(self, index: QModelIndex):
        model: AccountTreeModel = self.model()
        node = model.get_node(index)
        if node is None:
            return

        if node.is_virtual:
            self.virtual_node_selected.emit(node.virtual_id)
            return

        acc = node.account
        if acc is None:
            return

        modifiers = self.window().QApplication.keyboardModifiers() if hasattr(self.window(), 'QApplication') else Qt.KeyboardModifier.NoModifier
        from PyQt6.QtWidgets import QApplication
        modifiers = QApplication.keyboardModifiers()

        if modifiers & Qt.KeyboardModifier.ControlModifier:
            # Multi-select: add to current selection, emit all selected
            self._on_selection_changed()
            return

        # GRP click -> select all descendants
        if acc.status == "GRP":
            ids = [acc.id] + model.get_all_descendants(acc.id, self.settings.show_hidden_accounts)
            self.account_selected.emit(ids)
            return

        self.account_selected.emit([acc.id])

    def _on_selection_changed(self):
        model: AccountTreeModel = self.model()
        if model is None:
            return
        selected_ids = []
        for index in self.selectedIndexes():
            if index.column() != 0:
                continue
            node = model.get_node(index)
            if node and node.account and not node.is_virtual:
                selected_ids.append(node.account.id)
        if selected_ids:
            self.account_selected.emit(selected_ids)

    def _show_context_menu(self, pos):
        index = self.indexAt(pos)
        model: AccountTreeModel = self.model()
        menu = QMenu(self)

        # Add account
        add_action = QAction(tr("&Add Account"), self)
        add_action.triggered.connect(lambda: self._add_account(index if index.isValid() else QModelIndex()))
        menu.addAction(add_action)

        if index.isValid():
            node = model.get_node(index)
            if node and not node.is_virtual and node.account:
                menu.addSeparator()
                del_action = QAction(tr("&Delete Account"), self)
                del_action.triggered.connect(lambda: self._delete_account(index))
                menu.addAction(del_action)

        menu.exec(self.viewport().mapToGlobal(pos))

    def _add_account(self, parent_index: QModelIndex):
        model: AccountTreeModel = self.model()
        parent_id = None
        if parent_index.isValid():
            node = model.get_node(parent_index)
            if node and node.account:
                parent_id = node.account.id

        new_id = self.account_repo.insert(parent_id, tr("New Account"), None, None, None, "ACT")
        self.balance_service.clear()
        model.reload()
        self.expandAll()

        # Start inline rename on the newly created account
        new_index = model.get_index_for_account(new_id)
        if new_index.isValid():
            self.scrollTo(new_index)
            self.edit(new_index)

    def _delete_account(self, index: QModelIndex):
        model: AccountTreeModel = self.model()
        node = model.get_node(index)
        if node is None or node.account is None:
            return
        acc = node.account

        dlg = DeleteAccountDialog(acc.name, self.account_repo, acc.id, self)
        if dlg.exec() != DeleteAccountDialog.DialogCode.Accepted:
            return

        action = dlg.action
        if action == DeleteAccountDialog.HIDE:
            self.account_repo.update_status(acc.id, "HID")
        elif action == DeleteAccountDialog.MOVE:
            target = dlg.target_account_id
            if target:
                self.account_repo.move_splits_to_account(acc.id, target)
                self.account_repo.update_status(acc.id, "HID")
        elif action == DeleteAccountDialog.DELETE_SPLITS:
            self.split_repo.delete_by_account(acc.id)
            self.account_repo.update_status(acc.id, "HID")
        elif action == DeleteAccountDialog.DELETE_TRANS:
            trans_ids = self.account_repo.get_transaction_ids_for_account(acc.id)
            for tid in trans_ids:
                self.trans_repo.delete(tid)
            self.account_repo.update_status(acc.id, "HID")

        self.balance_service.clear()
        model.reload()
        self.expandAll()

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-chaoscash-account"):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat("application/x-chaoscash-account"):
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        """Handle DnD with cycle detection."""
        if not event.mimeData().hasFormat("application/x-chaoscash-account"):
            event.ignore()
            return
        target_index = self.indexAt(event.position().toPoint())
        model: AccountTreeModel = self.model()

        dragged_indexes = self.selectedIndexes()
        dragged_ids = set()
        for idx in dragged_indexes:
            if idx.column() == 0:
                node = model.get_node(idx)
                if node and node.account:
                    dragged_ids.add(node.account.id)

        if target_index.isValid():
            target_node = model.get_node(target_index)
            target_id = target_node.account.id if (target_node and target_node.account) else None
        else:
            target_id = None

        for moved_id in dragged_ids:
            if self._would_create_cycle(moved_id, target_id, model):
                from PyQt6.QtWidgets import QMessageBox
                QMessageBox.warning(self, tr("Invalid Move"),
                                    tr("Cannot move an account into itself or its descendants."))
                event.ignore()
                return

        for moved_id in dragged_ids:
            self.account_repo.update_parent(moved_id, target_id)

        self.balance_service.clear()
        model.reload()
        self.expandAll()
        event.accept()

    def _would_create_cycle(self, moved_id: int, new_parent_id: int | None,
                             model: AccountTreeModel) -> bool:
        if new_parent_id is None:
            return False
        if moved_id == new_parent_id:
            return True
        current = new_parent_id
        while current is not None:
            if current == moved_id:
                return True
            current = self.account_repo.get_parent_id(current)
        return False
