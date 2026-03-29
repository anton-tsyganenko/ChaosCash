"""Shared helpers for table/tree UI widgets."""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu

ACCOUNT_TREE_DEFAULT_WIDTHS = {0: 220, 1: 130, 2: 130, 3: 60, 4: 90, 5: 120, 6: 220}
ACCOUNT_TREE_DEFAULT_HIDDEN = [2, 3, 4, 5, 6]
ACCOUNT_TREE_DEFAULT_SORT_COL = 0
ACCOUNT_TREE_DEFAULT_SORT_ORDER = Qt.SortOrder.AscendingOrder


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
    callback = getattr(view, "display_change_callback", None)
    if callable(callback):
        callback()


def apply_display_settings(
    view,
    header,
    display,
    *,
    default_order: list[int],
    default_widths: dict[int, int],
    default_hidden: list[int],
    default_sort_col: int,
    default_sort_order: Qt.SortOrder,
):
    """Apply persisted column/sort settings to a view."""
    model = view.model()
    if model is None:
        return
    col_count = model.columnCount()

    order = display.get_column_order(default_order)
    if sorted(order) == list(range(col_count)):
        for visual_pos, logical in enumerate(order):
            current = header.visualIndex(logical)
            if current != visual_pos:
                header.moveSection(current, visual_pos)

    hidden = [c for c in display.get_hidden_columns(default_hidden) if 0 <= c < col_count]
    if len(hidden) >= col_count:
        hidden = hidden[:-1]
    for c in range(col_count):
        view.setColumnHidden(c, c in hidden)

    widths = display.get_column_widths(default_widths)
    for col, width in widths.items():
        if 0 <= col < col_count and width > 20:
            header.resizeSection(col, width)

    sort_col = display.get_sort_column(default_sort_col)
    default_sort_value = int(default_sort_order.value)
    sort_order = Qt.SortOrder(display.get_sort_order(default_sort_value))
    if 0 <= sort_col < col_count:
        view.sortByColumn(sort_col, sort_order)
        header.setSortIndicator(sort_col, sort_order)


def apply_account_tree_display_settings(view, header, display):
    """Apply shared account-tree display defaults and persisted settings."""
    model = view.model()
    if model is None:
        return
    apply_display_settings(
        view,
        header,
        display,
        default_order=list(range(model.columnCount())),
        default_widths=ACCOUNT_TREE_DEFAULT_WIDTHS,
        default_hidden=ACCOUNT_TREE_DEFAULT_HIDDEN,
        default_sort_col=ACCOUNT_TREE_DEFAULT_SORT_COL,
        default_sort_order=ACCOUNT_TREE_DEFAULT_SORT_ORDER,
    )
