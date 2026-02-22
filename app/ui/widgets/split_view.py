"""Split table view with context menu."""
import logging
from PyQt6.QtWidgets import QTableView, QMenu, QAbstractItemView
from PyQt6.QtCore import Qt, pyqtSignal, QModelIndex
from PyQt6.QtGui import QAction
from app.i18n import tr
from app.services.transaction_service import TransactionService
from app.ui.item_models.split_model import SplitModel, ROW_PHANTOM, ROW_REAL, COL_FIXED
from app.ui.widgets.view_helpers import (
    find_next_editable_table_cell,
    set_column_visibility,
    show_column_visibility_menu,
)


class SplitView(QTableView):
    """Table view for splits of the selected transaction."""

    split_changed = pyqtSignal()  # notify parent of changes

    escape_pressed = pyqtSignal()


    def __init__(self, trans_service: TransactionService, parent=None):
        super().__init__(parent)
        self.trans_service = trans_service
        self._logger = logging.getLogger("chaoscash.ui.split_view")

        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_context_menu)

        header = self.horizontalHeader()
        header.setSectionsMovable(True)
        header.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        header.customContextMenuRequested.connect(self._show_header_menu)

        self.setSortingEnabled(True)
        self.setObjectName("split_view")


    def _first_editable_in_row(self, row: int):
        model = self.model()
        if model is None:
            return QModelIndex()
        for col in range(model.columnCount()):
            idx = model.index(row, col)
            if model.flags(idx) & Qt.ItemFlag.ItemIsEditable:
                return idx
        return QModelIndex()

    def keyPressEvent(self, event):
        self._logger.debug("keyPressEvent key=%s text=%r modifiers=%s state=%s row=%s col=%s", event.key(), event.text(), int(event.modifiers().value), self.state().name, self.currentIndex().row() if self.currentIndex().isValid() else -1, self.currentIndex().column() if self.currentIndex().isValid() else -1)
        if self.state() == QAbstractItemView.State.EditingState:
            if event.key() == Qt.Key.Key_Escape:
                super().keyPressEvent(event)
                if self.state() != QAbstractItemView.State.EditingState:
                    self.escape_pressed.emit()
                    event.accept()
                return
            super().keyPressEvent(event)
            return
        if event.key() == Qt.Key.Key_Escape:
            self.escape_pressed.emit()
            event.accept()
            return
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            model = self.model()
            idx = self.currentIndex()
            if model is not None and idx.isValid():
                next_row = idx.row() + 1
                if next_row < model.rowCount():
                    next_idx = self._first_editable_in_row(next_row)
                    if next_idx.isValid():
                        self.setCurrentIndex(next_idx)
                        self.edit(next_idx)
                        event.accept()
                        return
        super().keyPressEvent(event)

    def moveCursor(self, cursorAction, modifiers):
        self._logger.debug("moveCursor action=%s modifiers=%s row=%s col=%s", cursorAction.name, int(modifiers.value), self.currentIndex().row() if self.currentIndex().isValid() else -1, self.currentIndex().column() if self.currentIndex().isValid() else -1)
        if cursorAction == QAbstractItemView.CursorAction.MoveNext:
            next_index = find_next_editable_table_cell(self)
            if next_index is not None:
                self._logger.debug("moveCursor next editable row=%s col=%s", next_index.row(), next_index.column())
                return next_index
        return super().moveCursor(cursorAction, modifiers)

    def mousePressEvent(self, event):
        self._logger.debug("mousePressEvent button=%s buttons=%s x=%s y=%s row=%s col=%s", int(event.button().value), int(event.buttons().value), event.position().x(), event.position().y(), self.indexAt(event.pos()).row() if self.indexAt(event.pos()).isValid() else -1, self.indexAt(event.pos()).column() if self.indexAt(event.pos()).isValid() else -1)
        super().mousePressEvent(event)

    def _show_context_menu(self, pos):
        index = self.indexAt(pos)
        if not index.isValid():
            return
        model: SplitModel = self.model()
        row = index.row()
        row_type = model.get_row_type(row)
        if row_type != ROW_REAL:
            return

        split = model.get_split(row)
        if split is None:
            return

        menu = QMenu(self)
        del_action = QAction(tr("&Delete Split"), self)
        del_action.triggered.connect(lambda: self._delete_split(split.id))
        menu.addAction(del_action)
        menu.exec(self.viewport().mapToGlobal(pos))

    def _delete_split(self, split_id: int):
        self.trans_service.delete_split_and_rebalance(split_id)
        self.split_changed.emit()


    def _show_header_menu(self, pos):
        show_column_visibility_menu(self, self.horizontalHeader(), pos)

    def _toggle_column(self, col: int, checked: bool):
        set_column_visibility(self, col, checked)
