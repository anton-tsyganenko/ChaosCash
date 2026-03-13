"""Account tree view with context menu and drag-and-drop."""
from PyQt6.QtCore import QItemSelectionModel, QModelIndex, QPoint, QRect, Qt, pyqtSignal
from PyQt6.QtGui import QAction, QColor, QDrag, QPainter, QPixmap
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

        self._dragged_ids: set[int] = set()
        self._drag_active = False
        self._drop_highlight_index: QModelIndex | None = None

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

    def startDrag(self, supportedActions):
        """Create a custom drag with account name preview and grabbing cursor."""
        import logging
        log = logging.getLogger(__name__)
        log.warning("[DnD] startDrag called, supportedActions=%s", supportedActions)

        model: AccountTreeModel = self.model()
        indexes = self.selectedIndexes()
        dragged_ids = set()
        first_name_index = None
        for idx in indexes:
            if idx.column() == 0:
                node = model.get_node(idx)
                if node and node.account and not node.is_virtual:
                    dragged_ids.add(node.account.id)
                    if first_name_index is None:
                        first_name_index = idx
        if not dragged_ids:
            log.warning("[DnD] startDrag: no dragged_ids, returning early")
            return

        log.warning("[DnD] startDrag: dragged_ids=%s", dragged_ids)
        self._dragged_ids = dragged_ids
        self._drag_active = True

        mime = model.mimeData(indexes)
        log.warning("[DnD] mimeData formats=%s", mime.formats())
        drag = QDrag(self)
        drag.setMimeData(mime)

        # Grab the visual row of the first selected account as drag pixmap
        rect = self.visualRect(first_name_index)
        log.warning("[DnD] visualRect=%s (x=%d, y=%d, w=%d, h=%d)",
                    rect, rect.x(), rect.y(), rect.width(), rect.height())
        row_rect = QRect(0, rect.y(), self.viewport().width(), rect.height())
        log.warning("[DnD] row_rect=%s, viewport size=%s",
                    row_rect, self.viewport().size())
        pixmap = self.viewport().grab(row_rect)
        log.warning("[DnD] grabbed pixmap: size=%s, isNull=%s",
                    pixmap.size(), pixmap.isNull())

        # Add semi-transparency
        translucent = QPixmap(pixmap.size())
        translucent.fill(Qt.GlobalColor.transparent)
        painter = QPainter(translucent)
        painter.setOpacity(0.7)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()
        log.warning("[DnD] translucent pixmap: size=%s, isNull=%s",
                    translucent.size(), translucent.isNull())
        drag.setPixmap(translucent)
        drag.setHotSpot(QPoint(rect.x(), rect.height() // 2))
        log.warning("[DnD] hotSpot=%s", drag.hotSpot())

        log.warning("[DnD] calling QApplication.setOverrideCursor(ClosedHandCursor)")
        QApplication.setOverrideCursor(Qt.CursorShape.ClosedHandCursor)
        log.warning("[DnD] calling drag.exec(MoveAction)")
        result = drag.exec(Qt.DropAction.MoveAction)
        log.warning("[DnD] drag.exec returned: %s", result)
        QApplication.restoreOverrideCursor()
        self._drag_active = False
        self._dragged_ids = set()
        self._clear_drop_highlight()

    def _is_valid_drop_target(self, index: QModelIndex) -> bool:
        """Check if dropping onto index would be valid for all dragged items."""
        model: AccountTreeModel = self.model()
        if index.isValid():
            target_node = model.get_node(index)
            if target_node and target_node.is_virtual:
                return False
            target_id = target_node.account.id if (target_node and target_node.account) else None
        else:
            target_id = None

        for moved_id in self._dragged_ids:
            if self._would_create_cycle(moved_id, target_id, model):
                return False
        return True

    def _clear_drop_highlight(self):
        """Remove drop highlight from previously highlighted item."""
        if hasattr(self, "_drop_highlight_index") and self._drop_highlight_index is not None:
            self._drop_highlight_index = None
            self.viewport().update()

    def dragEnterEvent(self, event):
        import logging
        log = logging.getLogger(__name__)
        has_fmt = event.mimeData().hasFormat("application/x-chaoscash-account")
        log.warning("[DnD] dragEnterEvent: hasFormat=%s, formats=%s",
                    has_fmt, event.mimeData().formats())
        if has_fmt:
            event.acceptProposedAction()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        import logging
        log = logging.getLogger(__name__)
        if not event.mimeData().hasFormat("application/x-chaoscash-account"):
            log.warning("[DnD] dragMoveEvent: wrong format, ignoring")
            event.ignore()
            return

        index = self.indexAt(event.position().toPoint())
        valid = self._is_valid_drop_target(index)
        log.warning("[DnD] dragMoveEvent: pos=%s, index.isValid=%s, valid=%s, _drag_active=%s",
                    event.position().toPoint(), index.isValid(), valid,
                    getattr(self, '_drag_active', 'N/A'))

        old_highlight = getattr(self, "_drop_highlight_index", None)
        if index.isValid() and valid:
            self._drop_highlight_index = index
        else:
            self._drop_highlight_index = None
        if old_highlight != self._drop_highlight_index:
            self.viewport().update()

        if valid:
            QApplication.changeOverrideCursor(Qt.CursorShape.ClosedHandCursor)
            event.setDropAction(Qt.DropAction.MoveAction)
            event.accept()
        else:
            QApplication.changeOverrideCursor(Qt.CursorShape.ForbiddenCursor)
            event.setDropAction(Qt.DropAction.IgnoreAction)
            event.accept()

    def dragLeaveEvent(self, event):
        import logging
        logging.getLogger(__name__).warning("[DnD] dragLeaveEvent")
        self._clear_drop_highlight()
        super().dragLeaveEvent(event)

    def paintEvent(self, event):
        super().paintEvent(event)
        highlight = getattr(self, "_drop_highlight_index", None)
        if highlight is not None and highlight.isValid():
            rect = self.visualRect(highlight)
            if not rect.isNull():
                # Draw highlight across the full row width
                rect.setLeft(0)
                rect.setWidth(self.viewport().width())
                painter = QPainter(self.viewport())
                painter.setPen(QColor(41, 128, 185))
                painter.setBrush(QColor(41, 128, 185, 40))
                painter.drawRect(rect.adjusted(0, 0, -1, -1))
                painter.end()

    def dropEvent(self, event):
        """Handle DnD with cycle detection."""
        import logging
        log = logging.getLogger(__name__)
        log.warning("[DnD] dropEvent called")
        self._clear_drop_highlight()

        if not event.mimeData().hasFormat("application/x-chaoscash-account"):
            event.ignore()
            return
        target_index = self.indexAt(event.position().toPoint())
        model: AccountTreeModel = self.model()

        dragged_ids = getattr(self, "_dragged_ids", set())
        if not dragged_ids:
            dragged_indexes = self.selectedIndexes()
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


    def _toggle_column(self, col: int, checked: bool):
        set_column_visibility(self, col, checked)
