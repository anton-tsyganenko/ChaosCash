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

    def __init__(self, trans_service: TransactionService, parent=None):
        super().__init__(parent)
        self.trans_service = trans_service

        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_context_menu)
        self.clicked.connect(self._on_clicked)

    def _on_clicked(self, index: QModelIndex):
        model: TransactionModel = self.model()
        trans_id = model.get_trans_id(index.row())
        if trans_id:
            self.transaction_selected.emit(trans_id)

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
