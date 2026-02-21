"""Searchable currency combo delegate."""
from PyQt6.QtWidgets import QStyledItemDelegate, QComboBox, QLineEdit
from PyQt6.QtCore import Qt, QEvent
from PyQt6.QtGui import QKeyEvent
import logging
from app.repositories.currency_repo import CurrencyRepo


class CurrencyComboDelegate(QStyledItemDelegate):
    """Searchable combobox for currency selection in splits."""

    def __init__(self, currency_repo: CurrencyRepo, parent=None):
        super().__init__(parent)
        self.currency_repo = currency_repo
        self._logger = logging.getLogger("chaoscash.ui.delegate.currency_combo")

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.setEditable(True)
        editor.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        for cur in self.currency_repo.get_all():
            editor.addItem(cur.code, cur.id)
        editor.completer().setFilterMode(Qt.MatchFlag.MatchContains)
        editor.completer().setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        editor.installEventFilter(self)
        if editor.lineEdit() is not None:
            editor.lineEdit().installEventFilter(self)
        return editor

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.KeyPress and isinstance(event, QKeyEvent):
            combo = None
            if isinstance(watched, QComboBox):
                combo = watched
            elif isinstance(watched, QLineEdit) and isinstance(watched.parent(), QComboBox):
                combo = watched.parent()

            if combo is not None and event.key() == Qt.Key.Key_Tab:
                self._logger.debug(
                    "Tab intercepted combo=%s text_before=%r current_data_before=%r",
                    combo.__class__.__name__,
                    combo.currentText(),
                    combo.currentData(),
                )
                self._apply_current_completion(combo)
                self._logger.debug(
                    "Tab commit combo=%s text_after_completion=%r current_data_after=%r current_index_after=%r",
                    combo.__class__.__name__,
                    combo.currentText(),
                    combo.currentData(),
                    combo.currentIndex(),
                )
                self.commitData.emit(combo)
                self.closeEditor.emit(combo, QStyledItemDelegate.EndEditHint.EditNextItem)
                return True
        return super().eventFilter(watched, event)

    def _sync_index_with_text(self, combo: QComboBox) -> None:
        text = combo.currentText().strip().lower()
        if not text:
            return
        for i in range(combo.count()):
            if combo.itemText(i).strip().lower() == text:
                combo.setCurrentIndex(i)
                return

    def _apply_current_completion(self, combo: QComboBox) -> None:
        completer = combo.completer()
        if completer is None:
            return

        popup = completer.popup()
        if popup is not None and popup.isVisible():
            idx = popup.currentIndex()
            if idx.isValid():
                combo.setEditText(str(idx.data()))
                return

        # Use Qt completer's current completion when popup is not visible.
        completion = (completer.currentCompletion() or "").strip()
        if completion:
            combo.setEditText(completion)

        self._sync_index_with_text(combo)

    def setEditorData(self, editor: QComboBox, index):
        currency_id = index.data(Qt.ItemDataRole.UserRole)
        for i in range(editor.count()):
            if editor.itemData(i) == currency_id:
                editor.setCurrentIndex(i)
                editor.lineEdit().selectAll()
                return
        editor.lineEdit().selectAll()

    def setModelData(self, editor: QComboBox, model, index):
        self._sync_index_with_text(editor)
        current_index = editor.currentIndex()
        selected_id = (editor.itemData(current_index)
                       if current_index >= 0 else editor.currentData())
        current_text = editor.currentText().strip()
        previous_display = index.data(Qt.ItemDataRole.DisplayRole)
        previous_user = index.data(Qt.ItemDataRole.UserRole)
        self._logger.debug(
            "setModelData row=%s col=%s text=%r selected_id=%r prev_display=%r prev_user=%r count=%s current_index=%s",
            index.row(), index.column(), current_text, selected_id, previous_display, previous_user, editor.count(), current_index
        )

        if selected_id is not None:
            selected_idx = current_index if current_index >= 0 else editor.findData(selected_id)
            display_text = (editor.itemText(selected_idx).strip()
                            if selected_idx >= 0 else current_text)
            self._logger.debug(
                "setModelData commit row=%s col=%s selected_idx=%s display=%r user=%r",
                index.row(), index.column(), selected_idx, display_text, selected_id,
            )
            model.setData(index, display_text, Qt.ItemDataRole.DisplayRole)
            model.setData(index, selected_id, Qt.ItemDataRole.UserRole)
            return

        self._logger.debug(
            "setModelData rollback row=%s col=%s restoring display=%r user=%r",
            index.row(), index.column(), previous_display, previous_user,
        )
        model.setData(index, previous_display, Qt.ItemDataRole.DisplayRole)
        model.setData(index, previous_user, Qt.ItemDataRole.UserRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
