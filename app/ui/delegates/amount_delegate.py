"""Delegate for amount fields with arithmetic expression support."""
from PyQt6.QtWidgets import QStyledItemDelegate, QLineEdit
from PyQt6.QtCore import Qt
from app.utils.expression_parser import safe_eval
from app.utils.amount_math import parse_amount


class AmountDelegate(QStyledItemDelegate):
    """Amount field that supports arithmetic expressions."""

    def __init__(self, settings, parent=None):
        super().__init__(parent)
        self.settings = settings

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setAlignment(Qt.AlignmentFlag.AlignRight)
        return editor

    def setEditorData(self, editor: QLineEdit, index):
        value = index.data(Qt.ItemDataRole.DisplayRole) or ""
        editor.setText(str(value))
        editor.selectAll()

    def setModelData(self, editor: QLineEdit, model, index):
        text = editor.text().strip()
        if not text:
            model.setData(index, "0", Qt.ItemDataRole.EditRole)
            return
        try:
            result = safe_eval(text)
            # Format result
            from app.utils.amount_math import format_amount
            # Store as string for now; conversion happens in service
            model.setData(index, f"{result}", Qt.ItemDataRole.EditRole)
        except ValueError:
            # Keep original on parse error
            pass

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
