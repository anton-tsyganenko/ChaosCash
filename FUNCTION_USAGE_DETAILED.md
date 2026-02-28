# Подробная документация использования функций и методов

*Дата создания: 2026-02-28*
*Проект: ChaosCash*

---

## Оглавление

1. [Статистика](#статистика)
2. [Qt сигналы и слоты](#qt-сигналы-и-слоты)
3. [Функции и методы](#функции-и-методы)
4. [Неиспользуемые функции](#неиспользуемые-функции)

---

## Статистика

- **Всего функций/методов:** 401
- **Qt соединений обнаружено:** 0
- **Неиспользуемые функции:** 165
- **Анализировано файлов:** 66

---

---

## Функции и методы

### По типам

#### Function (74)

- _apply_pragmas
- _ask_file_path
- _configure_logging
- _eval_node
- _make_virtual_account
- _parse_args
- _row_to_account
- _row_to_currency
- _row_to_split
- _row_to_trans
- _utc_now
- add_recent_file
- analyze_codebase
- analyze_file
- analyze_file_detailed
- balance_service
- compute_hidden_account_ids
- db
- ensure_schema
- find_all_usages_with_context
- ... и ещё 54

#### Method (327)

- AccountComboDelegate.__init__
- AccountComboDelegate._get_items
- AccountNode.is_virtual
- AccountRepo.__init__
- AccountRepo.delete
- AccountRepo.get_account_path
- AccountRepo.get_all
- AccountRepo.get_all_descendants
- AccountRepo.get_balance
- AccountRepo.get_by_id
- AccountRepo.get_children
- AccountRepo.get_parent_id
- AccountRepo.get_transaction_ids_for_account
- AccountRepo.insert
- AccountRepo.move_splits_to_account
- AccountRepo.update
- AccountRepo.update_hidden
- AccountRepo.update_parent
- AccountTreeModel.__init__
- AccountTreeModel._add_virtual_nodes
- ... и ещё 307

### Детальный список

#### AccountComboDelegate.__init__

**Определено в:** `app/ui/delegates/account_combo_delegate.py:11`

**Тип:** method

**Сигнатура:** `AccountComboDelegate.__init__(self, account_repo, settings, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### AccountComboDelegate._get_items

**Определено в:** `app/ui/delegates/account_combo_delegate.py:16`

**Тип:** method

**Сигнатура:** `AccountComboDelegate._get_items(self)`

**Использования (1 мест):**


#### AccountNode.is_virtual

**Определено в:** `app/ui/item_models/account_tree_model.py:37`

**Тип:** method

**Сигнатура:** `AccountNode.is_virtual(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AccountRepo.__init__

**Определено в:** `app/repositories/account_repo.py:19`

**Тип:** method

**Сигнатура:** `AccountRepo.__init__(self, conn, settings)`

**Использования (17 мест):**

- ... и ещё 7

#### AccountRepo.delete

**Определено в:** `app/repositories/account_repo.py:58`

**Тип:** method

**Сигнатура:** `AccountRepo.delete(self, account_id)`

**Использования (7 мест):**


#### AccountRepo.get_account_path

**Определено в:** `app/repositories/account_repo.py:84`

**Тип:** method

**Сигнатура:** `AccountRepo.get_account_path(self, account_id)`

**Использования (6 мест):**


#### AccountRepo.get_all

**Определено в:** `app/repositories/account_repo.py:23`

**Тип:** method

**Сигнатура:** `AccountRepo.get_all(self)`

**Использования (9 мест):**


#### AccountRepo.get_all_descendants

**Определено в:** `app/repositories/account_repo.py:75`

**Тип:** method

**Сигнатура:** `AccountRepo.get_all_descendants(self, account_id)`

**Использования (7 мест):**


#### AccountRepo.get_balance

**Определено в:** `app/repositories/account_repo.py:62`

**Тип:** method

**Сигнатура:** `AccountRepo.get_balance(self, account_id)`

**Использования (7 мест):**


#### AccountRepo.get_by_id

**Определено в:** `app/repositories/account_repo.py:27`

**Тип:** method

**Сигнатура:** `AccountRepo.get_by_id(self, account_id)`

**Использования (21 мест):**

- ... и ещё 11

#### AccountRepo.get_children

**Определено в:** `app/repositories/account_repo.py:31`

**Тип:** method

**Сигнатура:** `AccountRepo.get_children(self, account_id)`

**Использования (6 мест):**


#### AccountRepo.get_parent_id

**Определено в:** `app/repositories/account_repo.py:35`

**Тип:** method

**Сигнатура:** `AccountRepo.get_parent_id(self, account_id)`

**Использования (3 мест):**


#### AccountRepo.get_transaction_ids_for_account

**Определено в:** `app/repositories/account_repo.py:71`

**Тип:** method

**Сигнатура:** `AccountRepo.get_transaction_ids_for_account(self, account_id)`

**Использования (1 мест):**


#### AccountRepo.insert

**Определено в:** `app/repositories/account_repo.py:39`

**Тип:** method

**Сигнатура:** `AccountRepo.insert(self, parent, name, code, description, external_id, is_hidden)`

**Использования (73 мест):**

- ... и ещё 63

#### AccountRepo.move_splits_to_account

**Определено в:** `app/repositories/account_repo.py:67`

**Тип:** method

**Сигнатура:** `AccountRepo.move_splits_to_account(self, from_account_id, to_account_id)`

**Использования (1 мест):**


#### AccountRepo.update

**Определено в:** `app/repositories/account_repo.py:45`

**Тип:** method

**Сигнатура:** `AccountRepo.update(self, account_id, parent, name, code, description, external_id, is_hidden)`

**Использования (6 мест):**


#### AccountRepo.update_hidden

**Определено в:** `app/repositories/account_repo.py:54`

**Тип:** method

**Сигнатура:** `AccountRepo.update_hidden(self, account_id, is_hidden)`

**Использования (2 мест):**


#### AccountRepo.update_parent

**Определено в:** `app/repositories/account_repo.py:50`

**Тип:** method

**Сигнатура:** `AccountRepo.update_parent(self, account_id, new_parent)`

**Использования (2 мест):**


#### AccountTreeModel.__init__

**Определено в:** `app/ui/item_models/account_tree_model.py:44`

**Тип:** method

**Сигнатура:** `AccountTreeModel.__init__(self, account_repo, balance_service, currency_repo, settings, formatter, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### AccountTreeModel._add_virtual_nodes

**Определено в:** `app/ui/item_models/account_tree_model.py:96`

**Тип:** method

**Сигнатура:** `AccountTreeModel._add_virtual_nodes(self)`

**Использования (1 мест):**


#### AccountTreeModel._build_tree

**Определено в:** `app/ui/item_models/account_tree_model.py:69`

**Тип:** method

**Сигнатура:** `AccountTreeModel._build_tree(self)`

**Использования (1 мест):**


#### AccountTreeModel._format_balance

**Определено в:** `app/ui/item_models/account_tree_model.py:185`

**Тип:** method

**Сигнатура:** `AccountTreeModel._format_balance(self, account_id, include_children)`

**Использования (2 мест):**


#### AccountTreeModel._node_parent_index

**Определено в:** `app/ui/item_models/account_tree_model.py:276`

**Тип:** method

**Сигнатура:** `AccountTreeModel._node_parent_index(self, node)`

**Использования (1 мест):**


#### AccountTreeModel._remove_node_ids_recursive

**Определено в:** `app/ui/item_models/account_tree_model.py:297`

**Тип:** method

**Сигнатура:** `AccountTreeModel._remove_node_ids_recursive(self, node)`

**Использования (2 мест):**


#### AccountTreeModel._remove_node_subtree

**Определено в:** `app/ui/item_models/account_tree_model.py:286`

**Тип:** method

**Сигнатура:** `AccountTreeModel._remove_node_subtree(self, node)`

**Использования (1 мест):**


#### AccountTreeModel.columnCount

**Определено в:** `app/ui/item_models/account_tree_model.py:124`

**Тип:** method

**Сигнатура:** `AccountTreeModel.columnCount(self, parent)`

**Использования (13 мест):**

- ... и ещё 3

#### AccountTreeModel.data

**Определено в:** `app/ui/item_models/account_tree_model.py:147`

**Тип:** method

**Сигнатура:** `AccountTreeModel.data(self, index, role)`

**Использования (20 мест):**

- ... и ещё 10

#### AccountTreeModel.dropMimeData

**Определено в:** `app/ui/item_models/account_tree_model.py:321`

**Тип:** method

**Сигнатура:** `AccountTreeModel.dropMimeData(self, data, action, row, col, parent)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AccountTreeModel.flags

**Определено в:** `app/ui/item_models/account_tree_model.py:208`

**Тип:** method

**Сигнатура:** `AccountTreeModel.flags(self, index)`

**Использования (7 мест):**


#### AccountTreeModel.get_all_descendants

**Определено в:** `app/ui/item_models/account_tree_model.py:366`

**Тип:** method

**Сигнатура:** `AccountTreeModel.get_all_descendants(self, account_id, include_hidden)`

**Использования (7 мест):**


#### AccountTreeModel.get_index_for_account

**Определено в:** `app/ui/item_models/account_tree_model.py:359`

**Тип:** method

**Сигнатура:** `AccountTreeModel.get_index_for_account(self, account_id)`

**Использования (3 мест):**


#### AccountTreeModel.get_node

**Определено в:** `app/ui/item_models/account_tree_model.py:113`

**Тип:** method

**Сигнатура:** `AccountTreeModel.get_node(self, index)`

**Использования (10 мест):**


#### AccountTreeModel.get_node_by_account_id

**Определено в:** `app/ui/item_models/account_tree_model.py:356`

**Тип:** method

**Сигнатура:** `AccountTreeModel.get_node_by_account_id(self, account_id)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AccountTreeModel.headerData

**Определено в:** `app/ui/item_models/account_tree_model.py:199`

**Тип:** method

**Сигнатура:** `AccountTreeModel.headerData(self, section, orientation, role)`

**Использования (1 мест):**


#### AccountTreeModel.index

**Определено в:** `app/ui/item_models/account_tree_model.py:127`

**Тип:** method

**Сигнатура:** `AccountTreeModel.index(self, row, col, parent)`

**Использования (21 мест):**

- ... и ещё 11

#### AccountTreeModel.mimeData

**Определено в:** `app/ui/item_models/account_tree_model.py:309`

**Тип:** method

**Сигнатура:** `AccountTreeModel.mimeData(self, indexes)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AccountTreeModel.mimeTypes

**Определено в:** `app/ui/item_models/account_tree_model.py:306`

**Тип:** method

**Сигнатура:** `AccountTreeModel.mimeTypes(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AccountTreeModel.parent

**Определено в:** `app/ui/item_models/account_tree_model.py:135`

**Тип:** method

**Сигнатура:** `AccountTreeModel.parent(self, index)`

**Использования (4 мест):**


#### AccountTreeModel.reload

**Определено в:** `app/ui/item_models/account_tree_model.py:60`

**Тип:** method

**Сигнатура:** `AccountTreeModel.reload(self)`

**Использования (8 мест):**


#### AccountTreeModel.rowCount

**Определено в:** `app/ui/item_models/account_tree_model.py:118`

**Тип:** method

**Сигнатура:** `AccountTreeModel.rowCount(self, parent)`

**Использования (11 мест):**

- ... и ещё 1

#### AccountTreeModel.setData

**Определено в:** `app/ui/item_models/account_tree_model.py:221`

**Тип:** method

**Сигнатура:** `AccountTreeModel.setData(self, index, value, role)`

**Использования (8 мест):**


#### AccountTreeModel.set_virtual_nodes

**Определено в:** `app/ui/item_models/account_tree_model.py:106`

**Тип:** method

**Сигнатура:** `AccountTreeModel.set_virtual_nodes(self, has_imbalance, has_empty)`

**Использования (1 мест):**


#### AccountTreeModel.sort

**Определено в:** `app/ui/item_models/account_tree_model.py:324`

**Тип:** method

**Сигнатура:** `AccountTreeModel.sort(self, column, order)`

**Использования (5 мест):**


#### AccountTreeModel.sort_key

**Определено в:** `app/ui/item_models/account_tree_model.py:327`

**Тип:** method

**Сигнатура:** `AccountTreeModel.sort_key(n)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AccountTreeModel.sort_recursive

**Определено в:** `app/ui/item_models/account_tree_model.py:347`

**Тип:** method

**Сигнатура:** `AccountTreeModel.sort_recursive(node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AccountTreeModel.supportedDropActions

**Определено в:** `app/ui/item_models/account_tree_model.py:303`

**Тип:** method

**Сигнатура:** `AccountTreeModel.supportedDropActions(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AccountTreeView.__init__

**Определено в:** `app/ui/widgets/account_tree_view.py:26`

**Тип:** method

**Сигнатура:** `AccountTreeView.__init__(self, account_repo, trans_repo, split_repo, balance_service, settings, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### AccountTreeView._add_account

**Определено в:** `app/ui/widgets/account_tree_view.py:182`

**Тип:** method

**Сигнатура:** `AccountTreeView._add_account(self, parent_index)`

**Использования (2 мест):**


#### AccountTreeView._delete_account

**Определено в:** `app/ui/widgets/account_tree_view.py:201`

**Тип:** method

**Сигнатура:** `AccountTreeView._delete_account(self, index)`

**Использования (1 мест):**


#### AccountTreeView._delete_all_descendants

**Определено в:** `app/ui/widgets/account_tree_view.py:256`

**Тип:** method

**Сигнатура:** `AccountTreeView._delete_all_descendants(self, account_id)`

**Использования (2 мест):**


#### AccountTreeView._on_clicked

**Определено в:** `app/ui/widgets/account_tree_view.py:89`

**Тип:** method

**Сигнатура:** `AccountTreeView._on_clicked(self, index)`

**Использования (1 мест):**


#### AccountTreeView._on_selection_changed

**Определено в:** `app/ui/widgets/account_tree_view.py:144`

**Тип:** method

**Сигнатура:** `AccountTreeView._on_selection_changed(self)`

**Использования (1 мест):**


#### AccountTreeView._select_account_ids

**Определено в:** `app/ui/widgets/account_tree_view.py:128`

**Тип:** method

**Сигнатура:** `AccountTreeView._select_account_ids(self, account_ids, additive)`

**Использования (1 мест):**


#### AccountTreeView._show_context_menu

**Определено в:** `app/ui/widgets/account_tree_view.py:162`

**Тип:** method

**Сигнатура:** `AccountTreeView._show_context_menu(self, pos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AccountTreeView._show_header_menu

**Определено в:** `app/ui/widgets/account_tree_view.py:159`

**Тип:** method

**Сигнатура:** `AccountTreeView._show_header_menu(self, pos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AccountTreeView._toggle_column

**Определено в:** `app/ui/widgets/account_tree_view.py:327`

**Тип:** method

**Сигнатура:** `AccountTreeView._toggle_column(self, col, checked)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AccountTreeView._would_create_cycle

**Определено в:** `app/ui/widgets/account_tree_view.py:313`

**Тип:** method

**Сигнатура:** `AccountTreeView._would_create_cycle(self, moved_id, new_parent_id, model)`

**Использования (1 мест):**


#### AccountTreeView.dragEnterEvent

**Определено в:** `app/ui/widgets/account_tree_view.py:263`

**Тип:** method

**Сигнатура:** `AccountTreeView.dragEnterEvent(self, event)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AccountTreeView.dragMoveEvent

**Определено в:** `app/ui/widgets/account_tree_view.py:269`

**Тип:** method

**Сигнатура:** `AccountTreeView.dragMoveEvent(self, event)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AccountTreeView.dropEvent

**Определено в:** `app/ui/widgets/account_tree_view.py:275`

**Тип:** method

**Сигнатура:** `AccountTreeView.dropEvent(self, event)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AccountTreeView.keyPressEvent

**Определено в:** `app/ui/widgets/account_tree_view.py:57`

**Тип:** method

**Сигнатура:** `AccountTreeView.keyPressEvent(self, event)`

**Использования (7 мест):**


#### AccountTreeView.moveCursor

**Определено в:** `app/ui/widgets/account_tree_view.py:67`

**Тип:** method

**Сигнатура:** `AccountTreeView.moveCursor(self, cursorAction, modifiers)`

**Использования (3 мест):**


#### AccountTreeView.setModel

**Определено в:** `app/ui/widgets/account_tree_view.py:51`

**Тип:** method

**Сигнатура:** `AccountTreeView.setModel(self, model)`

**Использования (5 мест):**


#### AmountDelegate.__init__

**Определено в:** `app/ui/delegates/amount_delegate.py:11`

**Тип:** method

**Сигнатура:** `AmountDelegate.__init__(self, settings, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### AmountDelegate._preprocess

**Определено в:** `app/ui/delegates/amount_delegate.py:16`

**Тип:** method

**Сигнатура:** `AmountDelegate._preprocess(self, text)`

**Использования (2 мест):**


#### AmountDelegate.createEditor

**Определено в:** `app/ui/delegates/amount_delegate.py:33`

**Тип:** method

**Сигнатура:** `AmountDelegate.createEditor(self, parent, option, index)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AmountDelegate.eventFilter

**Определено в:** `app/ui/delegates/amount_delegate.py:43`

**Тип:** method

**Сигнатура:** `AmountDelegate.eventFilter(self, editor, event)`

**Использования (3 мест):**


#### AmountDelegate.setEditorData

**Определено в:** `app/ui/delegates/amount_delegate.py:38`

**Тип:** method

**Сигнатура:** `AmountDelegate.setEditorData(self, editor, index)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AmountDelegate.setModelData

**Определено в:** `app/ui/delegates/amount_delegate.py:60`

**Тип:** method

**Сигнатура:** `AmountDelegate.setModelData(self, editor, model, index)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AmountDelegate.updateEditorGeometry

**Определено в:** `app/ui/delegates/amount_delegate.py:85`

**Тип:** method

**Сигнатура:** `AmountDelegate.updateEditorGeometry(self, editor, option, index)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AmountFormatter.__init__

**Определено в:** `app/services/amount_formatter.py:11`

**Тип:** method

**Сигнатура:** `AmountFormatter.__init__(self, settings, currencies_repo)`

**Использования (17 мест):**

- ... и ещё 7

#### AmountFormatter.format_amount

**Определено в:** `app/services/amount_formatter.py:15`

**Тип:** method

**Сигнатура:** `AmountFormatter.format_amount(self, quants, currency_id)`

**Использования (2 мест):**


#### AmountFormatter.format_with_currency

**Определено в:** `app/services/amount_formatter.py:36`

**Тип:** method

**Сигнатура:** `AmountFormatter.format_with_currency(self, quants, currency_id)`

**Использования (1 мест):**


#### AppSettings.__init__

**Определено в:** `app/settings/app_settings.py:22`

**Тип:** method

**Сигнатура:** `AppSettings.__init__(self)`

**Использования (17 мест):**

- ... и ещё 7

#### AppSettings.account_path_sep

**Определено в:** `app/settings/app_settings.py:45`

**Тип:** method

**Сигнатура:** `AppSettings.account_path_sep(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AppSettings.allow_grouping_accounts_for_splits

**Определено в:** `app/settings/app_settings.py:64`

**Тип:** method

**Сигнатура:** `AppSettings.allow_grouping_accounts_for_splits(self, value)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AppSettings.date_format

**Определено в:** `app/settings/app_settings.py:33`

**Тип:** method

**Сигнатура:** `AppSettings.date_format(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AppSettings.decimal_sep

**Определено в:** `app/settings/app_settings.py:37`

**Тип:** method

**Сигнатура:** `AppSettings.decimal_sep(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AppSettings.get

**Определено в:** `app/settings/app_settings.py:25`

**Тип:** method

**Сигнатура:** `AppSettings.get(self, key)`

**Использования (45 мест):**

- ... и ещё 35

#### AppSettings.set

**Определено в:** `app/settings/app_settings.py:28`

**Тип:** method

**Сигнатура:** `AppSettings.set(self, key, value)`

**Использования (7 мест):**


#### AppSettings.show_hidden_accounts

**Определено в:** `app/settings/app_settings.py:54`

**Тип:** method

**Сигнатура:** `AppSettings.show_hidden_accounts(self, value)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AppSettings.thousands_sep

**Определено в:** `app/settings/app_settings.py:41`

**Тип:** method

**Сигнатура:** `AppSettings.thousands_sep(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### AppSettings.transaction_view_mode

**Определено в:** `app/settings/app_settings.py:71`

**Тип:** method

**Сигнатура:** `AppSettings.transaction_view_mode(self, value)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### BalanceService.__init__

**Определено в:** `app/services/balance_service.py:10`

**Тип:** method

**Сигнатура:** `BalanceService.__init__(self, account_repo, split_repo)`

**Использования (17 мест):**

- ... и ещё 7

#### BalanceService._get_leaf_balance

**Определено в:** `app/services/balance_service.py:43`

**Тип:** method

**Сигнатура:** `BalanceService._get_leaf_balance(self, account_id)`

**Использования (1 мест):**


#### BalanceService.clear

**Определено в:** `app/services/balance_service.py:51`

**Тип:** method

**Сигнатура:** `BalanceService.clear(self)`

**Использования (11 мест):**

- ... и ещё 1

#### BalanceService.get_balance

**Определено в:** `app/services/balance_service.py:29`

**Тип:** method

**Сигнатура:** `BalanceService.get_balance(self, account_id, include_children)`

**Использования (7 мест):**


#### BalanceService.invalidate

**Определено в:** `app/services/balance_service.py:16`

**Тип:** method

**Сигнатура:** `BalanceService.invalidate(self, account_id, currency_id)`

**Использования (2 мест):**


#### BalanceService.invalidate_account_tree

**Определено в:** `app/services/balance_service.py:23`

**Тип:** method

**Сигнатура:** `BalanceService.invalidate_account_tree(self, account_id)`

**Использования (1 мест):**


#### CurrencyComboDelegate.__init__

**Определено в:** `app/ui/delegates/currency_combo_delegate.py:10`

**Тип:** method

**Сигнатура:** `CurrencyComboDelegate.__init__(self, currency_repo, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### CurrencyComboDelegate._get_items

**Определено в:** `app/ui/delegates/currency_combo_delegate.py:14`

**Тип:** method

**Сигнатура:** `CurrencyComboDelegate._get_items(self)`

**Использования (1 мест):**


#### CurrencyEditorDialog.__init__

**Определено в:** `app/ui/dialogs/currency_editor_dialog.py:21`

**Тип:** method

**Сигнатура:** `CurrencyEditorDialog.__init__(self, currency_repo, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### CurrencyEditorDialog._add_row

**Определено в:** `app/ui/dialogs/currency_editor_dialog.py:82`

**Тип:** method

**Сигнатура:** `CurrencyEditorDialog._add_row(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### CurrencyEditorDialog._add_table_row

**Определено в:** `app/ui/dialogs/currency_editor_dialog.py:64`

**Тип:** method

**Сигнатура:** `CurrencyEditorDialog._add_table_row(self, cur_id, code, type_, name, denom)`

**Использования (2 мест):**


#### CurrencyEditorDialog._build_ui

**Определено в:** `app/ui/dialogs/currency_editor_dialog.py:31`

**Тип:** method

**Сигнатура:** `CurrencyEditorDialog._build_ui(self)`

**Использования (2 мест):**


#### CurrencyEditorDialog._delete_row

**Определено в:** `app/ui/dialogs/currency_editor_dialog.py:85`

**Тип:** method

**Сигнатура:** `CurrencyEditorDialog._delete_row(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### CurrencyEditorDialog._load

**Определено в:** `app/ui/dialogs/currency_editor_dialog.py:57`

**Тип:** method

**Сигнатура:** `CurrencyEditorDialog._load(self)`

**Использования (1 мест):**


#### CurrencyEditorDialog._save

**Определено в:** `app/ui/dialogs/currency_editor_dialog.py:99`

**Тип:** method

**Сигнатура:** `CurrencyEditorDialog._save(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### CurrencyRepo.__init__

**Определено в:** `app/repositories/currency_repo.py:17`

**Тип:** method

**Сигнатура:** `CurrencyRepo.__init__(self, conn)`

**Использования (17 мест):**

- ... и ещё 7

#### CurrencyRepo.delete

**Определено в:** `app/repositories/currency_repo.py:37`

**Тип:** method

**Сигнатура:** `CurrencyRepo.delete(self, currency_id)`

**Использования (7 мест):**


#### CurrencyRepo.get_all

**Определено в:** `app/repositories/currency_repo.py:20`

**Тип:** method

**Сигнатура:** `CurrencyRepo.get_all(self)`

**Использования (9 мест):**


#### CurrencyRepo.get_by_id

**Определено в:** `app/repositories/currency_repo.py:24`

**Тип:** method

**Сигнатура:** `CurrencyRepo.get_by_id(self, currency_id)`

**Использования (21 мест):**

- ... и ещё 11

#### CurrencyRepo.insert

**Определено в:** `app/repositories/currency_repo.py:28`

**Тип:** method

**Сигнатура:** `CurrencyRepo.insert(self, code, type_, name, denominator)`

**Использования (73 мест):**

- ... и ещё 63

#### CurrencyRepo.is_used

**Определено в:** `app/repositories/currency_repo.py:41`

**Тип:** method

**Сигнатура:** `CurrencyRepo.is_used(self, currency_id)`

**Использования (1 мест):**


#### CurrencyRepo.update

**Определено в:** `app/repositories/currency_repo.py:33`

**Тип:** method

**Сигнатура:** `CurrencyRepo.update(self, currency_id, code, type_, name, denominator)`

**Использования (6 мест):**


#### DateDelegate.__init__

**Определено в:** `app/ui/delegates/date_delegate.py:13`

**Тип:** method

**Сигнатура:** `DateDelegate.__init__(self, settings, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### DateDelegate._local_tz

**Определено в:** `app/ui/delegates/date_delegate.py:21`

**Тип:** method

**Сигнатура:** `DateDelegate._local_tz(self)`

**Использования (2 мест):**


#### DateDelegate._qt_format

**Определено в:** `app/ui/delegates/date_delegate.py:18`

**Тип:** method

**Сигнатура:** `DateDelegate._qt_format(self)`

**Использования (1 мест):**


#### DateDelegate.createEditor

**Определено в:** `app/ui/delegates/date_delegate.py:27`

**Тип:** method

**Сигнатура:** `DateDelegate.createEditor(self, parent, option, index)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DateDelegate.setEditorData

**Определено в:** `app/ui/delegates/date_delegate.py:34`

**Тип:** method

**Сигнатура:** `DateDelegate.setEditorData(self, editor, index)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DateDelegate.setModelData

**Определено в:** `app/ui/delegates/date_delegate.py:52`

**Тип:** method

**Сигнатура:** `DateDelegate.setModelData(self, editor, model, index)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DateDelegate.updateEditorGeometry

**Определено в:** `app/ui/delegates/date_delegate.py:67`

**Тип:** method

**Сигнатура:** `DateDelegate.updateEditorGeometry(self, editor, option, index)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DeleteAccountDialog.__init__

**Определено в:** `app/ui/dialogs/delete_account_dialog.py:39`

**Тип:** method

**Сигнатура:** `DeleteAccountDialog.__init__(self, account_name, account_repo, split_repo, settings, exclude_id, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### DeleteAccountDialog._accept

**Определено в:** `app/ui/dialogs/delete_account_dialog.py:261`

**Тип:** method

**Сигнатура:** `DeleteAccountDialog._accept(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DeleteAccountDialog._check_has_splits

**Определено в:** `app/ui/dialogs/delete_account_dialog.py:169`

**Тип:** method

**Сигнатура:** `DeleteAccountDialog._check_has_splits(self)`

**Использования (1 мест):**


#### DeleteAccountDialog._check_has_subaccounts

**Определено в:** `app/ui/dialogs/delete_account_dialog.py:164`

**Тип:** method

**Сигнатура:** `DeleteAccountDialog._check_has_subaccounts(self)`

**Использования (1 мест):**


#### DeleteAccountDialog._on_action_changed

**Определено в:** `app/ui/dialogs/delete_account_dialog.py:244`

**Тип:** method

**Сигнатура:** `DeleteAccountDialog._on_action_changed(self)`

**Использования (1 мест):**


#### DeleteAccountDialog._populate_subaccounts_combo

**Определено в:** `app/ui/dialogs/delete_account_dialog.py:181`

**Тип:** method

**Сигнатура:** `DeleteAccountDialog._populate_subaccounts_combo(self)`

**Использования (1 мест):**


#### DeleteAccountDialog._populate_transactions_combo

**Определено в:** `app/ui/dialogs/delete_account_dialog.py:207`

**Тип:** method

**Сигнатура:** `DeleteAccountDialog._populate_transactions_combo(self)`

**Использования (2 мест):**


#### DeleteAccountDialog._update_transactions_combo

**Определено в:** `app/ui/dialogs/delete_account_dialog.py:240`

**Тип:** method

**Сигнатура:** `DeleteAccountDialog._update_transactions_combo(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DeleteAccountDialog.action

**Определено в:** `app/ui/dialogs/delete_account_dialog.py:290`

**Тип:** method

**Сигнатура:** `DeleteAccountDialog.action(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DeleteAccountDialog.subaccounts_action

**Определено в:** `app/ui/dialogs/delete_account_dialog.py:294`

**Тип:** method

**Сигнатура:** `DeleteAccountDialog.subaccounts_action(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DeleteAccountDialog.subaccounts_target_id

**Определено в:** `app/ui/dialogs/delete_account_dialog.py:298`

**Тип:** method

**Сигнатура:** `DeleteAccountDialog.subaccounts_target_id(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DeleteAccountDialog.transactions_action

**Определено в:** `app/ui/dialogs/delete_account_dialog.py:302`

**Тип:** method

**Сигнатура:** `DeleteAccountDialog.transactions_action(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DeleteAccountDialog.transactions_target_id

**Определено в:** `app/ui/dialogs/delete_account_dialog.py:306`

**Тип:** method

**Сигнатура:** `DeleteAccountDialog.transactions_target_id(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DetailedFunctionAnalyzer.__init__

**Определено в:** `generate_detailed_function_usage.py:17`

**Тип:** method

**Сигнатура:** `DetailedFunctionAnalyzer.__init__(self, filepath, content)`

**Использования (17 мест):**

- ... и ещё 7

#### DetailedFunctionAnalyzer._analyze_qt_connect

**Определено в:** `generate_detailed_function_usage.py:120`

**Тип:** method

**Сигнатура:** `DetailedFunctionAnalyzer._analyze_qt_connect(self, node)`

**Использования (1 мест):**


#### DetailedFunctionAnalyzer.get_line_context

**Определено в:** `generate_detailed_function_usage.py:28`

**Тип:** method

**Сигнатура:** `DetailedFunctionAnalyzer.get_line_context(self, line_no)`

**Использования (3 мест):**


#### DetailedFunctionAnalyzer.visit_AsyncFunctionDef

**Определено в:** `generate_detailed_function_usage.py:58`

**Тип:** method

**Сигнатура:** `DetailedFunctionAnalyzer.visit_AsyncFunctionDef(self, node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DetailedFunctionAnalyzer.visit_Attribute

**Определено в:** `generate_detailed_function_usage.py:154`

**Тип:** method

**Сигнатура:** `DetailedFunctionAnalyzer.visit_Attribute(self, node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DetailedFunctionAnalyzer.visit_Call

**Определено в:** `generate_detailed_function_usage.py:88`

**Тип:** method

**Сигнатура:** `DetailedFunctionAnalyzer.visit_Call(self, node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DetailedFunctionAnalyzer.visit_ClassDef

**Определено в:** `generate_detailed_function_usage.py:81`

**Тип:** method

**Сигнатура:** `DetailedFunctionAnalyzer.visit_ClassDef(self, node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DetailedFunctionAnalyzer.visit_FunctionDef

**Определено в:** `generate_detailed_function_usage.py:34`

**Тип:** method

**Сигнатура:** `DetailedFunctionAnalyzer.visit_FunctionDef(self, node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DetailedFunctionAnalyzer.visit_Import

**Определено в:** `generate_detailed_function_usage.py:139`

**Тип:** method

**Сигнатура:** `DetailedFunctionAnalyzer.visit_Import(self, node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DetailedFunctionAnalyzer.visit_ImportFrom

**Определено в:** `generate_detailed_function_usage.py:146`

**Тип:** method

**Сигнатура:** `DetailedFunctionAnalyzer.visit_ImportFrom(self, node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DetailedFunctionAnalyzer.visit_Lambda

**Определено в:** `generate_detailed_function_usage.py:160`

**Тип:** method

**Сигнатура:** `DetailedFunctionAnalyzer.visit_Lambda(self, node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### DisplaySettings.__init__

**Определено в:** `app/settings/display_settings.py:11`

**Тип:** method

**Сигнатура:** `DisplaySettings.__init__(self, panel_name)`

**Использования (17 мест):**

- ... и ещё 7

#### DisplaySettings._key

**Определено в:** `app/settings/display_settings.py:15`

**Тип:** method

**Сигнатура:** `DisplaySettings._key(self, name)`

**Использования (10 мест):**


#### DisplaySettings.get_column_order

**Определено в:** `app/settings/display_settings.py:18`

**Тип:** method

**Сигнатура:** `DisplaySettings.get_column_order(self, default)`

**Использования (1 мест):**


#### DisplaySettings.get_column_widths

**Определено в:** `app/settings/display_settings.py:27`

**Тип:** method

**Сигнатура:** `DisplaySettings.get_column_widths(self, default)`

**Использования (1 мест):**


#### DisplaySettings.get_hidden_columns

**Определено в:** `app/settings/display_settings.py:36`

**Тип:** method

**Сигнатура:** `DisplaySettings.get_hidden_columns(self, default)`

**Использования (1 мест):**


#### DisplaySettings.get_sort_column

**Определено в:** `app/settings/display_settings.py:45`

**Тип:** method

**Сигнатура:** `DisplaySettings.get_sort_column(self, default)`

**Использования (1 мест):**


#### DisplaySettings.get_sort_order

**Определено в:** `app/settings/display_settings.py:51`

**Тип:** method

**Сигнатура:** `DisplaySettings.get_sort_order(self, default)`

**Использования (1 мест):**


#### DisplaySettings.set_column_order

**Определено в:** `app/settings/display_settings.py:24`

**Тип:** method

**Сигнатура:** `DisplaySettings.set_column_order(self, order)`

**Использования (1 мест):**


#### DisplaySettings.set_column_widths

**Определено в:** `app/settings/display_settings.py:33`

**Тип:** method

**Сигнатура:** `DisplaySettings.set_column_widths(self, widths)`

**Использования (1 мест):**


#### DisplaySettings.set_hidden_columns

**Определено в:** `app/settings/display_settings.py:42`

**Тип:** method

**Сигнатура:** `DisplaySettings.set_hidden_columns(self, cols)`

**Использования (1 мест):**


#### DisplaySettings.set_sort_column

**Определено в:** `app/settings/display_settings.py:48`

**Тип:** method

**Сигнатура:** `DisplaySettings.set_sort_column(self, col)`

**Использования (1 мест):**


#### DisplaySettings.set_sort_order

**Определено в:** `app/settings/display_settings.py:54`

**Тип:** method

**Сигнатура:** `DisplaySettings.set_sort_order(self, order)`

**Использования (1 мест):**


#### FunctionUsageAnalyzer.__init__

**Определено в:** `generate_function_usage_docs.py:17`

**Тип:** method

**Сигнатура:** `FunctionUsageAnalyzer.__init__(self, filepath)`

**Использования (17 мест):**

- ... и ещё 7

#### FunctionUsageAnalyzer.visit_AsyncFunctionDef

**Определено в:** `generate_function_usage_docs.py:34`

**Тип:** method

**Сигнатура:** `FunctionUsageAnalyzer.visit_AsyncFunctionDef(self, node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### FunctionUsageAnalyzer.visit_Call

**Определено в:** `generate_function_usage_docs.py:51`

**Тип:** method

**Сигнатура:** `FunctionUsageAnalyzer.visit_Call(self, node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### FunctionUsageAnalyzer.visit_ClassDef

**Определено в:** `generate_function_usage_docs.py:44`

**Тип:** method

**Сигнатура:** `FunctionUsageAnalyzer.visit_ClassDef(self, node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### FunctionUsageAnalyzer.visit_FunctionDef

**Определено в:** `generate_function_usage_docs.py:24`

**Тип:** method

**Сигнатура:** `FunctionUsageAnalyzer.visit_FunctionDef(self, node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### FunctionUsageAnalyzer.visit_Import

**Определено в:** `generate_function_usage_docs.py:62`

**Тип:** method

**Сигнатура:** `FunctionUsageAnalyzer.visit_Import(self, node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### FunctionUsageAnalyzer.visit_ImportFrom

**Определено в:** `generate_function_usage_docs.py:68`

**Тип:** method

**Сигнатура:** `FunctionUsageAnalyzer.visit_ImportFrom(self, node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### IntegrityService.__init__

**Определено в:** `app/services/integrity_service.py:9`

**Тип:** method

**Сигнатура:** `IntegrityService.__init__(self, trans_repo, split_repo, conn)`

**Использования (17 мест):**

- ... и ещё 7

#### IntegrityService.check_foreign_keys

**Определено в:** `app/services/integrity_service.py:28`

**Тип:** method

**Сигнатура:** `IntegrityService.check_foreign_keys(self)`

**Использования (1 мест):**


#### IntegrityService.get_empty_transactions

**Определено в:** `app/services/integrity_service.py:20`

**Тип:** method

**Сигнатура:** `IntegrityService.get_empty_transactions(self)`

**Использования (3 мест):**


#### IntegrityService.get_imbalanced_trans_ids

**Определено в:** `app/services/integrity_service.py:15`

**Тип:** method

**Сигнатура:** `IntegrityService.get_imbalanced_trans_ids(self)`

**Использования (3 мест):**


#### IntegrityService.get_zero_split_ids

**Определено в:** `app/services/integrity_service.py:24`

**Тип:** method

**Сигнатура:** `IntegrityService.get_zero_split_ids(self)`

**Использования (2 мест):**


#### IntegrityService.has_empty_transactions

**Определено в:** `app/services/integrity_service.py:36`

**Тип:** method

**Сигнатура:** `IntegrityService.has_empty_transactions(self)`

**Использования (3 мест):**


#### IntegrityService.has_imbalance

**Определено в:** `app/services/integrity_service.py:33`

**Тип:** method

**Сигнатура:** `IntegrityService.has_imbalance(self)`

**Использования (4 мест):**


#### MainWindow.__init__

**Определено в:** `app/ui/main_window.py:51`

**Тип:** method

**Сигнатура:** `MainWindow.__init__(self, db_path, settings, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### MainWindow._apply_display_settings

**Определено в:** `app/ui/main_window.py:425`

**Тип:** method

**Сигнатура:** `MainWindow._apply_display_settings(self, view, header, display, default_order, default_widths, default_hidden, default_sort_col, default_sort_order)`

**Использования (3 мест):**


#### MainWindow._connect_signals

**Определено в:** `app/ui/main_window.py:310`

**Тип:** method

**Сигнатура:** `MainWindow._connect_signals(self)`

**Использования (1 мест):**


#### MainWindow._focus_accounts

**Определено в:** `app/ui/main_window.py:489`

**Тип:** method

**Сигнатура:** `MainWindow._focus_accounts(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._focus_current_transaction_splits

**Определено в:** `app/ui/main_window.py:495`

**Тип:** method

**Сигнатура:** `MainWindow._focus_current_transaction_splits(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._focus_split_cell

**Определено в:** `app/ui/main_window.py:370`

**Тип:** method

**Сигнатура:** `MainWindow._focus_split_cell(self, row, col)`

**Использования (2 мест):**


#### MainWindow._focus_transactions

**Определено в:** `app/ui/main_window.py:492`

**Тип:** method

**Сигнатура:** `MainWindow._focus_transactions(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._load_transactions

**Определено в:** `app/ui/main_window.py:525`

**Тип:** method

**Сигнатура:** `MainWindow._load_transactions(self)`

**Использования (3 мест):**


#### MainWindow._load_virtual_transactions

**Определено в:** `app/ui/main_window.py:530`

**Тип:** method

**Сигнатура:** `MainWindow._load_virtual_transactions(self, virtual_id)`

**Использования (1 мест):**


#### MainWindow._new_file

**Определено в:** `app/ui/main_window.py:843`

**Тип:** method

**Сигнатура:** `MainWindow._new_file(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._on_accounts_selected

**Определено в:** `app/ui/main_window.py:512`

**Тип:** method

**Сигнатура:** `MainWindow._on_accounts_selected(self, account_ids)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._on_new_transaction_requested

**Определено в:** `app/ui/main_window.py:329`

**Тип:** method

**Сигнатура:** `MainWindow._on_new_transaction_requested(self, description, date)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._on_split_changed

**Определено в:** `app/ui/main_window.py:564`

**Тип:** method

**Сигнатура:** `MainWindow._on_split_changed(self, force)`

**Использования (5 мест):**


#### MainWindow._on_split_data_changed

**Определено в:** `app/ui/main_window.py:664`

**Тип:** method

**Сигнатура:** `MainWindow._on_split_data_changed(self, top_left, bottom_right, roles)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._on_trans_data_changed

**Определено в:** `app/ui/main_window.py:653`

**Тип:** method

**Сигнатура:** `MainWindow._on_trans_data_changed(self, top_left, bottom_right, roles)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._on_transaction_cleared

**Определено в:** `app/ui/main_window.py:543`

**Тип:** method

**Сигнатура:** `MainWindow._on_transaction_cleared(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._on_transaction_selected

**Определено в:** `app/ui/main_window.py:549`

**Тип:** method

**Сигнатура:** `MainWindow._on_transaction_selected(self, trans_id)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._on_transactions_changed

**Определено в:** `app/ui/main_window.py:557`

**Тип:** method

**Сигнатура:** `MainWindow._on_transactions_changed(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._on_virtual_node_selected

**Определено в:** `app/ui/main_window.py:519`

**Тип:** method

**Сигнатура:** `MainWindow._on_virtual_node_selected(self, virtual_id)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._open_currency_editor

**Определено в:** `app/ui/main_window.py:872`

**Тип:** method

**Сигнатура:** `MainWindow._open_currency_editor(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._open_file

**Определено в:** `app/ui/main_window.py:851`

**Тип:** method

**Сигнатура:** `MainWindow._open_file(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._open_file_path

**Определено в:** `app/ui/main_window.py:859`

**Тип:** method

**Сигнатура:** `MainWindow._open_file_path(self, path)`

**Использования (3 мест):**


#### MainWindow._open_settings

**Определено в:** `app/ui/main_window.py:877`

**Тип:** method

**Сигнатура:** `MainWindow._open_settings(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._refresh_integrity

**Определено в:** `app/ui/main_window.py:820`

**Тип:** method

**Сигнатура:** `MainWindow._refresh_integrity(self)`

**Использования (4 мест):**


#### MainWindow._refresh_recent_menu

**Определено в:** `app/ui/main_window.py:834`

**Тип:** method

**Сигнатура:** `MainWindow._refresh_recent_menu(self)`

**Использования (1 мест):**


#### MainWindow._restore_view_settings

**Определено в:** `app/ui/main_window.py:399`

**Тип:** method

**Сигнатура:** `MainWindow._restore_view_settings(self)`

**Использования (1 мест):**


#### MainWindow._restore_window_layout

**Определено в:** `app/ui/main_window.py:387`

**Тип:** method

**Сигнатура:** `MainWindow._restore_window_layout(self)`

**Использования (1 мест):**


#### MainWindow._save_view_settings

**Определено в:** `app/ui/main_window.py:459`

**Тип:** method

**Сигнатура:** `MainWindow._save_view_settings(self)`

**Использования (1 мест):**


#### MainWindow._save_window_layout

**Определено в:** `app/ui/main_window.py:479`

**Тип:** method

**Сигнатура:** `MainWindow._save_window_layout(self)`

**Использования (1 мест):**


#### MainWindow._set_view_mode

**Определено в:** `app/ui/main_window.py:814`

**Тип:** method

**Сигнатура:** `MainWindow._set_view_mode(self, mode)`

**Использования (2 мест):**


#### MainWindow._setup_delegates

**Определено в:** `app/ui/main_window.py:295`

**Тип:** method

**Сигнатура:** `MainWindow._setup_delegates(self)`

**Использования (1 мест):**


#### MainWindow._setup_menu

**Определено в:** `app/ui/main_window.py:159`

**Тип:** method

**Сигнатура:** `MainWindow._setup_menu(self)`

**Использования (1 мест):**


#### MainWindow._setup_models

**Определено в:** `app/ui/main_window.py:237`

**Тип:** method

**Сигнатура:** `MainWindow._setup_models(self)`

**Использования (1 мест):**


#### MainWindow._setup_ui

**Определено в:** `app/ui/main_window.py:98`

**Тип:** method

**Сигнатура:** `MainWindow._setup_ui(self)`

**Использования (1 мест):**


#### MainWindow._store_display_settings

**Определено в:** `app/ui/main_window.py:464`

**Тип:** method

**Сигнатура:** `MainWindow._store_display_settings(self, view, header, display)`

**Использования (3 мест):**


#### MainWindow._toggle_allow_grouping_for_splits

**Определено в:** `app/ui/main_window.py:811`

**Тип:** method

**Сигнатура:** `MainWindow._toggle_allow_grouping_for_splits(self, checked)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow._toggle_show_hidden

**Определено в:** `app/ui/main_window.py:806`

**Тип:** method

**Сигнатура:** `MainWindow._toggle_show_hidden(self, checked)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### MainWindow.closeEvent

**Определено в:** `app/ui/main_window.py:887`

**Тип:** method

**Сигнатура:** `MainWindow.closeEvent(self, event)`

**Использования (1 мест):**


#### SearchableComboDelegate.__init__

**Определено в:** `app/ui/delegates/searchable_combo_delegate.py:13`

**Тип:** method

**Сигнатура:** `SearchableComboDelegate.__init__(self, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### SearchableComboDelegate._apply_current_completion

**Определено в:** `app/ui/delegates/searchable_combo_delegate.py:63`

**Тип:** method

**Сигнатура:** `SearchableComboDelegate._apply_current_completion(self, combo)`

**Использования (1 мест):**


#### SearchableComboDelegate._extract_combo

**Определено в:** `app/ui/delegates/searchable_combo_delegate.py:47`

**Тип:** method

**Сигнатура:** `SearchableComboDelegate._extract_combo(self, watched)`

**Использования (1 мест):**


#### SearchableComboDelegate._get_items

**Определено в:** `app/ui/delegates/searchable_combo_delegate.py:17`

**Тип:** method

**Сигнатура:** `SearchableComboDelegate._get_items(self)`

**Использования (1 мест):**


#### SearchableComboDelegate._sync_index_with_text

**Определено в:** `app/ui/delegates/searchable_combo_delegate.py:54`

**Тип:** method

**Сигнатура:** `SearchableComboDelegate._sync_index_with_text(self, combo)`

**Использования (2 мест):**


#### SearchableComboDelegate.createEditor

**Определено в:** `app/ui/delegates/searchable_combo_delegate.py:21`

**Тип:** method

**Сигнатура:** `SearchableComboDelegate.createEditor(self, parent, option, index)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### SearchableComboDelegate.eventFilter

**Определено в:** `app/ui/delegates/searchable_combo_delegate.py:37`

**Тип:** method

**Сигнатура:** `SearchableComboDelegate.eventFilter(self, watched, event)`

**Использования (3 мест):**


#### SearchableComboDelegate.setEditorData

**Определено в:** `app/ui/delegates/searchable_combo_delegate.py:80`

**Тип:** method

**Сигнатура:** `SearchableComboDelegate.setEditorData(self, editor, index)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### SearchableComboDelegate.setModelData

**Определено в:** `app/ui/delegates/searchable_combo_delegate.py:97`

**Тип:** method

**Сигнатура:** `SearchableComboDelegate.setModelData(self, editor, model, index)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### SearchableComboDelegate.updateEditorGeometry

**Определено в:** `app/ui/delegates/searchable_combo_delegate.py:109`

**Тип:** method

**Сигнатура:** `SearchableComboDelegate.updateEditorGeometry(self, editor, option, index)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### SettingsDialog.__init__

**Определено в:** `app/ui/dialogs/settings_dialog.py:11`

**Тип:** method

**Сигнатура:** `SettingsDialog.__init__(self, settings, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### SettingsDialog._build_ui

**Определено в:** `app/ui/dialogs/settings_dialog.py:19`

**Тип:** method

**Сигнатура:** `SettingsDialog._build_ui(self)`

**Использования (2 мест):**


#### SettingsDialog._save_and_accept

**Определено в:** `app/ui/dialogs/settings_dialog.py:55`

**Тип:** method

**Сигнатура:** `SettingsDialog._save_and_accept(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### SplitModel.__init__

**Определено в:** `app/ui/item_models/split_model.py:65`

**Тип:** method

**Сигнатура:** `SplitModel.__init__(self, split_repo, account_repo, currency_repo, settings, formatter, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### SplitModel._add_phantom_rows

**Определено в:** `app/ui/item_models/split_model.py:103`

**Тип:** method

**Сигнатура:** `SplitModel._add_phantom_rows(self, splits)`

**Использования (1 мест):**


#### SplitModel._currency_code

**Определено в:** `app/ui/item_models/split_model.py:163`

**Тип:** method

**Сигнатура:** `SplitModel._currency_code(self, currency_id)`

**Использования (3 мест):**


#### SplitModel._edit_amt

**Определено в:** `app/ui/item_models/split_model.py:177`

**Тип:** method

**Сигнатура:** `SplitModel._edit_amt(self, quants, currency_id)`

**Использования (1 мест):**


#### SplitModel._enum_value

**Определено в:** `app/ui/item_models/split_model.py:129`

**Тип:** method

**Сигнатура:** `SplitModel._enum_value(value)`

**Использования (4 мест):**


#### SplitModel._format_amt

**Определено в:** `app/ui/item_models/split_model.py:169`

**Тип:** method

**Сигнатура:** `SplitModel._format_amt(self, quants, currency_id)`

**Использования (4 мест):**


#### SplitModel._to_checkstate

**Определено в:** `app/ui/item_models/split_model.py:133`

**Тип:** method

**Сигнатура:** `SplitModel._to_checkstate(value)`

**Использования (1 мест):**


#### SplitModel.columnCount

**Определено в:** `app/ui/item_models/split_model.py:125`

**Тип:** method

**Сигнатура:** `SplitModel.columnCount(self, parent)`

**Использования (13 мест):**

- ... и ещё 3

#### SplitModel.data

**Определено в:** `app/ui/item_models/split_model.py:187`

**Тип:** method

**Сигнатура:** `SplitModel.data(self, index, role)`

**Использования (20 мест):**

- ... и ещё 10

#### SplitModel.flags

**Определено в:** `app/ui/item_models/split_model.py:439`

**Тип:** method

**Сигнатура:** `SplitModel.flags(self, index)`

**Использования (7 мест):**


#### SplitModel.get_phantom_info

**Определено в:** `app/ui/item_models/split_model.py:473`

**Тип:** method

**Сигнатура:** `SplitModel.get_phantom_info(self, row)`

**Использования (1 мест):**


#### SplitModel.get_row_type

**Определено в:** `app/ui/item_models/split_model.py:468`

**Тип:** method

**Сигнатура:** `SplitModel.get_row_type(self, row)`

**Использования (3 мест):**


#### SplitModel.get_split

**Определено в:** `app/ui/item_models/split_model.py:463`

**Тип:** method

**Сигнатура:** `SplitModel.get_split(self, row)`

**Использования (2 мест):**


#### SplitModel.headerData

**Определено в:** `app/ui/item_models/split_model.py:145`

**Тип:** method

**Сигнатура:** `SplitModel.headerData(self, section, orientation, role)`

**Использования (1 мест):**


#### SplitModel.key

**Определено в:** `app/ui/item_models/split_model.py:484`

**Тип:** method

**Сигнатура:** `SplitModel.key(row_obj)`

**Использования (11 мест):**

- ... и ещё 1

#### SplitModel.load

**Определено в:** `app/ui/item_models/split_model.py:87`

**Тип:** method

**Сигнатура:** `SplitModel.load(self, trans_id)`

**Использования (11 мест):**

- ... и ещё 1

#### SplitModel.rowCount

**Определено в:** `app/ui/item_models/split_model.py:122`

**Тип:** method

**Сигнатура:** `SplitModel.rowCount(self, parent)`

**Использования (11 мест):**

- ... и ещё 1

#### SplitModel.setData

**Определено в:** `app/ui/item_models/split_model.py:293`

**Тип:** method

**Сигнатура:** `SplitModel.setData(self, index, value, role)`

**Использования (8 мест):**


#### SplitModel.set_filter

**Определено в:** `app/ui/item_models/split_model.py:510`

**Тип:** method

**Сигнатура:** `SplitModel.set_filter(self, filter_text)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### SplitModel.set_zero_split_ids

**Определено в:** `app/ui/item_models/split_model.py:112`

**Тип:** method

**Сигнатура:** `SplitModel.set_zero_split_ids(self, ids)`

**Использования (1 мест):**


#### SplitModel.sort

**Определено в:** `app/ui/item_models/split_model.py:477`

**Тип:** method

**Сигнатура:** `SplitModel.sort(self, column, order)`

**Использования (5 мест):**


#### SplitRepo.__init__

**Определено в:** `app/repositories/split_repo.py:20`

**Тип:** method

**Сигнатура:** `SplitRepo.__init__(self, conn)`

**Использования (17 мест):**

- ... и ещё 7

#### SplitRepo.delete

**Определено в:** `app/repositories/split_repo.py:62`

**Тип:** method

**Сигнатура:** `SplitRepo.delete(self, split_id)`

**Использования (7 мест):**


#### SplitRepo.delete_by_account

**Определено в:** `app/repositories/split_repo.py:66`

**Тип:** method

**Сигнатура:** `SplitRepo.delete_by_account(self, account_id)`

**Использования (1 мест):**


#### SplitRepo.get_balance_by_account

**Определено в:** `app/repositories/split_repo.py:70`

**Тип:** method

**Сигнатура:** `SplitRepo.get_balance_by_account(self, account_id)`

**Использования (1 мест):**


#### SplitRepo.get_by_id

**Определено в:** `app/repositories/split_repo.py:23`

**Тип:** method

**Сигнатура:** `SplitRepo.get_by_id(self, split_id)`

**Использования (21 мест):**

- ... и ещё 11

#### SplitRepo.get_by_transaction

**Определено в:** `app/repositories/split_repo.py:27`

**Тип:** method

**Сигнатура:** `SplitRepo.get_by_transaction(self, trans_id)`

**Использования (7 мест):**


#### SplitRepo.get_by_transaction_and_currency

**Определено в:** `app/repositories/split_repo.py:31`

**Тип:** method

**Сигнатура:** `SplitRepo.get_by_transaction_and_currency(self, trans_id, currency_id)`

**Использования (5 мест):**


#### SplitRepo.get_last_currency_for_account

**Определено в:** `app/repositories/split_repo.py:75`

**Тип:** method

**Сигнатура:** `SplitRepo.get_last_currency_for_account(self, account_id)`

**Использования (1 мест):**


#### SplitRepo.get_splits_with_zero_amount

**Определено в:** `app/repositories/split_repo.py:79`

**Тип:** method

**Сигнатура:** `SplitRepo.get_splits_with_zero_amount(self)`

**Использования (1 мест):**


#### SplitRepo.has_splits_for_account

**Определено в:** `app/repositories/split_repo.py:83`

**Тип:** method

**Сигнатура:** `SplitRepo.has_splits_for_account(self, account_id)`

**Использования (1 мест):**


#### SplitRepo.insert

**Определено в:** `app/repositories/split_repo.py:35`

**Тип:** method

**Сигнатура:** `SplitRepo.insert(self, trans_id, account_id, currency_id, description, external_id, amount, amount_fixed)`

**Использования (73 мест):**

- ... и ещё 63

#### SplitRepo.update

**Определено в:** `app/repositories/split_repo.py:43`

**Тип:** method

**Сигнатура:** `SplitRepo.update(self, split_id, account_id, currency_id, description, external_id, amount, amount_fixed)`

**Использования (6 мест):**


#### SplitRepo.update_account

**Определено в:** `app/repositories/split_repo.py:58`

**Тип:** method

**Сигнатура:** `SplitRepo.update_account(self, split_id, account_id)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### SplitRepo.update_amount

**Определено в:** `app/repositories/split_repo.py:50`

**Тип:** method

**Сигнатура:** `SplitRepo.update_amount(self, split_id, amount)`

**Использования (4 мест):**


#### SplitRepo.update_amount_fixed

**Определено в:** `app/repositories/split_repo.py:54`

**Тип:** method

**Сигнатура:** `SplitRepo.update_amount_fixed(self, split_id, fixed)`

**Использования (1 мест):**


#### SplitView.__init__

**Определено в:** `app/ui/widgets/split_view.py:24`

**Тип:** method

**Сигнатура:** `SplitView.__init__(self, trans_service, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### SplitView._delete_split

**Определено в:** `app/ui/widgets/split_view.py:115`

**Тип:** method

**Сигнатура:** `SplitView._delete_split(self, split_id)`

**Использования (1 мест):**


#### SplitView._first_editable_in_row

**Определено в:** `app/ui/widgets/split_view.py:43`

**Тип:** method

**Сигнатура:** `SplitView._first_editable_in_row(self, row)`

**Использования (1 мест):**


#### SplitView._show_context_menu

**Определено в:** `app/ui/widgets/split_view.py:95`

**Тип:** method

**Сигнатура:** `SplitView._show_context_menu(self, pos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### SplitView._show_header_menu

**Определено в:** `app/ui/widgets/split_view.py:120`

**Тип:** method

**Сигнатура:** `SplitView._show_header_menu(self, pos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### SplitView._toggle_column

**Определено в:** `app/ui/widgets/split_view.py:123`

**Тип:** method

**Сигнатура:** `SplitView._toggle_column(self, col, checked)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### SplitView.keyPressEvent

**Определено в:** `app/ui/widgets/split_view.py:53`

**Тип:** method

**Сигнатура:** `SplitView.keyPressEvent(self, event)`

**Использования (7 мест):**


#### SplitView.mousePressEvent

**Определено в:** `app/ui/widgets/split_view.py:91`

**Тип:** method

**Сигнатура:** `SplitView.mousePressEvent(self, event)`

**Использования (1 мест):**


#### SplitView.moveCursor

**Определено в:** `app/ui/widgets/split_view.py:82`

**Тип:** method

**Сигнатура:** `SplitView.moveCursor(self, cursorAction, modifiers)`

**Использования (3 мест):**


#### StartupDialog.__init__

**Определено в:** `main.py:90`

**Тип:** method

**Сигнатура:** `StartupDialog.__init__(self)`

**Использования (17 мест):**

- ... и ещё 7

#### StartupDialog._new

**Определено в:** `main.py:117`

**Тип:** method

**Сигнатура:** `StartupDialog._new(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### StartupDialog._open

**Определено в:** `main.py:108`

**Тип:** method

**Сигнатура:** `StartupDialog._open(self)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### TransactionModel.__init__

**Определено в:** `app/ui/item_models/transaction_model.py:36`

**Тип:** method

**Сигнатура:** `TransactionModel.__init__(self, trans_repo, currency_repo, settings, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### TransactionModel._format_amt

**Определено в:** `app/ui/item_models/transaction_model.py:149`

**Тип:** method

**Сигнатура:** `TransactionModel._format_amt(self, quants, denominator)`

**Использования (4 мест):**


#### TransactionModel._format_date

**Определено в:** `app/ui/item_models/transaction_model.py:138`

**Тип:** method

**Сигнатура:** `TransactionModel._format_date(self, utc_str)`

**Использования (1 мест):**


#### TransactionModel._is_phantom_row

**Определено в:** `app/ui/item_models/transaction_model.py:126`

**Тип:** method

**Сигнатура:** `TransactionModel._is_phantom_row(self, row)`

**Использования (3 мест):**


#### TransactionModel._phantom_date

**Определено в:** `app/ui/item_models/transaction_model.py:129`

**Тип:** method

**Сигнатура:** `TransactionModel._phantom_date(self)`

**Использования (1 мест):**


#### TransactionModel.canFetchMore

**Определено в:** `app/ui/item_models/transaction_model.py:99`

**Тип:** method

**Сигнатура:** `TransactionModel.canFetchMore(self, parent)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### TransactionModel.columnCount

**Определено в:** `app/ui/item_models/transaction_model.py:116`

**Тип:** method

**Сигнатура:** `TransactionModel.columnCount(self, parent)`

**Использования (13 мест):**

- ... и ещё 3

#### TransactionModel.data

**Определено в:** `app/ui/item_models/transaction_model.py:161`

**Тип:** method

**Сигнатура:** `TransactionModel.data(self, index, role)`

**Использования (20 мест):**

- ... и ещё 10

#### TransactionModel.fetchMore

**Определено в:** `app/ui/item_models/transaction_model.py:102`

**Тип:** method

**Сигнатура:** `TransactionModel.fetchMore(self, parent)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### TransactionModel.find_row_for_trans

**Определено в:** `app/ui/item_models/transaction_model.py:276`

**Тип:** method

**Сигнатура:** `TransactionModel.find_row_for_trans(self, trans_id)`

**Использования (4 мест):**


#### TransactionModel.flags

**Определено в:** `app/ui/item_models/transaction_model.py:215`

**Тип:** method

**Сигнатура:** `TransactionModel.flags(self, index)`

**Использования (7 мест):**


#### TransactionModel.get_trans_id

**Определено в:** `app/ui/item_models/transaction_model.py:271`

**Тип:** method

**Сигнатура:** `TransactionModel.get_trans_id(self, row)`

**Использования (3 мест):**


#### TransactionModel.headerData

**Определено в:** `app/ui/item_models/transaction_model.py:119`

**Тип:** method

**Сигнатура:** `TransactionModel.headerData(self, section, orientation, role)`

**Использования (1 мест):**


#### TransactionModel.key

**Определено в:** `app/ui/item_models/transaction_model.py:287`

**Тип:** method

**Сигнатура:** `TransactionModel.key(row)`

**Использования (11 мест):**

- ... и ещё 1

#### TransactionModel.load

**Определено в:** `app/ui/item_models/transaction_model.py:48`

**Тип:** method

**Сигнатура:** `TransactionModel.load(self, account_ids)`

**Использования (11 мест):**

- ... и ещё 1

#### TransactionModel.load_by_ids

**Определено в:** `app/ui/item_models/transaction_model.py:74`

**Тип:** method

**Сигнатура:** `TransactionModel.load_by_ids(self, trans_ids)`

**Использования (2 мест):**


#### TransactionModel.rowCount

**Определено в:** `app/ui/item_models/transaction_model.py:110`

**Тип:** method

**Сигнатура:** `TransactionModel.rowCount(self, parent)`

**Использования (11 мест):**

- ... и ещё 1

#### TransactionModel.setData

**Определено в:** `app/ui/item_models/transaction_model.py:227`

**Тип:** method

**Сигнатура:** `TransactionModel.setData(self, index, value, role)`

**Использования (8 мест):**


#### TransactionModel.set_filter

**Определено в:** `app/ui/item_models/transaction_model.py:308`

**Тип:** method

**Сигнатура:** `TransactionModel.set_filter(self, filter_text)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### TransactionModel.sort

**Определено в:** `app/ui/item_models/transaction_model.py:283`

**Тип:** method

**Сигнатура:** `TransactionModel.sort(self, column, order)`

**Использования (5 мест):**


#### TransactionRepo.__init__

**Определено в:** `app/repositories/transaction_repo.py:15`

**Тип:** method

**Сигнатура:** `TransactionRepo.__init__(self, conn)`

**Использования (17 мест):**

- ... и ещё 7

#### TransactionRepo._fetch_dicts_with_ids

**Определено в:** `app/repositories/transaction_repo.py:18`

**Тип:** method

**Сигнатура:** `TransactionRepo._fetch_dicts_with_ids(self, query_template, ids)`

**Использования (3 мест):**


#### TransactionRepo.delete

**Определено в:** `app/repositories/transaction_repo.py:39`

**Тип:** method

**Сигнатура:** `TransactionRepo.delete(self, trans_id)`

**Использования (7 мест):**


#### TransactionRepo.get_by_id

**Определено в:** `app/repositories/transaction_repo.py:26`

**Тип:** method

**Сигнатура:** `TransactionRepo.get_by_id(self, trans_id)`

**Использования (21 мест):**

- ... и ещё 11

#### TransactionRepo.get_empty

**Определено в:** `app/repositories/transaction_repo.py:56`

**Тип:** method

**Сигнатура:** `TransactionRepo.get_empty(self)`

**Использования (1 мест):**


#### TransactionRepo.get_imbalanced

**Определено в:** `app/repositories/transaction_repo.py:52`

**Тип:** method

**Сигнатура:** `TransactionRepo.get_imbalanced(self)`

**Использования (1 мест):**


#### TransactionRepo.get_summary_by_accounts

**Определено в:** `app/repositories/transaction_repo.py:46`

**Тип:** method

**Сигнатура:** `TransactionRepo.get_summary_by_accounts(self, account_ids)`

**Использования (1 мест):**


#### TransactionRepo.get_summary_by_ids

**Определено в:** `app/repositories/transaction_repo.py:49`

**Тип:** method

**Сигнатура:** `TransactionRepo.get_summary_by_ids(self, trans_ids)`

**Использования (1 мест):**


#### TransactionRepo.get_verbose_by_accounts

**Определено в:** `app/repositories/transaction_repo.py:43`

**Тип:** method

**Сигнатура:** `TransactionRepo.get_verbose_by_accounts(self, account_ids)`

**Использования (1 мест):**


#### TransactionRepo.insert

**Определено в:** `app/repositories/transaction_repo.py:30`

**Тип:** method

**Сигнатура:** `TransactionRepo.insert(self, date, description)`

**Использования (73 мест):**

- ... и ещё 63

#### TransactionRepo.update

**Определено в:** `app/repositories/transaction_repo.py:35`

**Тип:** method

**Сигнатура:** `TransactionRepo.update(self, trans_id, date, description)`

**Использования (6 мест):**


#### TransactionService.__init__

**Определено в:** `app/services/transaction_service.py:14`

**Тип:** method

**Сигнатура:** `TransactionService.__init__(self, trans_repo, split_repo)`

**Использования (17 мест):**

- ... и ещё 7

#### TransactionService._copy_transaction

**Определено в:** `app/services/transaction_service.py:80`

**Тип:** method

**Сигнатура:** `TransactionService._copy_transaction(self, trans_id, description_builder, amount_transform)`

**Использования (2 мест):**


#### TransactionService.add_split

**Определено в:** `app/services/transaction_service.py:30`

**Тип:** method

**Сигнатура:** `TransactionService.add_split(self, trans_id, account_id, currency_id, description, external_id, amount, amount_fixed)`

**Использования (19 мест):**

- ... и ещё 9

#### TransactionService.create_transaction

**Определено в:** `app/services/transaction_service.py:18`

**Тип:** method

**Сигнатура:** `TransactionService.create_transaction(self, description, date)`

**Использования (10 мест):**


#### TransactionService.delete_split

**Определено в:** `app/services/transaction_service.py:45`

**Тип:** method

**Сигнатура:** `TransactionService.delete_split(self, split_id)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### TransactionService.delete_split_and_rebalance

**Определено в:** `app/services/transaction_service.py:48`

**Тип:** method

**Сигнатура:** `TransactionService.delete_split_and_rebalance(self, split_id)`

**Использования (2 мест):**


#### TransactionService.delete_transaction

**Определено в:** `app/services/transaction_service.py:27`

**Тип:** method

**Сигнатура:** `TransactionService.delete_transaction(self, trans_id)`

**Использования (2 мест):**


#### TransactionService.duplicate_transaction

**Определено в:** `app/services/transaction_service.py:62`

**Тип:** method

**Сигнатура:** `TransactionService.duplicate_transaction(self, trans_id)`

**Использования (2 мест):**


#### TransactionService.recalculate_flexible_splits

**Определено в:** `app/services/transaction_service.py:101`

**Тип:** method

**Сигнатура:** `TransactionService.recalculate_flexible_splits(self, delta_amount, currency_id, trans_id)`

**Использования (8 мест):**


#### TransactionService.reverse_transaction

**Определено в:** `app/services/transaction_service.py:70`

**Тип:** method

**Сигнатура:** `TransactionService.reverse_transaction(self, trans_id)`

**Использования (2 мест):**


#### TransactionService.update_split

**Определено в:** `app/services/transaction_service.py:36`

**Тип:** method

**Сигнатура:** `TransactionService.update_split(self, split_id, account_id, currency_id, description, external_id, amount, amount_fixed)`

**Использования (1 мест):**


#### TransactionService.update_split_fixed

**Определено в:** `app/services/transaction_service.py:42`

**Тип:** method

**Сигнатура:** `TransactionService.update_split_fixed(self, split_id, amount_fixed)`

**Использования (3 мест):**


#### TransactionService.update_transaction

**Определено в:** `app/services/transaction_service.py:24`

**Тип:** method

**Сигнатура:** `TransactionService.update_transaction(self, trans_id, date, description)`

**Использования (1 мест):**


#### TransactionView.__init__

**Определено в:** `app/ui/widgets/transaction_view.py:25`

**Тип:** method

**Сигнатура:** `TransactionView.__init__(self, trans_service, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### TransactionView._delete

**Определено в:** `app/ui/widgets/transaction_view.py:158`

**Тип:** method

**Сигнатура:** `TransactionView._delete(self, trans_id)`

**Использования (1 мест):**


#### TransactionView._duplicate

**Определено в:** `app/ui/widgets/transaction_view.py:150`

**Тип:** method

**Сигнатура:** `TransactionView._duplicate(self, trans_id)`

**Использования (1 мест):**


#### TransactionView._on_clicked

**Определено в:** `app/ui/widgets/transaction_view.py:114`

**Тип:** method

**Сигнатура:** `TransactionView._on_clicked(self, index)`

**Использования (1 мест):**


#### TransactionView._on_current_row_changed

**Определено в:** `app/ui/widgets/transaction_view.py:108`

**Тип:** method

**Сигнатура:** `TransactionView._on_current_row_changed(self, current, previous)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### TransactionView._reverse

**Определено в:** `app/ui/widgets/transaction_view.py:154`

**Тип:** method

**Сигнатура:** `TransactionView._reverse(self, trans_id)`

**Использования (1 мест):**


#### TransactionView._show_context_menu

**Определено в:** `app/ui/widgets/transaction_view.py:123`

**Тип:** method

**Сигнатура:** `TransactionView._show_context_menu(self, pos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### TransactionView._show_header_menu

**Определено в:** `app/ui/widgets/transaction_view.py:169`

**Тип:** method

**Сигнатура:** `TransactionView._show_header_menu(self, pos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### TransactionView._toggle_column

**Определено в:** `app/ui/widgets/transaction_view.py:172`

**Тип:** method

**Сигнатура:** `TransactionView._toggle_column(self, col, checked)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### TransactionView.closeEditor

**Определено в:** `app/ui/widgets/transaction_view.py:75`

**Тип:** method

**Сигнатура:** `TransactionView.closeEditor(self, editor, hint)`

**Использования (3 мест):**


#### TransactionView.keyPressEvent

**Определено в:** `app/ui/widgets/transaction_view.py:50`

**Тип:** method

**Сигнатура:** `TransactionView.keyPressEvent(self, event)`

**Использования (7 мест):**


#### TransactionView.moveCursor

**Определено в:** `app/ui/widgets/transaction_view.py:65`

**Тип:** method

**Сигнатура:** `TransactionView.moveCursor(self, cursorAction, modifiers)`

**Использования (3 мест):**


#### TransactionView.setModel

**Определено в:** `app/ui/widgets/transaction_view.py:45`

**Тип:** method

**Сигнатура:** `TransactionView.setModel(self, model)`

**Использования (5 мест):**


#### UIEventLogger.__init__

**Определено в:** `app/ui/ui_event_logger.py:18`

**Тип:** method

**Сигнатура:** `UIEventLogger.__init__(self, parent)`

**Использования (17 мест):**

- ... и ещё 7

#### UIEventLogger._describe_event

**Определено в:** `app/ui/ui_event_logger.py:70`

**Тип:** method

**Сигнатура:** `UIEventLogger._describe_event(self, watched, event)`

**Использования (4 мест):**


#### UIEventLogger._describe_key_event

**Определено в:** `app/ui/ui_event_logger.py:47`

**Тип:** method

**Сигнатура:** `UIEventLogger._describe_key_event(self, watched, event)`

**Использования (1 мест):**


#### UIEventLogger._describe_mouse_event

**Определено в:** `app/ui/ui_event_logger.py:58`

**Тип:** method

**Сигнатура:** `UIEventLogger._describe_mouse_event(self, watched, event)`

**Использования (1 мест):**


#### UIEventLogger._object_name

**Определено в:** `app/ui/ui_event_logger.py:104`

**Тип:** method

**Сигнатура:** `UIEventLogger._object_name(self, obj)`

**Использования (5 мест):**


#### UIEventLogger._on_focus_changed

**Определено в:** `app/ui/ui_event_logger.py:40`

**Тип:** method

**Сигнатура:** `UIEventLogger._on_focus_changed(self, old, now)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### UIEventLogger._view_state

**Определено в:** `app/ui/ui_event_logger.py:76`

**Тип:** method

**Сигнатура:** `UIEventLogger._view_state(self, watched)`

**Использования (3 мест):**


#### UIEventLogger.eventFilter

**Определено в:** `app/ui/ui_event_logger.py:28`

**Тип:** method

**Сигнатура:** `UIEventLogger.eventFilter(self, watched, event)`

**Использования (3 мест):**


#### UIEventLogger.install

**Определено в:** `app/ui/ui_event_logger.py:22`

**Тип:** method

**Сигнатура:** `UIEventLogger.install(self, app)`

**Использования (1 мест):**


#### _apply_pragmas

**Определено в:** `app/database/connection.py:11`

**Тип:** function

**Сигнатура:** `_apply_pragmas(conn)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### _ask_file_path

**Определено в:** `main.py:85`

**Тип:** function

**Сигнатура:** `_ask_file_path()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### _configure_logging

**Определено в:** `main.py:18`

**Тип:** function

**Сигнатура:** `_configure_logging(enabled)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### _eval_node

**Определено в:** `app/utils/expression_parser.py:29`

**Тип:** function

**Сигнатура:** `_eval_node(node)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### _make_virtual_account

**Определено в:** `app/ui/item_models/account_tree_model.py:380`

**Тип:** function

**Сигнатура:** `_make_virtual_account(virtual_id, name)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### _parse_args

**Определено в:** `main.py:39`

**Тип:** function

**Сигнатура:** `_parse_args(argv)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### _row_to_account

**Определено в:** `app/repositories/account_repo.py:6`

**Тип:** function

**Сигнатура:** `_row_to_account(row)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### _row_to_currency

**Определено в:** `app/repositories/currency_repo.py:6`

**Тип:** function

**Сигнатура:** `_row_to_currency(row)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### _row_to_split

**Определено в:** `app/repositories/split_repo.py:6`

**Тип:** function

**Сигнатура:** `_row_to_split(row)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### _row_to_trans

**Определено в:** `app/repositories/transaction_repo.py:6`

**Тип:** function

**Сигнатура:** `_row_to_trans(row)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### _utc_now

**Определено в:** `app/services/transaction_service.py:9`

**Тип:** function

**Сигнатура:** `_utc_now()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### add_recent_file

**Определено в:** `app/utils/recent_files.py:18`

**Тип:** function

**Сигнатура:** `add_recent_file(path)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### analyze_codebase

**Определено в:** `generate_function_usage_docs.py:124`

**Тип:** function

**Сигнатура:** `analyze_codebase(root_dir)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### analyze_file

**Определено в:** `generate_function_usage_docs.py:76`

**Тип:** function

**Сигнатура:** `analyze_file(filepath)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### analyze_file_detailed

**Определено в:** `generate_detailed_function_usage.py:167`

**Тип:** function

**Сигнатура:** `analyze_file_detailed(filepath)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### balance_service

**Определено в:** `tests/test_balance_service.py:37`

**Тип:** function

**Сигнатура:** `balance_service(repos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### compute_hidden_account_ids

**Определено в:** `app/utils/account_hierarchy.py:6`

**Тип:** function

**Сигнатура:** `compute_hidden_account_ids(accounts)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### db

**Определено в:** `tests/test_transaction_service.py:17`

**Тип:** function

**Сигнатура:** `db()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### ensure_schema

**Определено в:** `app/database/schema.py:47`

**Тип:** function

**Сигнатура:** `ensure_schema(conn)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### find_all_usages_with_context

**Определено в:** `generate_detailed_function_usage.py:182`

**Тип:** function

**Сигнатура:** `find_all_usages_with_context(root_dir, function_name)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### find_next_editable_table_cell

**Определено в:** `app/ui/widgets/view_helpers.py:8`

**Тип:** function

**Сигнатура:** `find_next_editable_table_cell(view)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### float_to_quants

**Определено в:** `app/utils/amount_math.py:9`

**Тип:** function

**Сигнатура:** `float_to_quants(value, denominator)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### generate_comprehensive_report

**Определено в:** `generate_detailed_function_usage.py:219`

**Тип:** function

**Сигнатура:** `generate_comprehensive_report(root_dir)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### generate_markdown_report

**Определено в:** `generate_function_usage_docs.py:191`

**Тип:** function

**Сигнатура:** `generate_markdown_report(results)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### get_last_file

**Определено в:** `app/utils/recent_files.py:28`

**Тип:** function

**Сигнатура:** `get_last_file()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### get_recent_files

**Определено в:** `app/utils/recent_files.py:10`

**Тип:** function

**Сигнатура:** `get_recent_files()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### get_selectable_account_items

**Определено в:** `app/ui/account_selection.py:8`

**Тип:** function

**Сигнатура:** `get_selectable_account_items(account_repo, settings)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### integrity

**Определено в:** `tests/test_integrity_service.py:37`

**Тип:** function

**Сигнатура:** `integrity(repos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### main

**Определено в:** `main.py:50`

**Тип:** function

**Сигнатура:** `main()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### mark_hidden_descendants

**Определено в:** `app/utils/account_hierarchy.py:15`

**Тип:** function

**Сигнатура:** `mark_hidden_descendants(account_id)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### open_connection

**Определено в:** `app/database/connection.py:3`

**Тип:** function

**Сигнатура:** `open_connection(db_path)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### qt_format_to_strftime

**Определено в:** `app/utils/date_utils.py:4`

**Тип:** function

**Сигнатура:** `qt_format_to_strftime(qt_format)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### quants_to_float

**Определено в:** `app/utils/amount_math.py:4`

**Тип:** function

**Сигнатура:** `quants_to_float(quants, denominator)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### repos

**Определено в:** `tests/test_transaction_service.py:26`

**Тип:** function

**Сигнатура:** `repos(db)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### safe_eval

**Определено в:** `app/utils/expression_parser.py:14`

**Тип:** function

**Сигнатура:** `safe_eval(expr)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### search_usages_in_file

**Определено в:** `generate_function_usage_docs.py:95`

**Тип:** function

**Сигнатура:** `search_usages_in_file(filepath, function_name)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### service

**Определено в:** `tests/test_transaction_service.py:36`

**Тип:** function

**Сигнатура:** `service(repos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### set_column_visibility

**Определено в:** `app/ui/widgets/view_helpers.py:50`

**Тип:** function

**Сигнатура:** `set_column_visibility(view, col, checked)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### show_column_visibility_menu

**Определено в:** `app/ui/widgets/view_helpers.py:32`

**Тип:** function

**Сигнатура:** `show_column_visibility_menu(view, header, pos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_addition

**Определено в:** `tests/test_expression_parser.py:18`

**Тип:** function

**Сигнатура:** `test_addition()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_balanced_no_imbalance

**Определено в:** `tests/test_integrity_service.py:53`

**Тип:** function

**Сигнатура:** `test_balanced_no_imbalance(repos, integrity)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_cache_invalidation

**Определено в:** `tests/test_balance_service.py:84`

**Тип:** function

**Сигнатура:** `test_cache_invalidation(repos, balance_service)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_comma_as_decimal

**Определено в:** `tests/test_expression_parser.py:46`

**Тип:** function

**Сигнатура:** `test_comma_as_decimal()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_complex_expression

**Определено в:** `tests/test_expression_parser.py:42`

**Тип:** function

**Сигнатура:** `test_complex_expression()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_create_transaction

**Определено в:** `tests/test_transaction_service.py:40`

**Тип:** function

**Сигнатура:** `test_create_transaction(service, repos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_delete_split_and_rebalance

**Определено в:** `tests/test_transaction_service.py:163`

**Тип:** function

**Сигнатура:** `test_delete_split_and_rebalance(service, repos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_delete_transaction_cascades

**Определено в:** `tests/test_transaction_service.py:47`

**Тип:** function

**Сигнатура:** `test_delete_transaction_cascades(service, repos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_detects_empty_transactions

**Определено в:** `tests/test_integrity_service.py:63`

**Тип:** function

**Сигнатура:** `test_detects_empty_transactions(repos, integrity)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_detects_imbalance

**Определено в:** `tests/test_integrity_service.py:45`

**Тип:** function

**Сигнатура:** `test_detects_imbalance(repos, integrity)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_division

**Определено в:** `tests/test_expression_parser.py:30`

**Тип:** function

**Сигнатура:** `test_division()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_division_by_zero

**Определено в:** `tests/test_expression_parser.py:50`

**Тип:** function

**Сигнатура:** `test_division_by_zero()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_duplicate_transaction

**Определено в:** `tests/test_transaction_service.py:58`

**Тип:** function

**Сигнатура:** `test_duplicate_transaction(service, repos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_empty_account_balance

**Определено в:** `tests/test_balance_service.py:41`

**Тип:** function

**Сигнатура:** `test_empty_account_balance(repos, balance_service)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_empty_string

**Определено в:** `tests/test_expression_parser.py:60`

**Тип:** function

**Сигнатура:** `test_empty_string()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_float_number

**Определено в:** `tests/test_expression_parser.py:14`

**Тип:** function

**Сигнатура:** `test_float_number()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_grp_account_balance

**Определено в:** `tests/test_balance_service.py:70`

**Тип:** function

**Сигнатура:** `test_grp_account_balance(repos, balance_service)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_invalid_expression

**Определено в:** `tests/test_expression_parser.py:55`

**Тип:** function

**Сигнатура:** `test_invalid_expression()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_multi_currency_balance

**Определено в:** `tests/test_balance_service.py:57`

**Тип:** function

**Сигнатура:** `test_multi_currency_balance(repos, balance_service)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_multiplication

**Определено в:** `tests/test_expression_parser.py:26`

**Тип:** function

**Сигнатура:** `test_multiplication()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_negative

**Определено в:** `tests/test_expression_parser.py:38`

**Тип:** function

**Сигнатура:** `test_negative()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_no_empty_transactions_initially

**Определено в:** `tests/test_integrity_service.py:68`

**Тип:** function

**Сигнатура:** `test_no_empty_transactions_initially(integrity)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_no_imbalance_initially

**Определено в:** `tests/test_integrity_service.py:41`

**Тип:** function

**Сигнатура:** `test_no_imbalance_initially(integrity)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_parentheses

**Определено в:** `tests/test_expression_parser.py:34`

**Тип:** function

**Сигнатура:** `test_parentheses()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_recalculate_flexible_splits

**Определено в:** `tests/test_transaction_service.py:110`

**Тип:** function

**Сигнатура:** `test_recalculate_flexible_splits(service, repos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_recalculate_flexible_splits_rebalances_existing_imbalance

**Определено в:** `tests/test_transaction_service.py:132`

**Тип:** function

**Сигнатура:** `test_recalculate_flexible_splits_rebalances_existing_imbalance(service, repos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_recalculate_flexible_splits_returns_false_without_flexible_split

**Определено в:** `tests/test_transaction_service.py:150`

**Тип:** function

**Сигнатура:** `test_recalculate_flexible_splits_returns_false_without_flexible_split(service, repos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_reverse_transaction

**Определено в:** `tests/test_transaction_service.py:75`

**Тип:** function

**Сигнатура:** `test_reverse_transaction(service, repos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_simple_number

**Определено в:** `tests/test_expression_parser.py:10`

**Тип:** function

**Сигнатура:** `test_simple_number()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_single_currency_balance

**Определено в:** `tests/test_balance_service.py:47`

**Тип:** function

**Сигнатура:** `test_single_currency_balance(repos, balance_service)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_subtraction

**Определено в:** `tests/test_expression_parser.py:22`

**Тип:** function

**Сигнатура:** `test_subtraction()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_update_split_fixed

**Определено в:** `tests/test_transaction_service.py:92`

**Тип:** function

**Сигнатура:** `test_update_split_fixed(service, repos)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_whitespace

**Определено в:** `tests/test_expression_parser.py:64`

**Тип:** function

**Сигнатура:** `test_whitespace()`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### test_zero_split_detection

**Определено в:** `tests/test_integrity_service.py:72`

**Тип:** function

**Сигнатура:** `test_zero_split_detection(repos, integrity)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

#### tr

**Определено в:** `app/i18n/translator.py:4`

**Тип:** function

**Сигнатура:** `tr(text, context)`

**Использования:** Не найдены (возможно, неиспользуемая функция)

---

## Неиспользуемые функции

Найдено 132 неиспользуемых функций:

- **AccountNode.is_virtual** (`app/ui/item_models/account_tree_model.py:37`)
- **AccountTreeModel.dropMimeData** (`app/ui/item_models/account_tree_model.py:321`)
- **AccountTreeModel.get_node_by_account_id** (`app/ui/item_models/account_tree_model.py:356`)
- **AccountTreeModel.mimeData** (`app/ui/item_models/account_tree_model.py:309`)
- **AccountTreeModel.mimeTypes** (`app/ui/item_models/account_tree_model.py:306`)
- **AccountTreeModel.sort_key** (`app/ui/item_models/account_tree_model.py:327`)
- **AccountTreeModel.supportedDropActions** (`app/ui/item_models/account_tree_model.py:303`)
- **AccountTreeView._show_context_menu** (`app/ui/widgets/account_tree_view.py:162`)
- **AccountTreeView._show_header_menu** (`app/ui/widgets/account_tree_view.py:159`)
- **AccountTreeView._toggle_column** (`app/ui/widgets/account_tree_view.py:327`)
- **AccountTreeView.dragEnterEvent** (`app/ui/widgets/account_tree_view.py:263`)
- **AccountTreeView.dragMoveEvent** (`app/ui/widgets/account_tree_view.py:269`)
- **AccountTreeView.dropEvent** (`app/ui/widgets/account_tree_view.py:275`)
- **AmountDelegate.createEditor** (`app/ui/delegates/amount_delegate.py:33`)
- **AmountDelegate.setEditorData** (`app/ui/delegates/amount_delegate.py:38`)
- **AmountDelegate.setModelData** (`app/ui/delegates/amount_delegate.py:60`)
- **AmountDelegate.updateEditorGeometry** (`app/ui/delegates/amount_delegate.py:85`)
- **AppSettings.account_path_sep** (`app/settings/app_settings.py:45`)
- **AppSettings.allow_grouping_accounts_for_splits** (`app/settings/app_settings.py:64`)
- **AppSettings.date_format** (`app/settings/app_settings.py:33`)
- **AppSettings.decimal_sep** (`app/settings/app_settings.py:37`)
- **AppSettings.show_hidden_accounts** (`app/settings/app_settings.py:54`)
- **AppSettings.thousands_sep** (`app/settings/app_settings.py:41`)
- **AppSettings.transaction_view_mode** (`app/settings/app_settings.py:71`)
- **CurrencyEditorDialog._add_row** (`app/ui/dialogs/currency_editor_dialog.py:82`)
- **CurrencyEditorDialog._delete_row** (`app/ui/dialogs/currency_editor_dialog.py:85`)
- **CurrencyEditorDialog._save** (`app/ui/dialogs/currency_editor_dialog.py:99`)
- **DateDelegate.createEditor** (`app/ui/delegates/date_delegate.py:27`)
- **DateDelegate.setEditorData** (`app/ui/delegates/date_delegate.py:34`)
- **DateDelegate.setModelData** (`app/ui/delegates/date_delegate.py:52`)
- **DateDelegate.updateEditorGeometry** (`app/ui/delegates/date_delegate.py:67`)
- **DeleteAccountDialog._accept** (`app/ui/dialogs/delete_account_dialog.py:261`)
- **DeleteAccountDialog._update_transactions_combo** (`app/ui/dialogs/delete_account_dialog.py:240`)
- **DeleteAccountDialog.action** (`app/ui/dialogs/delete_account_dialog.py:290`)
- **DeleteAccountDialog.subaccounts_action** (`app/ui/dialogs/delete_account_dialog.py:294`)
- **DeleteAccountDialog.subaccounts_target_id** (`app/ui/dialogs/delete_account_dialog.py:298`)
- **DeleteAccountDialog.transactions_action** (`app/ui/dialogs/delete_account_dialog.py:302`)
- **DeleteAccountDialog.transactions_target_id** (`app/ui/dialogs/delete_account_dialog.py:306`)
- **DetailedFunctionAnalyzer.visit_AsyncFunctionDef** (`generate_detailed_function_usage.py:58`)
- **DetailedFunctionAnalyzer.visit_Attribute** (`generate_detailed_function_usage.py:154`)
- **DetailedFunctionAnalyzer.visit_Call** (`generate_detailed_function_usage.py:88`)
- **DetailedFunctionAnalyzer.visit_ClassDef** (`generate_detailed_function_usage.py:81`)
- **DetailedFunctionAnalyzer.visit_FunctionDef** (`generate_detailed_function_usage.py:34`)
- **DetailedFunctionAnalyzer.visit_Import** (`generate_detailed_function_usage.py:139`)
- **DetailedFunctionAnalyzer.visit_ImportFrom** (`generate_detailed_function_usage.py:146`)
- **DetailedFunctionAnalyzer.visit_Lambda** (`generate_detailed_function_usage.py:160`)
- **FunctionUsageAnalyzer.visit_AsyncFunctionDef** (`generate_function_usage_docs.py:34`)
- **FunctionUsageAnalyzer.visit_Call** (`generate_function_usage_docs.py:51`)
- **FunctionUsageAnalyzer.visit_ClassDef** (`generate_function_usage_docs.py:44`)
- **FunctionUsageAnalyzer.visit_FunctionDef** (`generate_function_usage_docs.py:24`)
- **FunctionUsageAnalyzer.visit_Import** (`generate_function_usage_docs.py:62`)
- **FunctionUsageAnalyzer.visit_ImportFrom** (`generate_function_usage_docs.py:68`)
- **MainWindow._focus_accounts** (`app/ui/main_window.py:489`)
- **MainWindow._focus_current_transaction_splits** (`app/ui/main_window.py:495`)
- **MainWindow._focus_transactions** (`app/ui/main_window.py:492`)
- **MainWindow._new_file** (`app/ui/main_window.py:843`)
- **MainWindow._on_accounts_selected** (`app/ui/main_window.py:512`)
- **MainWindow._on_new_transaction_requested** (`app/ui/main_window.py:329`)
- **MainWindow._on_split_data_changed** (`app/ui/main_window.py:664`)
- **MainWindow._on_trans_data_changed** (`app/ui/main_window.py:653`)
- **MainWindow._on_transaction_cleared** (`app/ui/main_window.py:543`)
- **MainWindow._on_transaction_selected** (`app/ui/main_window.py:549`)
- **MainWindow._on_transactions_changed** (`app/ui/main_window.py:557`)
- **MainWindow._on_virtual_node_selected** (`app/ui/main_window.py:519`)
- **MainWindow._open_currency_editor** (`app/ui/main_window.py:872`)
- **MainWindow._open_file** (`app/ui/main_window.py:851`)
- **MainWindow._open_settings** (`app/ui/main_window.py:877`)
- **MainWindow._toggle_allow_grouping_for_splits** (`app/ui/main_window.py:811`)
- **MainWindow._toggle_show_hidden** (`app/ui/main_window.py:806`)
- **SearchableComboDelegate.createEditor** (`app/ui/delegates/searchable_combo_delegate.py:21`)
- **SearchableComboDelegate.setEditorData** (`app/ui/delegates/searchable_combo_delegate.py:80`)
- **SearchableComboDelegate.setModelData** (`app/ui/delegates/searchable_combo_delegate.py:97`)
- **SearchableComboDelegate.updateEditorGeometry** (`app/ui/delegates/searchable_combo_delegate.py:109`)
- **SettingsDialog._save_and_accept** (`app/ui/dialogs/settings_dialog.py:55`)
- **SplitModel.set_filter** (`app/ui/item_models/split_model.py:510`)
- **SplitRepo.update_account** (`app/repositories/split_repo.py:58`)
- **SplitView._show_context_menu** (`app/ui/widgets/split_view.py:95`)
- **SplitView._show_header_menu** (`app/ui/widgets/split_view.py:120`)
- **SplitView._toggle_column** (`app/ui/widgets/split_view.py:123`)
- **StartupDialog._new** (`main.py:117`)
- **StartupDialog._open** (`main.py:108`)
- **TransactionModel.canFetchMore** (`app/ui/item_models/transaction_model.py:99`)
- **TransactionModel.fetchMore** (`app/ui/item_models/transaction_model.py:102`)
- **TransactionModel.set_filter** (`app/ui/item_models/transaction_model.py:308`)
- **TransactionService.delete_split** (`app/services/transaction_service.py:45`)
- **TransactionView._on_current_row_changed** (`app/ui/widgets/transaction_view.py:108`)
- **TransactionView._show_context_menu** (`app/ui/widgets/transaction_view.py:123`)
- **TransactionView._show_header_menu** (`app/ui/widgets/transaction_view.py:169`)
- **TransactionView._toggle_column** (`app/ui/widgets/transaction_view.py:172`)
- **UIEventLogger._on_focus_changed** (`app/ui/ui_event_logger.py:40`)
- **balance_service** (`tests/test_balance_service.py:37`)
- **db** (`tests/test_transaction_service.py:17`)
- **find_all_usages_with_context** (`generate_detailed_function_usage.py:182`)
- **integrity** (`tests/test_integrity_service.py:37`)
- **quants_to_float** (`app/utils/amount_math.py:4`)
- **repos** (`tests/test_transaction_service.py:26`)
- **search_usages_in_file** (`generate_function_usage_docs.py:95`)
- **service** (`tests/test_transaction_service.py:36`)
- **test_addition** (`tests/test_expression_parser.py:18`)
- **test_balanced_no_imbalance** (`tests/test_integrity_service.py:53`)
- **test_cache_invalidation** (`tests/test_balance_service.py:84`)
- **test_comma_as_decimal** (`tests/test_expression_parser.py:46`)
- **test_complex_expression** (`tests/test_expression_parser.py:42`)
- **test_create_transaction** (`tests/test_transaction_service.py:40`)
- **test_delete_split_and_rebalance** (`tests/test_transaction_service.py:163`)
- **test_delete_transaction_cascades** (`tests/test_transaction_service.py:47`)
- **test_detects_empty_transactions** (`tests/test_integrity_service.py:63`)
- **test_detects_imbalance** (`tests/test_integrity_service.py:45`)
- **test_division** (`tests/test_expression_parser.py:30`)
- **test_division_by_zero** (`tests/test_expression_parser.py:50`)
- **test_duplicate_transaction** (`tests/test_transaction_service.py:58`)
- **test_empty_account_balance** (`tests/test_balance_service.py:41`)
- **test_empty_string** (`tests/test_expression_parser.py:60`)
- **test_float_number** (`tests/test_expression_parser.py:14`)
- **test_grp_account_balance** (`tests/test_balance_service.py:70`)
- **test_invalid_expression** (`tests/test_expression_parser.py:55`)
- **test_multi_currency_balance** (`tests/test_balance_service.py:57`)
- **test_multiplication** (`tests/test_expression_parser.py:26`)
- **test_negative** (`tests/test_expression_parser.py:38`)
- **test_no_empty_transactions_initially** (`tests/test_integrity_service.py:68`)
- **test_no_imbalance_initially** (`tests/test_integrity_service.py:41`)
- **test_parentheses** (`tests/test_expression_parser.py:34`)
- **test_recalculate_flexible_splits** (`tests/test_transaction_service.py:110`)
- **test_recalculate_flexible_splits_rebalances_existing_imbalance** (`tests/test_transaction_service.py:132`)
- **test_recalculate_flexible_splits_returns_false_without_flexible_split** (`tests/test_transaction_service.py:150`)
- **test_reverse_transaction** (`tests/test_transaction_service.py:75`)
- **test_simple_number** (`tests/test_expression_parser.py:10`)
- **test_single_currency_balance** (`tests/test_balance_service.py:47`)
- **test_subtraction** (`tests/test_expression_parser.py:22`)
- **test_update_split_fixed** (`tests/test_transaction_service.py:92`)
- **test_whitespace** (`tests/test_expression_parser.py:64`)
- **test_zero_split_detection** (`tests/test_integrity_service.py:72`)