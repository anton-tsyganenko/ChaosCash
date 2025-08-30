from PyQt6.QtWidgets import QStyledItemDelegate, QDateTimeEdit, QComboBox
from PyQt6.QtCore import Qt, QDateTime, QModelIndex, QRect

class DateDelegate(QStyledItemDelegate):
    def __init__(self, date_format="yyyy-MM-dd hh:mm:ss"):
        super().__init__()
        self.date_format = date_format

    def createEditor(self, parent, option, index):
        editor = QDateTimeEdit(parent)
        editor.setCalendarPopup(True)
        editor.setDisplayFormat(self.date_format)
        return editor

    def setEditorData(self, editor, index):
        date_data = index.data(Qt.ItemDataRole.DisplayRole)
        date_time = QDateTime()
        if isinstance(date_data, str):
            date_time = QDateTime.fromString(date_data, self.date_format)
        
        if date_time.isValid():
            editor.setDateTime(date_time)
        else:
            editor.setDateTime(QDateTime.currentDateTime())

    def setModelData(self, editor, model, index):
        # 1. Получаем объект QDateTime из редактора
        date_time = editor.dateTime()
        
        # 2. Форматируем его в строку
        formatted_date = date_time.toString(self.date_format)
        
        # 3. Сохраняем отформатированную строку в модель
        model.setData(index, formatted_date, Qt.ItemDataRole.DisplayRole)




class ComboBoxDelegate(QStyledItemDelegate):
    """
    Delegate for creating a combo box editor.
    """
    def __init__(self, parent, items, item_map):
        super().__init__(parent)
        self.items = items
        self.item_map = item_map

    def createEditor(self, parent, option, index):
        editor = QComboBox(parent)
        editor.addItems(self.items)
        return editor

    def setEditorData(self, editor, index):
        # Set the editor's current index based on the model's data
        current_text = index.data(Qt.ItemDataRole.DisplayRole)
        current_index = editor.findText(current_text)
        if current_index >= 0:
            editor.setCurrentIndex(current_index)
        
    def setModelData(self, editor, model, index):
        # Get data from the editor and save it to the model
        selected_text = editor.currentText()
        selected_id = self.item_map.get(selected_text)
        
        # Set both the display text and the UserRole data
        if selected_id is not None:
            model.setData(index, selected_text, Qt.ItemDataRole.DisplayRole)
            model.setData(index, selected_id, Qt.ItemDataRole.UserRole)
        else:
            # Fallback for manually typed text that does not match
            model.setData(index, selected_text, Qt.ItemDataRole.DisplayRole)
            model.setData(index, None, Qt.ItemDataRole.UserRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
