"""Transaction table view with context menu."""
from PyQt6.QtWidgets import QTableView, QMenu, QAbstractItemView
from PyQt6.QtCore import Qt, pyqtSignal, QModelIndex
from PyQt6.QtGui import QAction
from app.i18n import tr
from app.services.transaction_service import TransactionService
from app.ui.item_models.transaction_model import TransactionModel


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

    def setModel(self, model):
        super().setModel(model)
        if self.selectionModel() is not None:
            self.selectionModel().currentRowChanged.connect(self._on_current_row_changed)

    def keyPressEvent(self, event):
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
        if cursorAction == QAbstractItemView.CursorAction.MoveNext:
            idx = self.currentIndex()
            model = self.model()
            if model is not None and idx.isValid():
                row = idx.row()
                col = idx.column()
                row_count = model.rowCount()
                col_count = model.columnCount()
                while True:
                    col += 1
                    if col >= col_count:
                        col = 0
                        row += 1
                    if row >= row_count:
                        break
                    cand = model.index(row, col)
                    if model.flags(cand) & Qt.ItemFlag.ItemIsEditable:
                        return cand
        return super().moveCursor(cursorAction, modifiers)

    def _on_current_row_changed(self, current: QModelIndex, previous: QModelIndex):
        if not current.isValid():
            return
        self._on_clicked(current)

    def _on_clicked(self, index: QModelIndex):
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
        header = self.horizontalHeader()
        menu = QMenu(self)
        model = self.model()
        if model is None:
            return

        for logical in range(model.columnCount()):
            title = model.headerData(logical, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole)
            action = QAction(str(title), self)
            action.setCheckable(True)
            action.setChecked(not self.isColumnHidden(logical))
            action.toggled.connect(
                lambda checked, col=logical: self._toggle_column(col, checked)
            )
            menu.addAction(action)

        menu.exec(header.mapToGlobal(pos))


    def _toggle_column(self, col: int, checked: bool):
        visible = sum(0 if self.isColumnHidden(i) else 1 for i in range(self.model().columnCount()))
        if not checked and visible <= 1:
            return
        self.setColumnHidden(col, not checked)
