"""Searchable currency combo delegate."""
from PyQt6.QtWidgets import QStyledItemDelegate, QComboBox
from PyQt6.QtCore import Qt
from app.repositories.currency_repo import CurrencyRepo


class CurrencyComboDelegate(QStyledItemDelegate):
    """Searchable combobox for currency selection in splits."""

    def __init__(self, currency_repo: CurrencyRepo, parent=None):
        super().__init__(parent)
        self.currency_repo = currency_repo

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.setEditable(True)
        editor.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        currencies = self.currency_repo.get_all()
        for cur in currencies:
            editor.addItem(cur.code, cur.id)
        editor.completer().setFilterMode(Qt.MatchFlag.MatchContains)
        editor.completer().setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        return editor

    def setEditorData(self, editor: QComboBox, index):
        currency_id = index.data(Qt.ItemDataRole.UserRole)
        for i in range(editor.count()):
            if editor.itemData(i) == currency_id:
                editor.setCurrentIndex(i)
                return

    def setModelData(self, editor: QComboBox, model, index):
        selected_id = editor.currentData()
        # Find code for display
        currencies = self.currency_repo.get_all()
        code = ""
        for c in currencies:
            if c.id == selected_id:
                code = c.code
                break
        model.setData(index, code, Qt.ItemDataRole.DisplayRole)
        model.setData(index, selected_id, Qt.ItemDataRole.UserRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
