from PyQt6.QtWidgets import QMainWindow, QSplitter, QTreeView, QTableView, QVBoxLayout, QWidget, QHeaderView, QStyle, QStyleOptionButton, QStyledItemDelegate
from PyQt6.QtCore import Qt, QModelIndex, pyqtSignal, QAbstractItemModel
from PyQt6.QtGui import QStandardItemModel, QStandardItem, QBrush

class MainWindowView(QMainWindow):
    """
    Класс, отвечающий исключительно за создание и отображение GUI.
    Не содержит логики взаимодействия с базой данных.
    """
    # Определяем сигналы для передачи событий в контроллер
    account_selected = pyqtSignal(int)
    transaction_selected = pyqtSignal(str)
    transaction_data_changed = pyqtSignal(QModelIndex, QModelIndex)
    split_data_changed = pyqtSignal(QModelIndex, QModelIndex)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Персональный финансовый учет")
        self.setGeometry(0, 0, 1500, 900)

        self.setup_ui()
        self.setup_models()
        self.connect_signals()
    
    def setup_ui(self):
        """Настраивает основной макет и виджеты."""
        self.splitter = QSplitter(Qt.Orientation.Horizontal, self)
        self.setCentralWidget(self.splitter)

        self.account_view = QTreeView(self.splitter)
        self.account_view.setHeaderHidden(False)
        #self.account_view.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)

        self.tables_widget = QWidget(self.splitter)
        self.tables_layout = QVBoxLayout(self.tables_widget)

        self.transaction_table = QTableView(self.tables_widget)
        self.transaction_table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.transaction_table.setSelectionMode(QTableView.SelectionMode.SingleSelection)

        self.split_table = QTableView(self.tables_widget)
        self.split_table.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.split_table.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        
        self.tables_layout.addWidget(self.transaction_table)
        self.tables_layout.addWidget(self.split_table)
        self.splitter.setSizes([55, 89])

    def setup_models(self):
        """Создает модели данных для таблиц."""
        self.account_model = QStandardItemModel()
        self.account_view.setModel(self.account_model)
        
        self.transaction_model = QStandardItemModel()
        self.transaction_table.setModel(self.transaction_model)

        self.split_model = QStandardItemModel()
        self.split_table.setModel(self.split_model)


    def connect_signals(self):
        """Соединяет сигналы виджетов с сигналами View."""
        self.account_view.clicked.connect(self.on_account_clicked)
        self.transaction_table.clicked.connect(self.on_transaction_clicked)
        self.transaction_model.dataChanged.connect(self.transaction_data_changed.emit)
        self.split_model.dataChanged.connect(self.split_data_changed.emit)

    def on_account_clicked(self, index):
        """Передает событие клика по счету в контроллер."""
        item = self.account_model.itemFromIndex(index)
        if item:
            account_id = item.data(Qt.ItemDataRole.UserRole)
            self.account_selected.emit(account_id)

    def on_transaction_clicked(self, index):
        """Передает событие клика по транзакции в контроллер."""
        # Получаем индекс первой колонки (ID) в той же строке
        id_index = self.transaction_model.index(index.row(), 0)
        trans_id = id_index.data()
        if trans_id is not None:
            self.transaction_selected.emit(trans_id)

    def update_account_tree(self, accounts_data, current_account_id=None):
        """
        Заполняет дерево счетов данными, включая балансы.
        Принимает словарь данных от контроллера.
        """
        self.account_model.clear()
        self.account_model.setHorizontalHeaderLabels(['Name', 'Balance'])

        account_map = {}
        # Создаем все элементы дерева
        for acc_id, acc_data in accounts_data.items():
            account_map[acc_id] = QStandardItem(acc_data['name'])

        # Строим иерархию и добавляем балансы
        for acc_id, item in account_map.items():
            acc_data = accounts_data[acc_id]
            
            balance_strings = []
            for balance, currency_code in acc_data['balances']:
                balance_strings.append(f"{balance:.2f} {currency_code}")
            
            balance_item = QStandardItem(", ".join(balance_strings))
            
            item.setData(acc_id, Qt.ItemDataRole.UserRole)
            
            if acc_data['parent'] is None:
                self.account_model.appendRow([item, balance_item])
            elif acc_data['parent'] in account_map:
                parent_item = account_map[acc_data['parent']]
                parent_item.appendRow([item, balance_item])

        self.account_view.expandAll()
        self.account_view.resizeColumnToContents(0)

        # Восстанавливаем выбранный элемент
        if current_account_id is not None:
            index = self.find_item_index_by_id(self.account_model, current_account_id)
            if index:
                self.account_view.setCurrentIndex(index)
                
    def update_transaction_table(self, transactions, current_trans_id=None):
        """Заполняет таблицу транзакций."""
        self.transaction_model.clear()
        self.transaction_model.setHorizontalHeaderLabels(['ID', 'Date', 'Description', 'Amount', 'Balance', 'Currency'])
        for trans_id, date, desc, amount, balance, currency_code in transactions:
            row = [
                QStandardItem(trans_id),
                QStandardItem(date),
                QStandardItem(desc),
                QStandardItem(amount),
                QStandardItem(balance),
                QStandardItem(currency_code)
            ]

            row[3].setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter) # amount
            row[4].setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter) # balance
            for column in (0, 3, 4, 5): # ID, amount, balance, currency:
                row[column].setFlags(row[column].flags() & ~Qt.ItemFlag.ItemIsEditable)
            self.transaction_model.appendRow(row)
            
        self.transaction_table.resizeColumnsToContents()
        self.transaction_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Interactive)
        
        # Восстанавливаем выбранный элемент
        if current_trans_id is not None:
            index = self.find_item_index_by_id(self.transaction_model, current_trans_id)
            if index:
                self.transaction_table.setCurrentIndex(index)

    def update_split_table(self, splits, accounts_map, currencies_map):
        """Заполняет таблицу сплитов."""
        self.split_model.clear()
        self.split_model.setHorizontalHeaderLabels(['ID', 'External ID', 'Description', 'Account' , 'Amount', 'Currency', 'Fixed'])
        for split_id, desc, account_id, ext_id, amount, currency_id, amnt_fix in splits:
            row = [
                QStandardItem(str(split_id)),
                QStandardItem(ext_id),
                QStandardItem(desc),
                QStandardItem(accounts_map.get(account_id, "N/A")),
                QStandardItem(amount),
                QStandardItem(currencies_map.get(currency_id, "N/A")),
                QStandardItem('') # Checkbox column
            ]
            #row[0].setData(split_id, Qt.ItemDataRole.UserRole)
            row[0].setFlags(row[0].flags() & ~Qt.ItemFlag.ItemIsEditable)
            row[4].setTextAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter) # amount
            # Настройка флажка для amnt_fix
            checkbox_item = row[6]
            checkbox_item.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsUserCheckable)
            checkbox_item.setCheckState(Qt.CheckState.Checked if amnt_fix else Qt.CheckState.Unchecked)
            
            self.split_model.appendRow(row)

        self.split_table.resizeColumnsToContents()
        
    def find_item_index_by_id(self, model, item_id):
        """Вспомогательный метод для поиска индекса по ID в модели."""
        for row in range(model.rowCount()):
            for col in range(model.columnCount()):
                index = model.index(row, col)
                if index.data(Qt.ItemDataRole.UserRole) == item_id:
                    return index
        return None
