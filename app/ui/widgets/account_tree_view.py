"""Account tree view with context menu and drag-and-drop."""
from PyQt6.QtCore import QItemSelectionModel, QMimeData, QModelIndex, Qt, pyqtSignal
from PyQt6.QtGui import (
    QAction, QBrush, QColor, QCursor, QDrag, QFont, QPainter, QPen, QPixmap
)
from PyQt6.QtWidgets import QAbstractItemView, QApplication, QMenu, QTreeView

from app.i18n import tr
from app.repositories.account_repo import AccountRepo
from app.repositories.split_repo import SplitRepo
from app.repositories.transaction_repo import TransactionRepo
from app.services.balance_service import BalanceService
from app.ui.dialogs.delete_account_dialog import DeleteAccountDialog
from app.ui.item_models.account_tree_model import AccountTreeModel
from app.ui.widgets.view_helpers import (
    set_column_visibility,
    show_column_visibility_menu,
)


class AccountTreeView(QTreeView):
    """Tree view for accounts with context menu actions."""

    account_selected = pyqtSignal(list)  # list of account IDs
    virtual_node_selected = pyqtSignal(int)  # virtual node ID
    enter_pressed = pyqtSignal()

    def __init__(self, account_repo: AccountRepo, trans_repo: TransactionRepo,
                 split_repo: SplitRepo, balance_service: BalanceService,
                 settings, parent=None):
        super().__init__(parent)
        self.account_repo = account_repo
        self.trans_repo = trans_repo
        self.split_repo = split_repo
        self.balance_service = balance_service
        self.settings = settings

        # Track the current drop target for visual feedback
        self._current_drop_target: QModelIndex | None = None
        self._drag_in_progress = False

        self.setSelectionMode(QTreeView.SelectionMode.ExtendedSelection)
        self.setDragDropMode(QTreeView.DragDropMode.InternalMove)
        self.setDefaultDropAction(Qt.DropAction.MoveAction)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_context_menu)
        self.clicked.connect(self._on_clicked)

        header = self.header()
        header.setSectionsMovable(True)
        header.setFirstSectionMovable(True)
        header.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        header.customContextMenuRequested.connect(self._show_header_menu)

        self.setSortingEnabled(True)

    def setModel(self, model):
        super().setModel(model)
        if model is not None:
            self.selectionModel().selectionChanged.connect(self._on_selection_changed)


    def keyPressEvent(self, event):
        if self.state() == QAbstractItemView.State.EditingState:
            super().keyPressEvent(event)
            return
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.enter_pressed.emit()
            event.accept()
            return
        super().keyPressEvent(event)

    def moveCursor(self, cursorAction, modifiers):
        if cursorAction == QAbstractItemView.CursorAction.MoveNext:
            idx = self.currentIndex()
            model = self.model()
            if model is not None and idx.isValid():
                row = idx.row()
                col = idx.column()
                parent = idx.parent()
                row_count = model.rowCount(parent)
                col_count = model.columnCount(parent)
                while True:
                    col += 1
                    if col >= col_count:
                        col = 0
                        row += 1
                    if row >= row_count:
                        break
                    cand = model.index(row, col, parent)
                    if model.flags(cand) & Qt.ItemFlag.ItemIsEditable:
                        return cand
        return super().moveCursor(cursorAction, modifiers)

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

        from PyQt6.QtWidgets import QApplication
        modifiers = QApplication.keyboardModifiers()

        if modifiers & Qt.KeyboardModifier.AltModifier:
            selected_ids = set()
            for selected_index in self.selectedIndexes():
                if selected_index.column() != 0:
                    continue
                selected_node = model.get_node(selected_index)
                if selected_node and selected_node.account and not selected_node.is_virtual:
                    selected_ids.add(selected_node.account.id)
            selected_ids.add(acc.id)
            selected_ids.update(self.account_repo.get_all_descendants(acc.id))

            additive = bool(modifiers & (Qt.KeyboardModifier.ControlModifier | Qt.KeyboardModifier.ShiftModifier))
            self._select_account_ids(selected_ids, additive=additive)
            self.account_selected.emit(list(selected_ids))
            return

        if modifiers & (Qt.KeyboardModifier.ControlModifier | Qt.KeyboardModifier.ShiftModifier):
            self._on_selection_changed()
            return

        self.account_selected.emit([acc.id])

    def _select_account_ids(self, account_ids: set[int], additive: bool) -> None:
        model: AccountTreeModel = self.model()
        sel_model = self.selectionModel()
        if model is None or sel_model is None:
            return

        if not additive:
            sel_model.clearSelection()

        flags = QItemSelectionModel.SelectionFlag.Select | QItemSelectionModel.SelectionFlag.Rows
        for account_id in account_ids:
            idx = model.get_index_for_account(account_id)
            if idx.isValid():
                sel_model.select(idx, flags)
                self.scrollTo(idx)

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


    def _show_header_menu(self, pos):
        show_column_visibility_menu(self, self.header(), pos)

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

        new_id = self.account_repo.insert(parent_id, tr("New Account"), None, None, None, False)
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

        dlg = DeleteAccountDialog(acc.name, self.account_repo, self.split_repo, self.settings, acc.id, self)
        if dlg.exec() != DeleteAccountDialog.DialogCode.Accepted:
            return

        action = dlg.action
        if action == DeleteAccountDialog.HIDE:
            self.account_repo.update_hidden(acc.id, True)
        elif action == DeleteAccountDialog.DELETE:
            # Handle sub-accounts
            if dlg.subaccounts_action == DeleteAccountDialog.MOVE_SUBACCOUNTS:
                # Move direct children to target account
                target_id = dlg.subaccounts_target_id
                if target_id is not None:
                    children = self.account_repo.get_children(acc.id)
                    for child in children:
                        self.account_repo.update_parent(child.id, target_id)
            elif dlg.subaccounts_action == DeleteAccountDialog.DELETE_SUBACCOUNTS:
                # Delete all sub-accounts recursively
                self._delete_all_descendants(acc.id)

            # Handle transactions - get list of accounts to process
            accounts_to_process = [acc.id]
            if dlg.subaccounts_action != DeleteAccountDialog.DELETE_SUBACCOUNTS:
                descendants = self.account_repo.get_all_descendants(acc.id)
                accounts_to_process.extend(descendants)

            if dlg.transactions_action == DeleteAccountDialog.MOVE_SPLITS:
                target_id = dlg.transactions_target_id
                if target_id is not None:
                    for acc_id in accounts_to_process:
                        self.account_repo.move_splits_to_account(acc_id, target_id)
            elif dlg.transactions_action == DeleteAccountDialog.DELETE_SPLITS:
                for acc_id in accounts_to_process:
                    self.split_repo.delete_by_account(acc_id)
            elif dlg.transactions_action == DeleteAccountDialog.DELETE_TRANS:
                trans_ids = set()
                for acc_id in accounts_to_process:
                    trans_ids.update(self.account_repo.get_transaction_ids_for_account(acc_id))
                for tid in trans_ids:
                    self.trans_repo.delete(tid)

            # Delete the account
            self.account_repo.delete(acc.id)

        self.balance_service.clear()
        model.reload()
        self.expandAll()

    def _delete_all_descendants(self, account_id: int):
        """Recursively delete all descendants of an account."""
        children = self.account_repo.get_children(account_id)
        for child in children:
            self._delete_all_descendants(child.id)
            self.account_repo.delete(child.id)

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat("application/x-chaoscash-account"):
            self._drag_in_progress = True
            target_index = self.indexAt(event.position().toPoint())
            if target_index.isValid():
                self._update_drop_target(target_index, event)
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if not event.mimeData().hasFormat("application/x-chaoscash-account"):
            event.ignore()
            return

        target_index = self.indexAt(event.position().toPoint())
        if target_index.isValid():
            self._update_drop_target(target_index, event)
        else:
            self._clear_drop_target()
        event.acceptProposedAction()

    def dragLeaveEvent(self, event):
        self._clear_drop_target()
        self._drag_in_progress = False
        event.accept()

    def dropEvent(self, event):
        """Handle DnD with cycle detection."""
        self._clear_drop_target()
        self._drag_in_progress = False

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

    def _update_drop_target(self, target_index: QModelIndex, event):
        """Update visual feedback for drop target with cursor indication."""
        model: AccountTreeModel = self.model()
        if model is None:
            return

        # Get dragged IDs for validation
        dragged_indexes = self.selectedIndexes()
        dragged_ids = set()
        for idx in dragged_indexes:
            if idx.column() == 0:
                node = model.get_node(idx)
                if node and node.account:
                    dragged_ids.add(node.account.id)

        # Get target account ID
        target_node = model.get_node(target_index)
        target_id = target_node.account.id if (target_node and target_node.account) else None

        # Check if drop is valid (no cycles)
        is_valid_drop = True
        if target_id is not None:
            for moved_id in dragged_ids:
                if self._would_create_cycle(moved_id, target_id, model):
                    is_valid_drop = False
                    break

        # Update current target and repaint
        if self._current_drop_target != target_index:
            if self._current_drop_target is not None:
                self.viewport().update(self.visualRect(self._current_drop_target))
            self._current_drop_target = target_index
            self.viewport().update(self.visualRect(target_index))

        # Set cursor based on validity
        if is_valid_drop:
            self.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        else:
            self.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))

    def _clear_drop_target(self):
        """Clear the drop target highlight and restore cursor."""
        self.unsetCursor()
        if self._current_drop_target is not None:
            self.viewport().update(self.visualRect(self._current_drop_target))
        self._current_drop_target = None

    def startDrag(self, supported_actions):
        """Create a custom drag pixmap showing what's being dragged."""
        model: AccountTreeModel = self.model()
        if model is None:
            return

        # Get selected account names
        selected_indexes = self.selectedIndexes()
        account_names = []
        for idx in selected_indexes:
            if idx.column() == 0:
                node = model.get_node(idx)
                if node and node.account and not node.is_virtual:
                    account_names.append(node.account.name)

        if not account_names:
            return

        # Create a text representation
        if len(account_names) == 1:
            text = account_names[0]
        else:
            text = f"{account_names[0]} (+{len(account_names) - 1})"

        # Create pixmap with text
        font = QFont()
        font.setPointSize(10)
        metrics = self.fontMetrics()
        text_width = metrics.horizontalAdvance(text) + 20
        text_height = metrics.height() + 10

        pixmap = QPixmap(text_width, text_height)
        pixmap.fill(QColor(200, 230, 201, 200))  # Light green with transparency

        painter = QPainter(pixmap)
        painter.setFont(font)
        painter.setPen(QPen(QColor(27, 94, 32)))  # Dark green text
        painter.drawText(pixmap.rect(), Qt.AlignmentFlag.AlignCenter, text)
        painter.drawRect(0, 0, pixmap.width() - 1, pixmap.height() - 1)
        painter.end()

        # Start drag with custom pixmap
        drag = QDrag(self)
        drag.setPixmap(pixmap)
        drag.setHotSpot(pixmap.rect().center())

        # Use existing MIME data from model
        mime = model.mimeData(self.selectedIndexes())
        drag.setMimeData(mime)

        drag.exec(supported_actions)

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


    def _toggle_column(self, col: int, checked: bool):
        set_column_visibility(self, col, checked)

    def drawRow(self, painter: QPainter, option, index: QModelIndex):
        """Override drawRow to highlight drop target."""
        # Draw the normal row first
        super().drawRow(painter, option, index)

        # If this is the current drop target, draw visual feedback
        if self._drag_in_progress and self._current_drop_target is not None:
            if index == self._current_drop_target:
                model: AccountTreeModel = self.model()
                if model is None:
                    return

                # Determine if this is a valid drop target
                dragged_indexes = self.selectedIndexes()
                dragged_ids = set()
                for idx in dragged_indexes:
                    if idx.column() == 0:
                        node = model.get_node(idx)
                        if node and node.account:
                            dragged_ids.add(node.account.id)

                target_node = model.get_node(index)
                target_id = target_node.account.id if (target_node and target_node.account) else None

                is_valid_drop = True
                if target_id is not None:
                    for moved_id in dragged_ids:
                        if self._would_create_cycle(moved_id, target_id, model):
                            is_valid_drop = False
                            break

                # Draw highlight background
                painter.save()
                if is_valid_drop:
                    # Green for valid drop
                    painter.fillRect(option.rect, QBrush(QColor(200, 230, 201, 100)))
                else:
                    # Red for invalid drop
                    painter.fillRect(option.rect, QBrush(QColor(255, 205, 210, 100)))
                painter.restore()
