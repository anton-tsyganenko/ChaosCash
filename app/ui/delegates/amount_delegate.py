"""Delegate for amount fields with arithmetic expression support."""
from PyQt6.QtWidgets import QStyledItemDelegate, QLineEdit, QToolTip
from PyQt6.QtCore import Qt, QEvent
from app.utils.expression_parser import safe_eval


class AmountDelegate(QStyledItemDelegate):
    """Amount field that supports arithmetic expressions."""

    def __init__(self, settings, parent=None):
        super().__init__(parent)
        self.settings = settings

    def _preprocess(self, text: str) -> str:
        """Normalise locale-specific separators so safe_eval can parse the result.

        Steps (applied in order to avoid double-replacement):
        1. Remove thousands separator (e.g. space, dot, comma).
        2. Replace the decimal separator with '.'.
        3. Replace any remaining ',' with '.' so that a comma not used as
           thousands separator is still accepted as a decimal point.
        """
        result = text
        if self.settings.thousands_sep:
            result = result.replace(self.settings.thousands_sep, "")
        if self.settings.decimal_sep != ".":
            result = result.replace(self.settings.decimal_sep, ".")
        result = result.replace(",", ".")
        return result

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setAlignment(Qt.AlignmentFlag.AlignRight)
        return editor

    def setEditorData(self, editor: QLineEdit, index):
        value = index.data(Qt.ItemDataRole.DisplayRole) or ""
        editor.setText(str(value))
        editor.selectAll()

    def eventFilter(self, editor, event):
        """Block commit on Enter/Tab when the expression is invalid."""
        if isinstance(editor, QLineEdit) and event.type() == QEvent.Type.KeyPress:
            if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter, Qt.Key.Key_Tab):
                text = editor.text().strip()
                if text:
                    try:
                        safe_eval(self._preprocess(text))
                    except ValueError:
                        QToolTip.showText(
                            editor.mapToGlobal(editor.rect().bottomLeft()),
                            "Ошибка: неверное выражение",
                            editor,
                        )
                        return True  # consume event — editor stays open
        return super().eventFilter(editor, event)

    def setModelData(self, editor: QLineEdit, model, index):
        text = editor.text().strip()
        if not text:
            model.setData(index, "0", Qt.ItemDataRole.EditRole)
            model.setData(index, "", Qt.ItemDataRole.UserRole)
            return
        try:
            result = safe_eval(self._preprocess(text))
            # Keep evaluated value in the amount cell, but store raw user input
            # in UserRole so caller can detect textual edits (e.g. "1000/2").
            # UserRole is written first so change handlers can read it while
            # processing the EditRole notification.
            model.setData(index, text, Qt.ItemDataRole.UserRole)
            model.setData(index, f"{result}", Qt.ItemDataRole.EditRole)
        except ValueError:
            pass  # editor was closed without Enter (e.g. click away) — discard silently

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
