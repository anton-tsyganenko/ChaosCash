"""Searchable account combo delegate."""
from PyQt6.QtWidgets import QStyledItemDelegate, QComboBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from app.repositories.account_repo import AccountRepo


class AccountComboDelegate(QStyledItemDelegate):
    """Searchable combobox for account selection in splits."""

    def __init__(self, account_repo: AccountRepo, settings, parent=None):
        super().__init__(parent)
        self.account_repo = account_repo
        self.settings = settings

    def _get_accounts(self):
        """Return list of (id, path) for selectable accounts."""
        all_accs = self.account_repo.get_all()
        acc_map = {a.id: a for a in all_accs}

        def build_path(acc_id):
            parts = []
            cid = acc_id
            while cid is not None:
                acc = acc_map.get(cid)
                if acc is None:
                    break
                parts.insert(0, acc.name)
                cid = acc.parent
            return self.settings.account_path_sep.join(parts)

        show_hidden = self.settings.show_hidden_accounts
        result = []
        for acc in all_accs:
            if acc.status == "GRP":
                continue  # Cannot use GRP accounts in splits
            if acc.status == "HID" and not show_hidden:
                continue
            result.append((acc.id, build_path(acc.id)))
        result.sort(key=lambda x: x[1].lower())
        return result

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.setEditable(True)
        editor.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        accounts = self._get_accounts()
        for acc_id, path in accounts:
            editor.addItem(path, acc_id)
        editor.completer().setFilterMode(Qt.MatchFlag.MatchContains)
        editor.completer().setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        return editor

    def setEditorData(self, editor: QComboBox, index):
        account_id = index.data(Qt.ItemDataRole.UserRole)
        for i in range(editor.count()):
            if editor.itemData(i) == account_id:
                editor.setCurrentIndex(i)
                return
        # Try display text
        text = index.data(Qt.ItemDataRole.DisplayRole) or ""
        idx = editor.findText(text)
        if idx >= 0:
            editor.setCurrentIndex(idx)

    def setModelData(self, editor: QComboBox, model, index):
        selected_id = editor.currentData()
        if selected_id is None:
            # Try to find by text
            text = editor.currentText()
            for i in range(editor.count()):
                if editor.itemText(i) == text:
                    selected_id = editor.itemData(i)
                    break
        model.setData(index, editor.currentText(), Qt.ItemDataRole.DisplayRole)
        model.setData(index, selected_id, Qt.ItemDataRole.UserRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
