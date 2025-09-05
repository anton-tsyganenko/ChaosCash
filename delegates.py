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
    def __init__(self, parent, id_to_name):
        #print("called init")
        super().__init__(parent)
        self.id_to_name = id_to_name

    def createEditor(self, parent, option, index):
        #print("called createEditor")
        editor = QComboBox(parent)
        for acc_id, name in self.id_to_name.items():
            editor.addItem(name, acc_id)
        return editor

    def setEditorData(self, editor, index):
        #print("called SetEditorData")
        account_id = index.data(Qt.ItemDataRole.UserRole)
        for i in range(editor.count()):
            item_id = editor.itemData(i, Qt.ItemDataRole.UserRole)
            if item_id == account_id:
                editor.setCurrentIndex(i)
                return

    def setModelData(self, editor, model, index):
        """
        Сохраняет данные из редактора обратно в модель.
        """
        #print("called SetModelData")
        selected_id = editor.currentData(Qt.ItemDataRole.UserRole)

        model.setData(index, selected_id, Qt.ItemDataRole.UserRole)
        #model.setData(index, self.id_to_name.get(selected_id), Qt.ItemDataRole.DisplayRole)
        
    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
