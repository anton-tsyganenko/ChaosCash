"""Split table view with context menu."""
from PyQt6.QtWidgets import QTableView, QMenu, QAbstractItemView
from PyQt6.QtCore import Qt, pyqtSignal, QModelIndex
from PyQt6.QtGui import QAction
from app.i18n import tr
from app.services.transaction_service import TransactionService
from app.ui.item_models.split_model import SplitModel, ROW_PHANTOM, ROW_REAL


class SplitView(QTableView):
    """Table view for splits of the selected transaction."""

    split_changed = pyqtSignal()  # notify parent of changes

    def __init__(self, trans_service: TransactionService, parent=None):
        super().__init__(parent)
        self.trans_service = trans_service

        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setUniformRowHeights(True)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_context_menu)

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
        self.trans_service.delete_split(split_id)
        self.split_changed.emit()
