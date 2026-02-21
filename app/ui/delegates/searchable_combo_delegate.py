"""Reusable searchable-combobox delegate for ID-backed selections."""
from __future__ import annotations

import logging
from PyQt6.QtCore import QEvent, Qt
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import QComboBox, QLineEdit, QStyledItemDelegate


class SearchableComboDelegate(QStyledItemDelegate):
    """Thin delegate for editable combobox columns that store selected IDs."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._logger = logging.getLogger(f"chaoscash.ui.delegate.{self.__class__.__name__.lower()}")

    def _get_items(self) -> list[tuple[str, int]]:
        """Return list of ``(display_text, id)`` options for editor."""
        raise NotImplementedError

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.setEditable(True)
        editor.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)
        for display, item_id in self._get_items():
            editor.addItem(display, item_id)
        completer = editor.completer()
        if completer is not None:
            completer.setFilterMode(Qt.MatchFlag.MatchContains)
            completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        editor.installEventFilter(self)
        line_edit = editor.lineEdit()
        if line_edit is not None:
            line_edit.installEventFilter(self)
        return editor

    def eventFilter(self, watched, event):
        if event.type() == QEvent.Type.KeyPress and isinstance(event, QKeyEvent):
            combo = self._extract_combo(watched)
            if combo is not None and event.key() == Qt.Key.Key_Tab:
                self._apply_current_completion(combo)
                self.commitData.emit(combo)
                self.closeEditor.emit(combo, QStyledItemDelegate.EndEditHint.EditNextItem)
                return True
        return super().eventFilter(watched, event)

    def _extract_combo(self, watched) -> QComboBox | None:
        if isinstance(watched, QComboBox):
            return watched
        if isinstance(watched, QLineEdit) and isinstance(watched.parent(), QComboBox):
            return watched.parent()
        return None

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

        completion = (completer.currentCompletion() or "").strip()
        if completion:
            combo.setEditText(completion)
        self._sync_index_with_text(combo)

    def setEditorData(self, editor: QComboBox, index):
        selected_id = index.data(Qt.ItemDataRole.UserRole)
        if selected_id is not None:
            item_index = editor.findData(selected_id)
            if item_index >= 0:
                editor.setCurrentIndex(item_index)
        else:
            display = (index.data(Qt.ItemDataRole.DisplayRole) or "").strip()
            if display:
                item_index = editor.findText(display)
                if item_index >= 0:
                    editor.setCurrentIndex(item_index)

        line_edit = editor.lineEdit()
        if line_edit is not None:
            line_edit.selectAll()

    def setModelData(self, editor: QComboBox, model, index):
        self._sync_index_with_text(editor)
        current_index = editor.currentIndex()
        selected_id = editor.itemData(current_index) if current_index >= 0 else None

        if selected_id is None:
            self._logger.debug("Ignoring commit for unmatched combo text=%r", editor.currentText())
            return

        model.setData(index, editor.itemText(current_index).strip(), Qt.ItemDataRole.DisplayRole)
        model.setData(index, selected_id, Qt.ItemDataRole.UserRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
