"""Split table view with context menu."""
from PyQt6.QtWidgets import QTableView, QMenu, QAbstractItemView
from PyQt6.QtCore import Qt, pyqtSignal, QModelIndex
from PyQt6.QtGui import QAction
from app.i18n import tr
from app.services.transaction_service import TransactionService
from app.ui.item_models.split_model import SplitModel, ROW_PHANTOM, ROW_REAL, COL_FIXED


class SplitView(QTableView):
    """Table view for splits of the selected transaction."""

    split_changed = pyqtSignal()  # notify parent of changes

    def __init__(self, trans_service: TransactionService, parent=None):
        super().__init__(parent)
        self.trans_service = trans_service

        self.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self._show_context_menu)

        header = self.horizontalHeader()
        header.setSectionsMovable(True)
        header.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        header.customContextMenuRequested.connect(self._show_header_menu)

        self.setSortingEnabled(True)

    def mousePressEvent(self, event):
        index = self.indexAt(event.pos())
        if (index.isValid()
                and index.column() == COL_FIXED
                and event.button() == Qt.MouseButton.LeftButton):
            model: SplitModel = self.model()
            if model and model.get_row_type(index.row()) == ROW_REAL:
                current = index.data(Qt.ItemDataRole.CheckStateRole)
                if current is not None:
                    new_state = (Qt.CheckState.Unchecked
                                 if current == Qt.CheckState.Checked
                                 else Qt.CheckState.Checked)
                    model.setData(index, new_state, Qt.ItemDataRole.CheckStateRole)
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
        header = self.horizontalHeader()
        model = self.model()
        if model is None:
            return

        menu = QMenu(self)
        for logical in range(model.columnCount()):
            title = model.headerData(logical, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole)
            action = QAction(str(title), self)
            action.setCheckable(True)
            action.setChecked(not self.isColumnHidden(logical))
            action.toggled.connect(lambda checked, col=logical: self._toggle_column(col, checked))
            menu.addAction(action)

        menu.exec(header.mapToGlobal(pos))


    def _toggle_column(self, col: int, checked: bool):
        visible = sum(0 if self.isColumnHidden(i) else 1 for i in range(self.model().columnCount()))
        if not checked and visible <= 1:
            return
        self.setColumnHidden(col, not checked)
