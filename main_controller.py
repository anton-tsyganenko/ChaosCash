from PyQt6.QtCore import Qt, QTimer #, QModelIndex
#from PyQt6.QtGui import QStandardItemModel, QStandardItem
from main_view import MainWindowView
from db import Database
from delegates import DateDelegate, ComboBoxDelegate
from math import ceil, log10

class MainController:
    """
    Класс, отвечающий за логику приложения.
    Связывает View (MainWindowView) и Model (Database).
    """
    def __init__(self, db):
        self.db = db
        self.view = MainWindowView()
        self.current_account_id = None
        self.current_trans_id = None
        
        # Получаем данные для делегатов
        self.accounts_list = self.db.get_accounts()
        self.accounts_map_id_to_name = {acc[0]: acc[2] for acc in self.accounts_list}
        self.accounts_map_name_to_id = {acc[2]: acc[0] for acc in self.accounts_list}

        self.currencies = self.db.get_all_currencies()
        self.currency_map_code_to_id = {c[1]: c[0] for c in self.currencies}
        self.currency_map_id_to_code = {c[0]: c[1] for c in self.currencies}
        self.currency_codes = [c[1] for c in self.currencies]
        
        # Устанавливаем делегаты
        self.setup_delegates()
        
        # Соединяем сигналы View с методами контроллера
        self.connect_signals()
        
        # Инициализируем UI
        self.update_ui_after_edit()

    def show_view(self):
        """Отображает главное окно."""
        self.view.show()

    def setup_delegates(self):
        """Устанавливает делегаты для таблиц в View."""
        self.date_delegate = DateDelegate()
        self.account_delegate = ComboBoxDelegate(self.view, self.accounts_map_id_to_name.values(), self.accounts_map_name_to_id)
        self.currency_delegate = ComboBoxDelegate(self.view, self.currency_codes, self.currency_map_code_to_id)

        self.view.transaction_table.setItemDelegateForColumn(1, self.date_delegate) # Date
        self.view.split_table.setItemDelegateForColumn(1, self.account_delegate) # Account
        self.view.split_table.setItemDelegateForColumn(5, self.currency_delegate) # Currency
        
    def connect_signals(self):
        """Соединяет сигналы из View с методами контроллера."""
        self.view.account_selected.connect(self.on_account_selected)
        self.view.transaction_selected.connect(self.on_transaction_selected)
        self.view.transaction_data_changed.connect(self.on_transaction_data_changed)
        self.view.split_data_changed.connect(self.on_split_data_changed)

    def update_ui_after_edit(self, split_id=None, trans_id=None):
        """
        Полностью обновляет таблицы с сохранением активного выбора.
        """
        if split_id is not None and trans_id is None:
            split_data = self.db.get_splits_by_id(split_id)
            if split_data:
                trans_id = split_data[1]

        # Обрабатываем данные, полученные от базы, для правильного отображения
        accounts_data = self.db.get_accounts_with_balances()
        processed_accounts = {}
        for acc_id, parent_id, name, balance, currency_code, denominator in accounts_data:
            if acc_id not in processed_accounts:
                processed_accounts[acc_id] = {
                    'parent': parent_id,
                    'name': name,
                    'balances': []
                }
            if balance is not None:
                processed_accounts[acc_id]['balances'].append(
                    (balance / denominator, currency_code)
                )

        self.view.update_account_tree(processed_accounts)

        # Если был выбран счет, обновляем таблицы
        if self.current_account_id:
            self.on_account_selected(self.current_account_id)
        if self.current_trans_id:
            self.on_transaction_selected(self.current_trans_id)

    def on_account_selected(self, account_id):
        """Обрабатывает выбор счета в дереве."""
        self.current_account_id = account_id
        self.current_trans_id = None
        self.populate_transactions_table(account_id)
        
    def populate_transactions_table(self, account_id):
        transactions = [
            (str(trans_id), date, desc,
            f"{amount:,.{ceil(log10(denom))}f}",
            f"{balance:,.{ceil(log10(denom))}f}",
            curr)
            for (trans_id, date, desc, amount, balance, curr, denom)
            in self.db.get_transactions_by_account_with_balance(account_id)
        ]
        self.view.update_transaction_table(transactions)
        
    def on_transaction_selected(self, trans_id):
        """Обрабатывает выбор транзакции в таблице."""
        self.current_trans_id = trans_id
        splits = self.db.get_splits_by_transaction(trans_id)
        self.view.update_split_table(splits, self.accounts_map_id_to_name, self.currency_map_id_to_code)

    def on_transaction_data_changed(self, top_left, bottom_right):
        """Обрабатывает изменения в таблице транзакций."""
        if top_left.column() == 0:  # Column 'ID'
            return # Don't update
        
        row = top_left.row()
        trans_id = self.view.transaction_model.index(row, 0).data(Qt.ItemDataRole.UserRole)
        date_str = self.view.transaction_model.index(row, 1).data(Qt.ItemDataRole.DisplayRole)
        desc = self.view.transaction_model.index(row, 2).data(Qt.ItemDataRole.DisplayRole)

        if self.db.update_transaction(trans_id, date_str, desc):
            QTimer.singleShot(0, lambda: self.update_ui_after_edit(trans_id=trans_id))

    def on_split_data_changed(self, top_left, bottom_right):
        """Обрабатывает изменения в таблице сплитов."""
        row = top_left.row()
        split_id = self.view.split_model.index(row, 0).data(Qt.ItemDataRole.UserRole)
        
        # Получаем данные из модели
        account_name = self.view.split_model.index(row, 1).data(Qt.ItemDataRole.DisplayRole)
        account_id = self.accounts_map_name_to_id.get(account_name)
        
        desc = self.view.split_model.index(row, 2).data(Qt.ItemDataRole.DisplayRole)
        ext_id = self.view.split_model.index(row, 3).data(Qt.ItemDataRole.DisplayRole)
        amount_str = self.view.split_model.index(row, 4).data(Qt.ItemDataRole.DisplayRole)
        amount = float(amount_str.replace(',', '.'))
        
        currency_code = self.view.split_model.index(row, 5).data(Qt.ItemDataRole.DisplayRole)
        currency_id = self.currency_map_code_to_id.get(currency_code)

        amnt_fix_state = self.view.split_model.index(row, 6).checkState()
        amnt_fix = amnt_fix_state == Qt.CheckState.Checked

        denominator = 1
        for c_id, _, _, den in self.currencies:
            if c_id == currency_id:
                denominator = den
                break

        if split_id is None:
            new_split_id = self.db.add_split(self.current_trans_id, account_id, desc, ext_id, int(amount * denominator), currency_id, amnt_fix)
            if new_split_id:
                self.update_ui_after_edit(split_id=new_split_id)
        else:
            if self.db.update_split(split_id, account_id, desc, ext_id, int(amount * denominator), currency_id, amnt_fix):
                self.update_ui_after_edit(split_id=split_id)
