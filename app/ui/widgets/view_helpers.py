"""Shared helpers for table/tree UI widgets."""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QAbstractItemView, QMenu
from PyQt6.QtGui import QAction


def find_next_editable_table_cell(view):
    """Return next editable index for MoveNext navigation in table-like views."""
    current = view.currentIndex()
    model = view.model()
    if model is None or not current.isValid():
        return None

    row = current.row()
    col = current.column()
    row_count = model.rowCount()
    col_count = model.columnCount()

    while True:
        col += 1
        if col >= col_count:
            col = 0
            row += 1
        if row >= row_count:
            return None
        candidate = model.index(row, col)
        if model.flags(candidate) & Qt.ItemFlag.ItemIsEditable:
            return candidate


def show_column_visibility_menu(view, header, pos):
    """Render a common show/hide-columns menu for item views."""
    model = view.model()
    if model is None:
        return

    menu = QMenu(view)
    for logical in range(model.columnCount()):
        title = model.headerData(logical, Qt.Orientation.Horizontal, Qt.ItemDataRole.DisplayRole)
        action = QAction(str(title), view)
        action.setCheckable(True)
        action.setChecked(not view.isColumnHidden(logical))
        action.toggled.connect(lambda checked, col=logical: set_column_visibility(view, col, checked))
        menu.addAction(action)

    menu.exec(header.mapToGlobal(pos))


def set_column_visibility(view, col: int, checked: bool):
    """Hide/show a column while ensuring at least one column remains visible."""
    model = view.model()
    if model is None:
        return

    visible = sum(0 if view.isColumnHidden(i) else 1 for i in range(model.columnCount()))
    if not checked and visible <= 1:
        return
    view.setColumnHidden(col, not checked)
