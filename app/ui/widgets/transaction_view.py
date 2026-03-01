"""Transaction table view with context menu."""
import logging

from PyQt6.QtCore import QModelIndex, Qt, pyqtSignal
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import (
    QAbstractItemDelegate,
    QAbstractItemView,
    QMenu,
    QTableView,
    QWidget,
)

from app.i18n import tr
from app.services.transaction_service import TransactionService
from app.ui.item_models.transaction_model import COL_DATE, COL_DESC, TransactionModel
from app.ui.widgets.view_helpers import (
    find_next_editable_table_cell,
    set_column_visibility,
    show_column_visibility_menu,
)


class TransactionView(QTableView):
    """Table view for transactions with context menu (duplicate, reverse, delete)."""

    transaction_selected = pyqtSignal(int)  # trans_id
    transactions_changed = pyqtSignal()     # refresh needed
    escape_pressed = pyqtSignal()
    enter_pressed = pyqtSignal()
    transaction_cleared = pyqtSignal()

    def __init__(self, trans_service: TransactionService, parent=None):
        super().__init__(parent)
        self.trans_service = trans_service
        self._logger = logging.getLogger("chaoscash.ui.transaction_view")
        self._processing_close_editor = False

        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_context_menu)
        self.clicked.connect(self._on_clicked)

        header = self.horizontalHeader()
        header.setSectionsMovable(True)
        header.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        header.customContextMenuRequested.connect(self._show_header_menu)

        self.setSortingEnabled(True)
        self.setObjectName("transaction_view")

    def setModel(self, model):
        super().setModel(model)
        if self.selectionModel() is not None:
            self.selectionModel().currentRowChanged.connect(self._on_current_row_changed)

    def keyPressEvent(self, event):
        self._logger.debug("keyPressEvent key=%s text=%r modifiers=%s state=%s row=%s col=%s", event.key(), event.text(), int(event.modifiers().value), self.state().name, self.currentIndex().row() if self.currentIndex().isValid() else -1, self.currentIndex().column() if self.currentIndex().isValid() else -1)
        if self.state() == QAbstractItemView.State.EditingState:
            super().keyPressEvent(event)
            return
        if event.key() == Qt.Key.Key_Escape:
            self.escape_pressed.emit()
            event.accept()
            return
        if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
            self.enter_pressed.emit()
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


    def closeEditor(self, editor: QWidget, hint):
        current = self.currentIndex()
        self._logger.debug(
            "closeEditor hint=%s current_row=%s current_col=%s",
            hint.name if hasattr(hint, "name") else str(hint),
            current.row() if current.isValid() else -1,
            current.column() if current.isValid() else -1,
        )
        if self._processing_close_editor:
            super().closeEditor(editor, hint)
            return

        if (
            hint == QAbstractItemDelegate.EndEditHint.EditNextItem
            and current.isValid()
            and current.column() == COL_DATE
        ):
            self._processing_close_editor = True
            try:
                super().closeEditor(editor, QAbstractItemDelegate.EndEditHint.NoHint)
                model = self.model()
                if model is not None:
                    next_idx = model.index(current.row(), COL_DESC)
                    if next_idx.isValid() and model.flags(next_idx) & Qt.ItemFlag.ItemIsEditable:
                        self._logger.debug("tab-navigation forcing date->description row=%s", current.row())
                        self.setCurrentIndex(next_idx)
                        self.edit(next_idx)
                        return
            finally:
                self._processing_close_editor = False

        super().closeEditor(editor, hint)

    def _on_current_row_changed(self, current: QModelIndex, previous: QModelIndex):
        self._logger.debug("currentRowChanged current=(%s,%s) previous=(%s,%s)", current.row() if current.isValid() else -1, current.column() if current.isValid() else -1, previous.row() if previous.isValid() else -1, previous.column() if previous.isValid() else -1)
        if not current.isValid():
            return
        self._on_clicked(current)

    def _on_clicked(self, index: QModelIndex):
        self._logger.debug("clicked row=%s col=%s", index.row(), index.column())
        model: TransactionModel = self.model()
        trans_id = model.get_trans_id(index.row())
        if trans_id:
            self.transaction_selected.emit(trans_id)
        else:
            self.transaction_cleared.emit()

    def _show_context_menu(self, pos):
        index = self.indexAt(pos)
        if not index.isValid():
            return
        model: TransactionModel = self.model()
        trans_id = model.get_trans_id(index.row())
        if trans_id is None:
            return

        menu = QMenu(self)

        dup_action = QAction(tr("&Duplicate"), self)
        dup_action.triggered.connect(lambda: self._duplicate(trans_id))
        menu.addAction(dup_action)

        rev_action = QAction(tr("&Reverse (Create Reversal)"), self)
        rev_action.triggered.connect(lambda: self._reverse(trans_id))
        menu.addAction(rev_action)

        menu.addSeparator()

        del_action = QAction(tr("De&lete"), self)
        del_action.triggered.connect(lambda: self._delete(trans_id))
        menu.addAction(del_action)

        menu.exec(self.viewport().mapToGlobal(pos))

    def _duplicate(self, trans_id: int):
        self.trans_service.duplicate_transaction(trans_id)
        self.transactions_changed.emit()

    def _reverse(self, trans_id: int):
        self.trans_service.reverse_transaction(trans_id)
        self.transactions_changed.emit()

    def _delete(self, trans_id: int):
        from PyQt6.QtWidgets import QMessageBox
        reply = QMessageBox.question(
            self, tr("Delete Transaction"),
            tr("Delete this transaction and all its splits?"),
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.trans_service.delete_transaction(trans_id)
            self.transactions_changed.emit()

    def _show_header_menu(self, pos):
        show_column_visibility_menu(self, self.horizontalHeader(), pos)

    def _toggle_column(self, col: int, checked: bool):
        set_column_visibility(self, col, checked)
