# PyQt Сигналы, Слоты и Соединения

*Дата создания: 2026-02-28*

## Статистика

- **Найдено .connect() соединений:** 93
- **Найдено PyQt-декораторов:** 0
- **Файлов с соединениями:** 18
- **Файлов с декораторами:** 0

## Signal-Slot соединения (.connect)

### app/database/connection.py

Соединений: 1

**Строка 5:**

- **Сигнал:** `sqlite3`
- **Слот:** `db_path`
- **Тип:** connect

```python
    conn = sqlite3.connect(db_path)
```

### app/ui/account_selection.py

Соединений: 1

**Строка 38:**

- **Сигнал:** `items.sort`
- **Слот:** `lambda`
- **Тип:** lambda

```python
    items.sort(key=lambda x: x[0].lower())
```

### app/ui/dialogs/currency_editor_dialog.py

Соединений: 4

**Строка 44:**

- **Сигнал:** `self.btn_add.clicked`
- **Слот:** `self._add_row`
- **Тип:** connect

```python
        self.btn_add.clicked.connect(self._add_row)
```

**Строка 45:**

- **Сигнал:** `self.btn_delete.clicked`
- **Слот:** `self._delete_row`
- **Тип:** connect

```python
        self.btn_delete.clicked.connect(self._delete_row)
```

**Строка 53:**

- **Сигнал:** `buttons.accepted`
- **Слот:** `self._save`
- **Тип:** connect

```python
        buttons.accepted.connect(self._save)
```

**Строка 54:**

- **Сигнал:** `buttons.rejected`
- **Слот:** `self.reject`
- **Тип:** connect

```python
        buttons.rejected.connect(self.reject)
```

### app/ui/dialogs/delete_account_dialog.py

Соединений: 16

**Строка 105:**

- **Сигнал:** `self.rb_move_subaccounts.toggled`
- **Слот:** `lambda checked: self.subaccounts_combo.setEnabled(checked`
- **Тип:** connect

```python
            self.rb_move_subaccounts.toggled.connect(lambda checked: self.subaccounts_combo.setEnabled(checked))
```

**Строка 105:**

- **Сигнал:** `self.rb_move_subaccounts.toggled.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
            self.rb_move_subaccounts.toggled.connect(lambda checked: self.subaccounts_combo.setEnabled(checked))
```

**Строка 106:**

- **Сигнал:** `self.rb_delete_recursive.toggled`
- **Слот:** `lambda checked: self.subaccounts_combo.setEnabled(not checked`
- **Тип:** connect

```python
            self.rb_delete_recursive.toggled.connect(lambda checked: self.subaccounts_combo.setEnabled(not checked))
```

**Строка 106:**

- **Сигнал:** `self.rb_delete_recursive.toggled.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
            self.rb_delete_recursive.toggled.connect(lambda checked: self.subaccounts_combo.setEnabled(not checked))
```

**Строка 108:**

- **Сигнал:** `self.rb_move_subaccounts.toggled`
- **Слот:** `self._update_transactions_combo`
- **Тип:** connect

```python
            self.rb_move_subaccounts.toggled.connect(self._update_transactions_combo)
```

**Строка 109:**

- **Сигнал:** `self.rb_delete_recursive.toggled`
- **Слот:** `self._update_transactions_combo`
- **Тип:** connect

```python
            self.rb_delete_recursive.toggled.connect(self._update_transactions_combo)
```

**Строка 142:**

- **Сигнал:** `self.rb_move_splits.toggled`
- **Слот:** `lambda checked: self.transactions_combo.setEnabled(checked`
- **Тип:** connect

```python
            self.rb_move_splits.toggled.connect(lambda checked: self.transactions_combo.setEnabled(checked))
```

**Строка 142:**

- **Сигнал:** `self.rb_move_splits.toggled.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
            self.rb_move_splits.toggled.connect(lambda checked: self.transactions_combo.setEnabled(checked))
```

**Строка 143:**

- **Сигнал:** `self.rb_delete_splits.toggled`
- **Слот:** `lambda checked: self.transactions_combo.setEnabled(not checked`
- **Тип:** connect

```python
            self.rb_delete_splits.toggled.connect(lambda checked: self.transactions_combo.setEnabled(not checked))
```

**Строка 143:**

- **Сигнал:** `self.rb_delete_splits.toggled.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
            self.rb_delete_splits.toggled.connect(lambda checked: self.transactions_combo.setEnabled(not checked))
```

**Строка 144:**

- **Сигнал:** `self.rb_delete_trans.toggled`
- **Слот:** `lambda checked: self.transactions_combo.setEnabled(not checked`
- **Тип:** connect

```python
            self.rb_delete_trans.toggled.connect(lambda checked: self.transactions_combo.setEnabled(not checked))
```

**Строка 144:**

- **Сигнал:** `self.rb_delete_trans.toggled.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
            self.rb_delete_trans.toggled.connect(lambda checked: self.transactions_combo.setEnabled(not checked))
```

**Строка 153:**

- **Сигнал:** `buttons.accepted`
- **Слот:** `self._accept`
- **Тип:** connect

```python
        buttons.accepted.connect(self._accept)
```

**Строка 154:**

- **Сигнал:** `buttons.rejected`
- **Слот:** `self.reject`
- **Тип:** connect

```python
        buttons.rejected.connect(self.reject)
```

**Строка 158:**

- **Сигнал:** `self.rb_hide.toggled`
- **Слот:** `self._on_action_changed`
- **Тип:** connect

```python
        self.rb_hide.toggled.connect(self._on_action_changed)
```

**Строка 159:**

- **Сигнал:** `self.rb_delete.toggled`
- **Слот:** `self._on_action_changed`
- **Тип:** connect

```python
        self.rb_delete.toggled.connect(self._on_action_changed)
```

### app/ui/dialogs/settings_dialog.py

Соединений: 2

**Строка 51:**

- **Сигнал:** `buttons.accepted`
- **Слот:** `self._save_and_accept`
- **Тип:** connect

```python
        buttons.accepted.connect(self._save_and_accept)
```

**Строка 52:**

- **Сигнал:** `buttons.rejected`
- **Слот:** `self.reject`
- **Тип:** connect

```python
        buttons.rejected.connect(self.reject)
```

### app/ui/item_models/account_tree_model.py

Соединений: 1

**Строка 90:**

- **Сигнал:** `parent.children.sort`
- **Слот:** `lambda`
- **Тип:** lambda

```python
            parent.children.sort(key=lambda n: (n.account.name or "").lower())
```

### app/ui/item_models/transaction_model.py

Соединений: 1

**Строка 234:**

- **Сигнал:** `QTimer.singleShot`
- **Слот:** `lambda`
- **Тип:** lambda

```python
                QTimer.singleShot(0, lambda d=desc, t=now_utc: self.new_transaction_requested.emit(d, t))
```

### app/ui/main_window.py

Соединений: 34

**Строка 167:**

- **Сигнал:** `new_action.triggered`
- **Слот:** `self._new_file`
- **Тип:** connect

```python
        new_action.triggered.connect(self._new_file)
```

**Строка 172:**

- **Сигнал:** `open_action.triggered`
- **Слот:** `self._open_file`
- **Тип:** connect

```python
        open_action.triggered.connect(self._open_file)
```

**Строка 183:**

- **Сигнал:** `add_acc_action.triggered`
- **Слот:** `lambda: self.account_tree._add_account(QModelIndex(`
- **Тип:** connect

```python
        add_acc_action.triggered.connect(lambda: self.account_tree._add_account(QModelIndex()))
```

**Строка 183:**

- **Сигнал:** `add_acc_action.triggered.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
        add_acc_action.triggered.connect(lambda: self.account_tree._add_account(QModelIndex()))
```

**Строка 189:**

- **Сигнал:** `close_action.triggered`
- **Слот:** `self.close`
- **Тип:** connect

```python
        close_action.triggered.connect(self.close)
```

**Строка 198:**

- **Сигнал:** `self.act_show_hidden.toggled`
- **Слот:** `self._toggle_show_hidden`
- **Тип:** connect

```python
        self.act_show_hidden.toggled.connect(self._toggle_show_hidden)
```

**Строка 204:**

- **Сигнал:** `self.act_allow_grouping_for_splits.toggled`
- **Слот:** `self._toggle_allow_grouping_for_splits`
- **Тип:** connect

```python
        self.act_allow_grouping_for_splits.toggled.connect(self._toggle_allow_grouping_for_splits)
```

**Строка 221:**

- **Сигнал:** `self.act_detailed.triggered`
- **Слот:** `lambda: self._set_view_mode("detailed"`
- **Тип:** connect

```python
        self.act_detailed.triggered.connect(lambda: self._set_view_mode("detailed"))
```

**Строка 221:**

- **Сигнал:** `self.act_detailed.triggered.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
        self.act_detailed.triggered.connect(lambda: self._set_view_mode("detailed"))
```

**Строка 222:**

- **Сигнал:** `self.act_aggregated.triggered`
- **Слот:** `lambda: self._set_view_mode("aggregated"`
- **Тип:** connect

```python
        self.act_aggregated.triggered.connect(lambda: self._set_view_mode("aggregated"))
```

**Строка 222:**

- **Сигнал:** `self.act_aggregated.triggered.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
        self.act_aggregated.triggered.connect(lambda: self._set_view_mode("aggregated"))
```

**Строка 230:**

- **Сигнал:** `currencies_action.triggered`
- **Слот:** `self._open_currency_editor`
- **Тип:** connect

```python
        currencies_action.triggered.connect(self._open_currency_editor)
```

**Строка 234:**

- **Сигнал:** `settings_action.triggered`
- **Слот:** `self._open_settings`
- **Тип:** connect

```python
        settings_action.triggered.connect(self._open_settings)
```

**Строка 311:**

- **Сигнал:** `self.account_tree.account_selected`
- **Слот:** `self._on_accounts_selected`
- **Тип:** connect

```python
        self.account_tree.account_selected.connect(self._on_accounts_selected)
```

**Строка 312:**

- **Сигнал:** `self.account_tree.virtual_node_selected`
- **Слот:** `self._on_virtual_node_selected`
- **Тип:** connect

```python
        self.account_tree.virtual_node_selected.connect(self._on_virtual_node_selected)
```

**Строка 313:**

- **Сигнал:** `self.account_tree.enter_pressed`
- **Слот:** `self._focus_transactions`
- **Тип:** connect

```python
        self.account_tree.enter_pressed.connect(self._focus_transactions)
```

**Строка 314:**

- **Сигнал:** `self.transaction_view.transaction_selected`
- **Слот:** `self._on_transaction_selected`
- **Тип:** connect

```python
        self.transaction_view.transaction_selected.connect(self._on_transaction_selected)
```

**Строка 315:**

- **Сигнал:** `self.transaction_view.transactions_changed`
- **Слот:** `self._on_transactions_changed`
- **Тип:** connect

```python
        self.transaction_view.transactions_changed.connect(self._on_transactions_changed)
```

**Строка 316:**

- **Сигнал:** `self.transaction_view.transaction_cleared`
- **Слот:** `self._on_transaction_cleared`
- **Тип:** connect

```python
        self.transaction_view.transaction_cleared.connect(self._on_transaction_cleared)
```

**Строка 317:**

- **Сигнал:** `self.transaction_view.enter_pressed`
- **Слот:** `self._focus_current_transaction_splits`
- **Тип:** connect

```python
        self.transaction_view.enter_pressed.connect(self._focus_current_transaction_splits)
```

**Строка 318:**

- **Сигнал:** `self.transaction_view.escape_pressed`
- **Слот:** `self._focus_accounts`
- **Тип:** connect

```python
        self.transaction_view.escape_pressed.connect(self._focus_accounts)
```

**Строка 319:**

- **Сигнал:** `self.split_view.split_changed`
- **Слот:** `self._on_split_changed`
- **Тип:** connect

```python
        self.split_view.split_changed.connect(self._on_split_changed)
```

**Строка 320:**

- **Сигнал:** `self.split_view.escape_pressed`
- **Слот:** `self._focus_transactions`
- **Тип:** connect

```python
        self.split_view.escape_pressed.connect(self._focus_transactions)
```

**Строка 323:**

- **Сигнал:** `self.split_model.dataChanged`
- **Слот:** `self._on_split_data_changed`
- **Тип:** connect

```python
        self.split_model.dataChanged.connect(self._on_split_data_changed)
```

**Строка 324:**

- **Сигнал:** `self.trans_model.dataChanged`
- **Слот:** `self._on_trans_data_changed`
- **Тип:** connect

```python
        self.trans_model.dataChanged.connect(self._on_trans_data_changed)
```

**Строка 325:**

- **Сигнал:** `self.trans_model.new_transaction_requested`
- **Слот:** `self._on_new_transaction_requested`
- **Тип:** connect

```python
        self.trans_model.new_transaction_requested.connect(self._on_new_transaction_requested)
```

**Строка 368:**

- **Сигнал:** `QTimer.singleShot`
- **Слот:** `lambda`
- **Тип:** lambda

```python
        QTimer.singleShot(0, lambda: self._focus_split_cell(0, COL_AMOUNT))
```

**Строка 651:**

- **Сигнал:** `QTimer.singleShot`
- **Слот:** `lambda`
- **Тип:** lambda

```python
            QTimer.singleShot(0, lambda row=r, col=c: self._focus_split_cell(row, col))
```

**Строка 695:**

- **Сигнал:** `QTimer.singleShot`
- **Слот:** `lambda`
- **Тип:** lambda

```python
                    QTimer.singleShot(0, lambda: self._on_split_changed(force=True))
```

**Строка 718:**

- **Сигнал:** `QTimer.singleShot`
- **Слот:** `lambda`
- **Тип:** lambda

```python
                    QTimer.singleShot(0, lambda: self._on_split_changed(force=True))
```

**Строка 744:**

- **Сигнал:** `QTimer.singleShot`
- **Слот:** `lambda`
- **Тип:** lambda

```python
                QTimer.singleShot(0, lambda: self._on_split_changed(force=True))
```

**Строка 804:**

- **Сигнал:** `QTimer.singleShot`
- **Слот:** `lambda`
- **Тип:** lambda

```python
        QTimer.singleShot(0, lambda: self._on_split_changed(force=True))
```

**Строка 838:**

- **Сигнал:** `action.triggered`
- **Слот:** `lambda checked, p=path: self._open_file_path(p`
- **Тип:** connect

```python
            action.triggered.connect(lambda checked, p=path: self._open_file_path(p))
```

**Строка 838:**

- **Сигнал:** `action.triggered.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
            action.triggered.connect(lambda checked, p=path: self._open_file_path(p))
```

### app/ui/ui_event_logger.py

Соединений: 1

**Строка 25:**

- **Сигнал:** `app.focusChanged`
- **Слот:** `self._on_focus_changed`
- **Тип:** connect

```python
        app.focusChanged.connect(self._on_focus_changed)
```

### app/ui/widgets/account_tree_view.py

Соединений: 8

**Строка 40:**

- **Сигнал:** `self.customContextMenuRequested`
- **Слот:** `self._show_context_menu`
- **Тип:** connect

```python
        self.customContextMenuRequested.connect(self._show_context_menu)
```

**Строка 41:**

- **Сигнал:** `self.clicked`
- **Слот:** `self._on_clicked`
- **Тип:** connect

```python
        self.clicked.connect(self._on_clicked)
```

**Строка 47:**

- **Сигнал:** `header.customContextMenuRequested`
- **Слот:** `self._show_header_menu`
- **Тип:** connect

```python
        header.customContextMenuRequested.connect(self._show_header_menu)
```

**Строка 54:**

- **Сигнал:** `selectionChanged`
- **Слот:** `self._on_selection_changed`
- **Тип:** connect

```python
            self.selectionModel().selectionChanged.connect(self._on_selection_changed)
```

**Строка 169:**

- **Сигнал:** `add_action.triggered`
- **Слот:** `lambda: self._add_account(index if index.isValid(`
- **Тип:** connect

```python
        add_action.triggered.connect(lambda: self._add_account(index if index.isValid() else QModelIndex()))
```

**Строка 169:**

- **Сигнал:** `add_action.triggered.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
        add_action.triggered.connect(lambda: self._add_account(index if index.isValid() else QModelIndex()))
```

**Строка 177:**

- **Сигнал:** `del_action.triggered`
- **Слот:** `lambda: self._delete_account(index`
- **Тип:** connect

```python
                del_action.triggered.connect(lambda: self._delete_account(index))
```

**Строка 177:**

- **Сигнал:** `del_action.triggered.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
                del_action.triggered.connect(lambda: self._delete_account(index))
```

### app/ui/widgets/split_view.py

Соединений: 4

**Строка 32:**

- **Сигнал:** `self.customContextMenuRequested`
- **Слот:** `self._show_context_menu`
- **Тип:** connect

```python
        self.customContextMenuRequested.connect(self._show_context_menu)
```

**Строка 37:**

- **Сигнал:** `header.customContextMenuRequested`
- **Слот:** `self._show_header_menu`
- **Тип:** connect

```python
        header.customContextMenuRequested.connect(self._show_header_menu)
```

**Строка 111:**

- **Сигнал:** `del_action.triggered`
- **Слот:** `lambda: self._delete_split(split.id`
- **Тип:** connect

```python
        del_action.triggered.connect(lambda: self._delete_split(split.id))
```

**Строка 111:**

- **Сигнал:** `del_action.triggered.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
        del_action.triggered.connect(lambda: self._delete_split(split.id))
```

### app/ui/widgets/transaction_view.py

Соединений: 10

**Строка 34:**

- **Сигнал:** `self.customContextMenuRequested`
- **Слот:** `self._show_context_menu`
- **Тип:** connect

```python
        self.customContextMenuRequested.connect(self._show_context_menu)
```

**Строка 35:**

- **Сигнал:** `self.clicked`
- **Слот:** `self._on_clicked`
- **Тип:** connect

```python
        self.clicked.connect(self._on_clicked)
```

**Строка 40:**

- **Сигнал:** `header.customContextMenuRequested`
- **Слот:** `self._show_header_menu`
- **Тип:** connect

```python
        header.customContextMenuRequested.connect(self._show_header_menu)
```

**Строка 48:**

- **Сигнал:** `currentRowChanged`
- **Слот:** `self._on_current_row_changed`
- **Тип:** connect

```python
            self.selectionModel().currentRowChanged.connect(self._on_current_row_changed)
```

**Строка 135:**

- **Сигнал:** `dup_action.triggered`
- **Слот:** `lambda: self._duplicate(trans_id`
- **Тип:** connect

```python
        dup_action.triggered.connect(lambda: self._duplicate(trans_id))
```

**Строка 135:**

- **Сигнал:** `dup_action.triggered.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
        dup_action.triggered.connect(lambda: self._duplicate(trans_id))
```

**Строка 139:**

- **Сигнал:** `rev_action.triggered`
- **Слот:** `lambda: self._reverse(trans_id`
- **Тип:** connect

```python
        rev_action.triggered.connect(lambda: self._reverse(trans_id))
```

**Строка 139:**

- **Сигнал:** `rev_action.triggered.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
        rev_action.triggered.connect(lambda: self._reverse(trans_id))
```

**Строка 145:**

- **Сигнал:** `del_action.triggered`
- **Слот:** `lambda: self._delete(trans_id`
- **Тип:** connect

```python
        del_action.triggered.connect(lambda: self._delete(trans_id))
```

**Строка 145:**

- **Сигнал:** `del_action.triggered.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
        del_action.triggered.connect(lambda: self._delete(trans_id))
```

### app/ui/widgets/view_helpers.py

Соединений: 2

**Строка 44:**

- **Сигнал:** `action.toggled`
- **Слот:** `lambda checked, col=logical: set_column_visibility(view, col, checked`
- **Тип:** connect

```python
        action.toggled.connect(lambda checked, col=logical: set_column_visibility(view, col, checked))
```

**Строка 44:**

- **Сигнал:** `action.toggled.connect`
- **Слот:** `lambda`
- **Тип:** lambda

```python
        action.toggled.connect(lambda checked, col=logical: set_column_visibility(view, col, checked))
```

### extract_qt_connections.py

Соединений: 2

**Строка 79:**

- **Сигнал:** `re.search`
- **Слот:** `lambda`
- **Тип:** lambda

```python
                    match = re.search(r'(\w+(?:\.\w+)*)\s*\.(\w+)\s*\(.*?lambda.*?\)', line)
```

**Строка 253:**

- **Сигнал:** `signal_counts.items`
- **Слот:** `lambda`
- **Тип:** lambda

```python
        for signal, count in sorted(signal_counts.items(), key=lambda x: -x[1])[:15]:
```

### main.py

Соединений: 3

**Строка 100:**

- **Сигнал:** `btn_open.clicked`
- **Слот:** `self._open`
- **Тип:** connect

```python
            btn_open.clicked.connect(self._open)
```

**Строка 101:**

- **Сигнал:** `btn_new.clicked`
- **Слот:** `self._new`
- **Тип:** connect

```python
            btn_new.clicked.connect(self._new)
```

**Строка 102:**

- **Сигнал:** `btn_cancel.clicked`
- **Слот:** `self.reject`
- **Тип:** connect

```python
            btn_cancel.clicked.connect(self.reject)
```

### tests/test_balance_service.py

Соединений: 1

**Строка 19:**

- **Сигнал:** `sqlite3`
- **Слот:** `":memory:"`
- **Тип:** connect

```python
    conn = sqlite3.connect(":memory:")
```

### tests/test_integrity_service.py

Соединений: 1

**Строка 18:**

- **Сигнал:** `sqlite3`
- **Слот:** `":memory:"`
- **Тип:** connect

```python
    conn = sqlite3.connect(":memory:")
```

### tests/test_transaction_service.py

Соединений: 1

**Строка 18:**

- **Сигнал:** `sqlite3`
- **Слот:** `":memory:"`
- **Тип:** connect

```python
    conn = sqlite3.connect(":memory:")
```

---

## PyQt Декораторы (@pyqtSlot, @Slot, @Signal)

PyQt-декораторы не найдены.

---

## Анализ часто используемых сигналов

### Самые часто используемые сигналы:

- `connect` — 16 использований
- `triggered` — 15 использований
- `toggled` — 12 использований
- `clicked` — 7 использований
- `singleShot` — 7 использований
- `customContextMenuRequested` — 6 использований
- `sqlite3` — 4 использований
- `accepted` — 3 использований
- `rejected` — 3 использований
- `sort` — 2 использований
- `enter_pressed` — 2 использований
- `escape_pressed` — 2 использований
- `dataChanged` — 2 использований
- `account_selected` — 1 использований
- `virtual_node_selected` — 1 использований
