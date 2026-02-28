# Документация использования функций и методов
Дата создания: 2026-02-28
Всего функций/методов: 387

## Индекс функций

- [AccountComboDelegate.__init__](#accountcombodelegate---init--)
- [AccountComboDelegate._get_items](#accountcombodelegate--get-items)
- [AccountNode.is_virtual](#accountnode-is-virtual)
- [AccountRepo.__init__](#accountrepo---init--)
- [AccountRepo.delete](#accountrepo-delete)
- [AccountRepo.get_account_path](#accountrepo-get-account-path)
- [AccountRepo.get_all](#accountrepo-get-all)
- [AccountRepo.get_all_descendants](#accountrepo-get-all-descendants)
- [AccountRepo.get_balance](#accountrepo-get-balance)
- [AccountRepo.get_by_id](#accountrepo-get-by-id)
- [AccountRepo.get_children](#accountrepo-get-children)
- [AccountRepo.get_parent_id](#accountrepo-get-parent-id)
- [AccountRepo.get_transaction_ids_for_account](#accountrepo-get-transaction-ids-for-account)
- [AccountRepo.insert](#accountrepo-insert)
- [AccountRepo.move_splits_to_account](#accountrepo-move-splits-to-account)
- [AccountRepo.update](#accountrepo-update)
- [AccountRepo.update_hidden](#accountrepo-update-hidden)
- [AccountRepo.update_parent](#accountrepo-update-parent)
- [AccountTreeModel.__init__](#accounttreemodel---init--)
- [AccountTreeModel._add_virtual_nodes](#accounttreemodel--add-virtual-nodes)
- [AccountTreeModel._build_tree](#accounttreemodel--build-tree)
- [AccountTreeModel._format_balance](#accounttreemodel--format-balance)
- [AccountTreeModel._node_parent_index](#accounttreemodel--node-parent-index)
- [AccountTreeModel._remove_node_ids_recursive](#accounttreemodel--remove-node-ids-recursive)
- [AccountTreeModel._remove_node_subtree](#accounttreemodel--remove-node-subtree)
- [AccountTreeModel.columnCount](#accounttreemodel-columncount)
- [AccountTreeModel.data](#accounttreemodel-data)
- [AccountTreeModel.dropMimeData](#accounttreemodel-dropmimedata)
- [AccountTreeModel.flags](#accounttreemodel-flags)
- [AccountTreeModel.get_all_descendants](#accounttreemodel-get-all-descendants)
- [AccountTreeModel.get_index_for_account](#accounttreemodel-get-index-for-account)
- [AccountTreeModel.get_node](#accounttreemodel-get-node)
- [AccountTreeModel.get_node_by_account_id](#accounttreemodel-get-node-by-account-id)
- [AccountTreeModel.headerData](#accounttreemodel-headerdata)
- [AccountTreeModel.index](#accounttreemodel-index)
- [AccountTreeModel.mimeData](#accounttreemodel-mimedata)
- [AccountTreeModel.mimeTypes](#accounttreemodel-mimetypes)
- [AccountTreeModel.parent](#accounttreemodel-parent)
- [AccountTreeModel.reload](#accounttreemodel-reload)
- [AccountTreeModel.rowCount](#accounttreemodel-rowcount)
- [AccountTreeModel.setData](#accounttreemodel-setdata)
- [AccountTreeModel.set_virtual_nodes](#accounttreemodel-set-virtual-nodes)
- [AccountTreeModel.sort](#accounttreemodel-sort)
- [AccountTreeModel.sort_key](#accounttreemodel-sort-key)
- [AccountTreeModel.sort_recursive](#accounttreemodel-sort-recursive)
- [AccountTreeModel.supportedDropActions](#accounttreemodel-supporteddropactions)
- [AccountTreeView.__init__](#accounttreeview---init--)
- [AccountTreeView._add_account](#accounttreeview--add-account)
- [AccountTreeView._delete_account](#accounttreeview--delete-account)
- [AccountTreeView._delete_all_descendants](#accounttreeview--delete-all-descendants)
- [AccountTreeView._on_clicked](#accounttreeview--on-clicked)
- [AccountTreeView._on_selection_changed](#accounttreeview--on-selection-changed)
- [AccountTreeView._select_account_ids](#accounttreeview--select-account-ids)
- [AccountTreeView._show_context_menu](#accounttreeview--show-context-menu)
- [AccountTreeView._show_header_menu](#accounttreeview--show-header-menu)
- [AccountTreeView._toggle_column](#accounttreeview--toggle-column)
- [AccountTreeView._would_create_cycle](#accounttreeview--would-create-cycle)
- [AccountTreeView.dragEnterEvent](#accounttreeview-dragenterevent)
- [AccountTreeView.dragMoveEvent](#accounttreeview-dragmoveevent)
- [AccountTreeView.dropEvent](#accounttreeview-dropevent)
- [AccountTreeView.keyPressEvent](#accounttreeview-keypressevent)
- [AccountTreeView.moveCursor](#accounttreeview-movecursor)
- [AccountTreeView.setModel](#accounttreeview-setmodel)
- [AmountDelegate.__init__](#amountdelegate---init--)
- [AmountDelegate._preprocess](#amountdelegate--preprocess)
- [AmountDelegate.createEditor](#amountdelegate-createeditor)
- [AmountDelegate.eventFilter](#amountdelegate-eventfilter)
- [AmountDelegate.setEditorData](#amountdelegate-seteditordata)
- [AmountDelegate.setModelData](#amountdelegate-setmodeldata)
- [AmountDelegate.updateEditorGeometry](#amountdelegate-updateeditorgeometry)
- [AmountFormatter.__init__](#amountformatter---init--)
- [AmountFormatter.format_amount](#amountformatter-format-amount)
- [AmountFormatter.format_with_currency](#amountformatter-format-with-currency)
- [AppSettings.__init__](#appsettings---init--)
- [AppSettings.account_path_sep](#appsettings-account-path-sep)
- [AppSettings.allow_grouping_accounts_for_splits](#appsettings-allow-grouping-accounts-for-splits)
- [AppSettings.date_format](#appsettings-date-format)
- [AppSettings.decimal_sep](#appsettings-decimal-sep)
- [AppSettings.get](#appsettings-get)
- [AppSettings.set](#appsettings-set)
- [AppSettings.show_hidden_accounts](#appsettings-show-hidden-accounts)
- [AppSettings.thousands_sep](#appsettings-thousands-sep)
- [AppSettings.transaction_view_mode](#appsettings-transaction-view-mode)
- [BalanceService.__init__](#balanceservice---init--)
- [BalanceService._get_leaf_balance](#balanceservice--get-leaf-balance)
- [BalanceService.clear](#balanceservice-clear)
- [BalanceService.get_balance](#balanceservice-get-balance)
- [BalanceService.invalidate](#balanceservice-invalidate)
- [BalanceService.invalidate_account_tree](#balanceservice-invalidate-account-tree)
- [CurrencyComboDelegate.__init__](#currencycombodelegate---init--)
- [CurrencyComboDelegate._get_items](#currencycombodelegate--get-items)
- [CurrencyEditorDialog.__init__](#currencyeditordialog---init--)
- [CurrencyEditorDialog._add_row](#currencyeditordialog--add-row)
- [CurrencyEditorDialog._add_table_row](#currencyeditordialog--add-table-row)
- [CurrencyEditorDialog._build_ui](#currencyeditordialog--build-ui)
- [CurrencyEditorDialog._delete_row](#currencyeditordialog--delete-row)
- [CurrencyEditorDialog._load](#currencyeditordialog--load)
- [CurrencyEditorDialog._save](#currencyeditordialog--save)
- [CurrencyRepo.__init__](#currencyrepo---init--)
- [CurrencyRepo.delete](#currencyrepo-delete)
- [CurrencyRepo.get_all](#currencyrepo-get-all)
- [CurrencyRepo.get_by_id](#currencyrepo-get-by-id)
- [CurrencyRepo.insert](#currencyrepo-insert)
- [CurrencyRepo.is_used](#currencyrepo-is-used)
- [CurrencyRepo.update](#currencyrepo-update)
- [DateDelegate.__init__](#datedelegate---init--)
- [DateDelegate._local_tz](#datedelegate--local-tz)
- [DateDelegate._qt_format](#datedelegate--qt-format)
- [DateDelegate.createEditor](#datedelegate-createeditor)
- [DateDelegate.setEditorData](#datedelegate-seteditordata)
- [DateDelegate.setModelData](#datedelegate-setmodeldata)
- [DateDelegate.updateEditorGeometry](#datedelegate-updateeditorgeometry)
- [DeleteAccountDialog.__init__](#deleteaccountdialog---init--)
- [DeleteAccountDialog._accept](#deleteaccountdialog--accept)
- [DeleteAccountDialog._check_has_splits](#deleteaccountdialog--check-has-splits)
- [DeleteAccountDialog._check_has_subaccounts](#deleteaccountdialog--check-has-subaccounts)
- [DeleteAccountDialog._on_action_changed](#deleteaccountdialog--on-action-changed)
- [DeleteAccountDialog._populate_subaccounts_combo](#deleteaccountdialog--populate-subaccounts-combo)
- [DeleteAccountDialog._populate_transactions_combo](#deleteaccountdialog--populate-transactions-combo)
- [DeleteAccountDialog._update_transactions_combo](#deleteaccountdialog--update-transactions-combo)
- [DeleteAccountDialog.action](#deleteaccountdialog-action)
- [DeleteAccountDialog.subaccounts_action](#deleteaccountdialog-subaccounts-action)
- [DeleteAccountDialog.subaccounts_target_id](#deleteaccountdialog-subaccounts-target-id)
- [DeleteAccountDialog.transactions_action](#deleteaccountdialog-transactions-action)
- [DeleteAccountDialog.transactions_target_id](#deleteaccountdialog-transactions-target-id)
- [DisplaySettings.__init__](#displaysettings---init--)
- [DisplaySettings._key](#displaysettings--key)
- [DisplaySettings.get_column_order](#displaysettings-get-column-order)
- [DisplaySettings.get_column_widths](#displaysettings-get-column-widths)
- [DisplaySettings.get_hidden_columns](#displaysettings-get-hidden-columns)
- [DisplaySettings.get_sort_column](#displaysettings-get-sort-column)
- [DisplaySettings.get_sort_order](#displaysettings-get-sort-order)
- [DisplaySettings.set_column_order](#displaysettings-set-column-order)
- [DisplaySettings.set_column_widths](#displaysettings-set-column-widths)
- [DisplaySettings.set_hidden_columns](#displaysettings-set-hidden-columns)
- [DisplaySettings.set_sort_column](#displaysettings-set-sort-column)
- [DisplaySettings.set_sort_order](#displaysettings-set-sort-order)
- [FunctionUsageAnalyzer.__init__](#functionusageanalyzer---init--)
- [FunctionUsageAnalyzer.visit_AsyncFunctionDef](#functionusageanalyzer-visit-asyncfunctiondef)
- [FunctionUsageAnalyzer.visit_Call](#functionusageanalyzer-visit-call)
- [FunctionUsageAnalyzer.visit_ClassDef](#functionusageanalyzer-visit-classdef)
- [FunctionUsageAnalyzer.visit_FunctionDef](#functionusageanalyzer-visit-functiondef)
- [FunctionUsageAnalyzer.visit_Import](#functionusageanalyzer-visit-import)
- [FunctionUsageAnalyzer.visit_ImportFrom](#functionusageanalyzer-visit-importfrom)
- [IntegrityService.__init__](#integrityservice---init--)
- [IntegrityService.check_foreign_keys](#integrityservice-check-foreign-keys)
- [IntegrityService.get_empty_transactions](#integrityservice-get-empty-transactions)
- [IntegrityService.get_imbalanced_trans_ids](#integrityservice-get-imbalanced-trans-ids)
- [IntegrityService.get_zero_split_ids](#integrityservice-get-zero-split-ids)
- [IntegrityService.has_empty_transactions](#integrityservice-has-empty-transactions)
- [IntegrityService.has_imbalance](#integrityservice-has-imbalance)
- [MainWindow.__init__](#mainwindow---init--)
- [MainWindow._apply_display_settings](#mainwindow--apply-display-settings)
- [MainWindow._connect_signals](#mainwindow--connect-signals)
- [MainWindow._focus_accounts](#mainwindow--focus-accounts)
- [MainWindow._focus_current_transaction_splits](#mainwindow--focus-current-transaction-splits)
- [MainWindow._focus_split_cell](#mainwindow--focus-split-cell)
- [MainWindow._focus_transactions](#mainwindow--focus-transactions)
- [MainWindow._load_transactions](#mainwindow--load-transactions)
- [MainWindow._load_virtual_transactions](#mainwindow--load-virtual-transactions)
- [MainWindow._new_file](#mainwindow--new-file)
- [MainWindow._on_accounts_selected](#mainwindow--on-accounts-selected)
- [MainWindow._on_new_transaction_requested](#mainwindow--on-new-transaction-requested)
- [MainWindow._on_split_changed](#mainwindow--on-split-changed)
- [MainWindow._on_split_data_changed](#mainwindow--on-split-data-changed)
- [MainWindow._on_trans_data_changed](#mainwindow--on-trans-data-changed)
- [MainWindow._on_transaction_cleared](#mainwindow--on-transaction-cleared)
- [MainWindow._on_transaction_selected](#mainwindow--on-transaction-selected)
- [MainWindow._on_transactions_changed](#mainwindow--on-transactions-changed)
- [MainWindow._on_virtual_node_selected](#mainwindow--on-virtual-node-selected)
- [MainWindow._open_currency_editor](#mainwindow--open-currency-editor)
- [MainWindow._open_file](#mainwindow--open-file)
- [MainWindow._open_file_path](#mainwindow--open-file-path)
- [MainWindow._open_settings](#mainwindow--open-settings)
- [MainWindow._refresh_integrity](#mainwindow--refresh-integrity)
- [MainWindow._refresh_recent_menu](#mainwindow--refresh-recent-menu)
- [MainWindow._restore_view_settings](#mainwindow--restore-view-settings)
- [MainWindow._restore_window_layout](#mainwindow--restore-window-layout)
- [MainWindow._save_view_settings](#mainwindow--save-view-settings)
- [MainWindow._save_window_layout](#mainwindow--save-window-layout)
- [MainWindow._set_view_mode](#mainwindow--set-view-mode)
- [MainWindow._setup_delegates](#mainwindow--setup-delegates)
- [MainWindow._setup_menu](#mainwindow--setup-menu)
- [MainWindow._setup_models](#mainwindow--setup-models)
- [MainWindow._setup_ui](#mainwindow--setup-ui)
- [MainWindow._store_display_settings](#mainwindow--store-display-settings)
- [MainWindow._toggle_allow_grouping_for_splits](#mainwindow--toggle-allow-grouping-for-splits)
- [MainWindow._toggle_show_hidden](#mainwindow--toggle-show-hidden)
- [MainWindow.closeEvent](#mainwindow-closeevent)
- [SearchableComboDelegate.__init__](#searchablecombodelegate---init--)
- [SearchableComboDelegate._apply_current_completion](#searchablecombodelegate--apply-current-completion)
- [SearchableComboDelegate._extract_combo](#searchablecombodelegate--extract-combo)
- [SearchableComboDelegate._get_items](#searchablecombodelegate--get-items)
- [SearchableComboDelegate._sync_index_with_text](#searchablecombodelegate--sync-index-with-text)
- [SearchableComboDelegate.createEditor](#searchablecombodelegate-createeditor)
- [SearchableComboDelegate.eventFilter](#searchablecombodelegate-eventfilter)
- [SearchableComboDelegate.setEditorData](#searchablecombodelegate-seteditordata)
- [SearchableComboDelegate.setModelData](#searchablecombodelegate-setmodeldata)
- [SearchableComboDelegate.updateEditorGeometry](#searchablecombodelegate-updateeditorgeometry)
- [SettingsDialog.__init__](#settingsdialog---init--)
- [SettingsDialog._build_ui](#settingsdialog--build-ui)
- [SettingsDialog._save_and_accept](#settingsdialog--save-and-accept)
- [SplitModel.__init__](#splitmodel---init--)
- [SplitModel._add_phantom_rows](#splitmodel--add-phantom-rows)
- [SplitModel._currency_code](#splitmodel--currency-code)
- [SplitModel._edit_amt](#splitmodel--edit-amt)
- [SplitModel._enum_value](#splitmodel--enum-value)
- [SplitModel._format_amt](#splitmodel--format-amt)
- [SplitModel._to_checkstate](#splitmodel--to-checkstate)
- [SplitModel.columnCount](#splitmodel-columncount)
- [SplitModel.data](#splitmodel-data)
- [SplitModel.flags](#splitmodel-flags)
- [SplitModel.get_phantom_info](#splitmodel-get-phantom-info)
- [SplitModel.get_row_type](#splitmodel-get-row-type)
- [SplitModel.get_split](#splitmodel-get-split)
- [SplitModel.headerData](#splitmodel-headerdata)
- [SplitModel.key](#splitmodel-key)
- [SplitModel.load](#splitmodel-load)
- [SplitModel.rowCount](#splitmodel-rowcount)
- [SplitModel.setData](#splitmodel-setdata)
- [SplitModel.set_filter](#splitmodel-set-filter)
- [SplitModel.set_zero_split_ids](#splitmodel-set-zero-split-ids)
- [SplitModel.sort](#splitmodel-sort)
- [SplitRepo.__init__](#splitrepo---init--)
- [SplitRepo.delete](#splitrepo-delete)
- [SplitRepo.delete_by_account](#splitrepo-delete-by-account)
- [SplitRepo.get_balance_by_account](#splitrepo-get-balance-by-account)
- [SplitRepo.get_by_id](#splitrepo-get-by-id)
- [SplitRepo.get_by_transaction](#splitrepo-get-by-transaction)
- [SplitRepo.get_by_transaction_and_currency](#splitrepo-get-by-transaction-and-currency)
- [SplitRepo.get_last_currency_for_account](#splitrepo-get-last-currency-for-account)
- [SplitRepo.get_splits_with_zero_amount](#splitrepo-get-splits-with-zero-amount)
- [SplitRepo.has_splits_for_account](#splitrepo-has-splits-for-account)
- [SplitRepo.insert](#splitrepo-insert)
- [SplitRepo.update](#splitrepo-update)
- [SplitRepo.update_account](#splitrepo-update-account)
- [SplitRepo.update_amount](#splitrepo-update-amount)
- [SplitRepo.update_amount_fixed](#splitrepo-update-amount-fixed)
- [SplitView.__init__](#splitview---init--)
- [SplitView._delete_split](#splitview--delete-split)
- [SplitView._first_editable_in_row](#splitview--first-editable-in-row)
- [SplitView._show_context_menu](#splitview--show-context-menu)
- [SplitView._show_header_menu](#splitview--show-header-menu)
- [SplitView._toggle_column](#splitview--toggle-column)
- [SplitView.keyPressEvent](#splitview-keypressevent)
- [SplitView.mousePressEvent](#splitview-mousepressevent)
- [SplitView.moveCursor](#splitview-movecursor)
- [StartupDialog.__init__](#startupdialog---init--)
- [StartupDialog._new](#startupdialog--new)
- [StartupDialog._open](#startupdialog--open)
- [TransactionModel.__init__](#transactionmodel---init--)
- [TransactionModel._format_amt](#transactionmodel--format-amt)
- [TransactionModel._format_date](#transactionmodel--format-date)
- [TransactionModel._is_phantom_row](#transactionmodel--is-phantom-row)
- [TransactionModel._phantom_date](#transactionmodel--phantom-date)
- [TransactionModel.canFetchMore](#transactionmodel-canfetchmore)
- [TransactionModel.columnCount](#transactionmodel-columncount)
- [TransactionModel.data](#transactionmodel-data)
- [TransactionModel.fetchMore](#transactionmodel-fetchmore)
- [TransactionModel.find_row_for_trans](#transactionmodel-find-row-for-trans)
- [TransactionModel.flags](#transactionmodel-flags)
- [TransactionModel.get_trans_id](#transactionmodel-get-trans-id)
- [TransactionModel.headerData](#transactionmodel-headerdata)
- [TransactionModel.key](#transactionmodel-key)
- [TransactionModel.load](#transactionmodel-load)
- [TransactionModel.load_by_ids](#transactionmodel-load-by-ids)
- [TransactionModel.rowCount](#transactionmodel-rowcount)
- [TransactionModel.setData](#transactionmodel-setdata)
- [TransactionModel.set_filter](#transactionmodel-set-filter)
- [TransactionModel.sort](#transactionmodel-sort)
- [TransactionRepo.__init__](#transactionrepo---init--)
- [TransactionRepo._fetch_dicts_with_ids](#transactionrepo--fetch-dicts-with-ids)
- [TransactionRepo.delete](#transactionrepo-delete)
- [TransactionRepo.get_by_id](#transactionrepo-get-by-id)
- [TransactionRepo.get_empty](#transactionrepo-get-empty)
- [TransactionRepo.get_imbalanced](#transactionrepo-get-imbalanced)
- [TransactionRepo.get_summary_by_accounts](#transactionrepo-get-summary-by-accounts)
- [TransactionRepo.get_summary_by_ids](#transactionrepo-get-summary-by-ids)
- [TransactionRepo.get_verbose_by_accounts](#transactionrepo-get-verbose-by-accounts)
- [TransactionRepo.insert](#transactionrepo-insert)
- [TransactionRepo.update](#transactionrepo-update)
- [TransactionService.__init__](#transactionservice---init--)
- [TransactionService._copy_transaction](#transactionservice--copy-transaction)
- [TransactionService.add_split](#transactionservice-add-split)
- [TransactionService.create_transaction](#transactionservice-create-transaction)
- [TransactionService.delete_split](#transactionservice-delete-split)
- [TransactionService.delete_split_and_rebalance](#transactionservice-delete-split-and-rebalance)
- [TransactionService.delete_transaction](#transactionservice-delete-transaction)
- [TransactionService.duplicate_transaction](#transactionservice-duplicate-transaction)
- [TransactionService.recalculate_flexible_splits](#transactionservice-recalculate-flexible-splits)
- [TransactionService.reverse_transaction](#transactionservice-reverse-transaction)
- [TransactionService.update_split](#transactionservice-update-split)
- [TransactionService.update_split_fixed](#transactionservice-update-split-fixed)
- [TransactionService.update_transaction](#transactionservice-update-transaction)
- [TransactionView.__init__](#transactionview---init--)
- [TransactionView._delete](#transactionview--delete)
- [TransactionView._duplicate](#transactionview--duplicate)
- [TransactionView._on_clicked](#transactionview--on-clicked)
- [TransactionView._on_current_row_changed](#transactionview--on-current-row-changed)
- [TransactionView._reverse](#transactionview--reverse)
- [TransactionView._show_context_menu](#transactionview--show-context-menu)
- [TransactionView._show_header_menu](#transactionview--show-header-menu)
- [TransactionView._toggle_column](#transactionview--toggle-column)
- [TransactionView.closeEditor](#transactionview-closeeditor)
- [TransactionView.keyPressEvent](#transactionview-keypressevent)
- [TransactionView.moveCursor](#transactionview-movecursor)
- [TransactionView.setModel](#transactionview-setmodel)
- [UIEventLogger.__init__](#uieventlogger---init--)
- [UIEventLogger._describe_event](#uieventlogger--describe-event)
- [UIEventLogger._describe_key_event](#uieventlogger--describe-key-event)
- [UIEventLogger._describe_mouse_event](#uieventlogger--describe-mouse-event)
- [UIEventLogger._object_name](#uieventlogger--object-name)
- [UIEventLogger._on_focus_changed](#uieventlogger--on-focus-changed)
- [UIEventLogger._view_state](#uieventlogger--view-state)
- [UIEventLogger.eventFilter](#uieventlogger-eventfilter)
- [UIEventLogger.install](#uieventlogger-install)
- [_apply_pragmas](#-apply-pragmas)
- [_ask_file_path](#-ask-file-path)
- [_configure_logging](#-configure-logging)
- [_eval_node](#-eval-node)
- [_make_virtual_account](#-make-virtual-account)
- [_parse_args](#-parse-args)
- [_row_to_account](#-row-to-account)
- [_row_to_currency](#-row-to-currency)
- [_row_to_split](#-row-to-split)
- [_row_to_trans](#-row-to-trans)
- [_utc_now](#-utc-now)
- [add_recent_file](#add-recent-file)
- [analyze_codebase](#analyze-codebase)
- [analyze_file](#analyze-file)
- [balance_service](#balance-service)
- [compute_hidden_account_ids](#compute-hidden-account-ids)
- [db](#db)
- [ensure_schema](#ensure-schema)
- [find_next_editable_table_cell](#find-next-editable-table-cell)
- [float_to_quants](#float-to-quants)
- [generate_markdown_report](#generate-markdown-report)
- [get_last_file](#get-last-file)
- [get_recent_files](#get-recent-files)
- [get_selectable_account_items](#get-selectable-account-items)
- [integrity](#integrity)
- [main](#main)
- [mark_hidden_descendants](#mark-hidden-descendants)
- [open_connection](#open-connection)
- [qt_format_to_strftime](#qt-format-to-strftime)
- [quants_to_float](#quants-to-float)
- [repos](#repos)
- [safe_eval](#safe-eval)
- [search_usages_in_file](#search-usages-in-file)
- [service](#service)
- [set_column_visibility](#set-column-visibility)
- [show_column_visibility_menu](#show-column-visibility-menu)
- [test_addition](#test-addition)
- [test_balanced_no_imbalance](#test-balanced-no-imbalance)
- [test_cache_invalidation](#test-cache-invalidation)
- [test_comma_as_decimal](#test-comma-as-decimal)
- [test_complex_expression](#test-complex-expression)
- [test_create_transaction](#test-create-transaction)
- [test_delete_split_and_rebalance](#test-delete-split-and-rebalance)
- [test_delete_transaction_cascades](#test-delete-transaction-cascades)
- [test_detects_empty_transactions](#test-detects-empty-transactions)
- [test_detects_imbalance](#test-detects-imbalance)
- [test_division](#test-division)
- [test_division_by_zero](#test-division-by-zero)
- [test_duplicate_transaction](#test-duplicate-transaction)
- [test_empty_account_balance](#test-empty-account-balance)
- [test_empty_string](#test-empty-string)
- [test_float_number](#test-float-number)
- [test_grp_account_balance](#test-grp-account-balance)
- [test_invalid_expression](#test-invalid-expression)
- [test_multi_currency_balance](#test-multi-currency-balance)
- [test_multiplication](#test-multiplication)
- [test_negative](#test-negative)
- [test_no_empty_transactions_initially](#test-no-empty-transactions-initially)
- [test_no_imbalance_initially](#test-no-imbalance-initially)
- [test_parentheses](#test-parentheses)
- [test_recalculate_flexible_splits](#test-recalculate-flexible-splits)
- [test_recalculate_flexible_splits_rebalances_existing_imbalance](#test-recalculate-flexible-splits-rebalances-existing-imbalance)
- [test_recalculate_flexible_splits_returns_false_without_flexible_split](#test-recalculate-flexible-splits-returns-false-without-flexible-split)
- [test_reverse_transaction](#test-reverse-transaction)
- [test_simple_number](#test-simple-number)
- [test_single_currency_balance](#test-single-currency-balance)
- [test_subtraction](#test-subtraction)
- [test_update_split_fixed](#test-update-split-fixed)
- [test_whitespace](#test-whitespace)
- [test_zero_split_detection](#test-zero-split-detection)
- [tr](#tr)

---

## Подробный список

### AccountComboDelegate.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:11`

**Тип:** Метод класса `AccountComboDelegate`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### AccountComboDelegate._get_items

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:16`

**Тип:** Метод класса `AccountComboDelegate`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:25`

### AccountNode.is_virtual

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:37`

**Тип:** Метод класса `AccountNode`

**Использования:** Нет (возможно, неиспользуемая функция)

### AccountRepo.__init__

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:19`

**Тип:** Метод класса `AccountRepo`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### AccountRepo.delete

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:58`

**Тип:** Метод класса `AccountRepo`

**Использования (7 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:28`
- `/home/user/ChaosCash/app/services/transaction_service.py:46`
- `/home/user/ChaosCash/app/services/transaction_service.py:56`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:95`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:247`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:250`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:261`

### AccountRepo.get_account_path

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:84`

**Тип:** Метод класса `AccountRepo`

**Использования (7 мест):**

- `/home/user/ChaosCash/app/ui/account_selection.py:36`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:193`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:226`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:201`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:208`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:227`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:495`

### AccountRepo.get_all

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:23`

**Тип:** Метод класса `AccountRepo`

**Использования (9 мест):**

- `/home/user/ChaosCash/app/ui/account_selection.py:15`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:15`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:58`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:64`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:70`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:91`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:51`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:78`
- `/home/user/ChaosCash/app/ui/main_window.py:338`

### AccountRepo.get_all_descendants

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:75`

**Тип:** Метод класса `AccountRepo`

**Использования (7 мест):**

- `/home/user/ChaosCash/app/repositories/account_repo.py:81`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:173`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:187`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:218`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:376`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:115`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:231`

### AccountRepo.get_balance

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:62`

**Тип:** Метод класса `AccountRepo`

**Использования (10 мест):**

- `/home/user/ChaosCash/app/services/balance_service.py:39`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:188`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:334`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:336`
- `/home/user/ChaosCash/tests/test_balance_service.py:43`
- `/home/user/ChaosCash/tests/test_balance_service.py:53`
- `/home/user/ChaosCash/tests/test_balance_service.py:65`
- `/home/user/ChaosCash/tests/test_balance_service.py:80`
- `/home/user/ChaosCash/tests/test_balance_service.py:91`
- `/home/user/ChaosCash/tests/test_balance_service.py:99`

### AccountRepo.get_by_id

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:27`

**Тип:** Метод класса `AccountRepo`

**Использования (21 мест):**

- `/home/user/ChaosCash/app/repositories/account_repo.py:36`
- `/home/user/ChaosCash/app/repositories/account_repo.py:88`
- `/home/user/ChaosCash/app/repositories/account_repo.py:96`
- `/home/user/ChaosCash/app/services/amount_formatter.py:25`
- `/home/user/ChaosCash/app/services/amount_formatter.py:46`
- `/home/user/ChaosCash/app/services/transaction_service.py:50`
- `/home/user/ChaosCash/app/services/transaction_service.py:83`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:191`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:224`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:236`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:269`
- `/home/user/ChaosCash/app/ui/main_window.py:707`
- `/home/user/ChaosCash/app/ui/main_window.py:726`
- `/home/user/ChaosCash/app/ui/main_window.py:767`
- `/home/user/ChaosCash/tests/test_transaction_service.py:102`
- `/home/user/ChaosCash/tests/test_transaction_service.py:106`
- `/home/user/ChaosCash/tests/test_transaction_service.py:144`
- `/home/user/ChaosCash/tests/test_transaction_service.py:145`
- `/home/user/ChaosCash/tests/test_transaction_service.py:42`
- `/home/user/ChaosCash/tests/test_transaction_service.py:84`
- `/home/user/ChaosCash/tests/test_transaction_service.py:98`

### AccountRepo.get_children

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:31`

**Тип:** Метод класса `AccountRepo`

**Использования (6 мест):**

- `/home/user/ChaosCash/app/repositories/account_repo.py:78`
- `/home/user/ChaosCash/app/services/balance_service.py:26`
- `/home/user/ChaosCash/app/services/balance_service.py:38`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:166`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:221`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:258`

### AccountRepo.get_parent_id

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:35`

**Тип:** Метод класса `AccountRepo`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/services/balance_service.py:21`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:60`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:323`

### AccountRepo.get_transaction_ids_for_account

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:71`

**Тип:** Метод класса `AccountRepo`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:245`

### AccountRepo.insert

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:39`

**Тип:** Метод класса `AccountRepo`

**Использования (73 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:22`
- `/home/user/ChaosCash/app/services/transaction_service.py:33`
- `/home/user/ChaosCash/app/services/transaction_service.py:88`
- `/home/user/ChaosCash/app/services/transaction_service.py:90`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:114`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:190`
- `/home/user/ChaosCash/app/utils/recent_files.py:22`
- `/home/user/ChaosCash/main.py:8`
- `/home/user/ChaosCash/tests/test_balance_service.py:42`
- `/home/user/ChaosCash/tests/test_balance_service.py:48`
- `/home/user/ChaosCash/tests/test_balance_service.py:49`
- `/home/user/ChaosCash/tests/test_balance_service.py:50`
- `/home/user/ChaosCash/tests/test_balance_service.py:51`
- `/home/user/ChaosCash/tests/test_balance_service.py:58`
- `/home/user/ChaosCash/tests/test_balance_service.py:59`
- `/home/user/ChaosCash/tests/test_balance_service.py:6`
- `/home/user/ChaosCash/tests/test_balance_service.py:60`
- `/home/user/ChaosCash/tests/test_balance_service.py:61`
- `/home/user/ChaosCash/tests/test_balance_service.py:62`
- `/home/user/ChaosCash/tests/test_balance_service.py:63`
- `/home/user/ChaosCash/tests/test_balance_service.py:71`
- `/home/user/ChaosCash/tests/test_balance_service.py:72`
- `/home/user/ChaosCash/tests/test_balance_service.py:73`
- `/home/user/ChaosCash/tests/test_balance_service.py:74`
- `/home/user/ChaosCash/tests/test_balance_service.py:76`
- `/home/user/ChaosCash/tests/test_balance_service.py:77`
- `/home/user/ChaosCash/tests/test_balance_service.py:78`
- `/home/user/ChaosCash/tests/test_balance_service.py:85`
- `/home/user/ChaosCash/tests/test_balance_service.py:86`
- `/home/user/ChaosCash/tests/test_balance_service.py:87`
- `/home/user/ChaosCash/tests/test_balance_service.py:88`
- `/home/user/ChaosCash/tests/test_expression_parser.py:5`
- `/home/user/ChaosCash/tests/test_integrity_service.py:46`
- `/home/user/ChaosCash/tests/test_integrity_service.py:47`
- `/home/user/ChaosCash/tests/test_integrity_service.py:48`
- `/home/user/ChaosCash/tests/test_integrity_service.py:49`
- `/home/user/ChaosCash/tests/test_integrity_service.py:54`
- `/home/user/ChaosCash/tests/test_integrity_service.py:55`
- `/home/user/ChaosCash/tests/test_integrity_service.py:56`
- `/home/user/ChaosCash/tests/test_integrity_service.py:57`
- `/home/user/ChaosCash/tests/test_integrity_service.py:58`
- `/home/user/ChaosCash/tests/test_integrity_service.py:59`
- `/home/user/ChaosCash/tests/test_integrity_service.py:6`
- `/home/user/ChaosCash/tests/test_integrity_service.py:64`
- `/home/user/ChaosCash/tests/test_integrity_service.py:73`
- `/home/user/ChaosCash/tests/test_integrity_service.py:74`
- `/home/user/ChaosCash/tests/test_integrity_service.py:75`
- `/home/user/ChaosCash/tests/test_integrity_service.py:76`
- `/home/user/ChaosCash/tests/test_transaction_service.py:111`
- `/home/user/ChaosCash/tests/test_transaction_service.py:112`
- `/home/user/ChaosCash/tests/test_transaction_service.py:113`
- `/home/user/ChaosCash/tests/test_transaction_service.py:114`
- `/home/user/ChaosCash/tests/test_transaction_service.py:133`
- `/home/user/ChaosCash/tests/test_transaction_service.py:134`
- `/home/user/ChaosCash/tests/test_transaction_service.py:135`
- `/home/user/ChaosCash/tests/test_transaction_service.py:151`
- `/home/user/ChaosCash/tests/test_transaction_service.py:152`
- `/home/user/ChaosCash/tests/test_transaction_service.py:153`
- `/home/user/ChaosCash/tests/test_transaction_service.py:164`
- `/home/user/ChaosCash/tests/test_transaction_service.py:165`
- `/home/user/ChaosCash/tests/test_transaction_service.py:166`
- `/home/user/ChaosCash/tests/test_transaction_service.py:167`
- `/home/user/ChaosCash/tests/test_transaction_service.py:48`
- `/home/user/ChaosCash/tests/test_transaction_service.py:49`
- `/home/user/ChaosCash/tests/test_transaction_service.py:59`
- `/home/user/ChaosCash/tests/test_transaction_service.py:6`
- `/home/user/ChaosCash/tests/test_transaction_service.py:60`
- `/home/user/ChaosCash/tests/test_transaction_service.py:61`
- `/home/user/ChaosCash/tests/test_transaction_service.py:76`
- `/home/user/ChaosCash/tests/test_transaction_service.py:77`
- `/home/user/ChaosCash/tests/test_transaction_service.py:78`
- `/home/user/ChaosCash/tests/test_transaction_service.py:93`
- `/home/user/ChaosCash/tests/test_transaction_service.py:94`

### AccountRepo.move_splits_to_account

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:67`

**Тип:** Метод класса `AccountRepo`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:238`

### AccountRepo.update

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:45`

**Тип:** Метод класса `AccountRepo`

**Использования (6 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:25`
- `/home/user/ChaosCash/app/services/transaction_service.py:39`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:116`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:268`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:115`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:245`

### AccountRepo.update_hidden

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:54`

**Тип:** Метод класса `AccountRepo`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:235`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:214`

### AccountRepo.update_parent

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:50`

**Тип:** Метод класса `AccountRepo`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:223`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:306`

### AccountTreeModel.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:44`

**Тип:** Метод класса `AccountTreeModel`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### AccountTreeModel._add_virtual_nodes

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:96`

**Тип:** Метод класса `AccountTreeModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:66`

### AccountTreeModel._build_tree

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:69`

**Тип:** Метод класса `AccountTreeModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:65`

### AccountTreeModel._format_balance

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:185`

**Тип:** Метод класса `AccountTreeModel`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:168`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:172`

### AccountTreeModel._node_parent_index

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:276`

**Тип:** Метод класса `AccountTreeModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:291`

### AccountTreeModel._remove_node_ids_recursive

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:297`

**Тип:** Метод класса `AccountTreeModel`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:294`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:301`

### AccountTreeModel._remove_node_subtree

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:286`

**Тип:** Метод класса `AccountTreeModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:241`

### AccountTreeModel.columnCount

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:124`

**Тип:** Метод класса `AccountTreeModel`

**Использования (13 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:247`
- `/home/user/ChaosCash/app/ui/main_window.py:283`
- `/home/user/ChaosCash/app/ui/main_window.py:402`
- `/home/user/ChaosCash/app/ui/main_window.py:410`
- `/home/user/ChaosCash/app/ui/main_window.py:418`
- `/home/user/ChaosCash/app/ui/main_window.py:432`
- `/home/user/ChaosCash/app/ui/main_window.py:468`
- `/home/user/ChaosCash/app/ui/main_window.py:640`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:76`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:47`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:18`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:39`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:56`

### AccountTreeModel.data

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:147`

**Тип:** Метод класса `AccountTreeModel`

**Использования (21 мест):**

- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:39`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:65`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:35`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:63`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:72`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:81`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:87`
- `/home/user/ChaosCash/app/ui/main_window.py:659`
- `/home/user/ChaosCash/app/ui/main_window.py:660`
- `/home/user/ChaosCash/app/ui/main_window.py:685`
- `/home/user/ChaosCash/app/ui/main_window.py:699`
- `/home/user/ChaosCash/app/ui/main_window.py:700`
- `/home/user/ChaosCash/app/ui/main_window.py:701`
- `/home/user/ChaosCash/app/ui/main_window.py:732`
- `/home/user/ChaosCash/app/ui/main_window.py:748`
- `/home/user/ChaosCash/app/ui/main_window.py:749`
- `/home/user/ChaosCash/app/ui/main_window.py:750`
- `/home/user/ChaosCash/app/ui/main_window.py:751`
- `/home/user/ChaosCash/app/ui/main_window.py:752`
- `/home/user/ChaosCash/app/ui/main_window.py:754`

### AccountTreeModel.dropMimeData

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:321`

**Тип:** Метод класса `AccountTreeModel`

**Использования:** Нет (возможно, неиспользуемая функция)

### AccountTreeModel.flags

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:208`

**Тип:** Метод класса `AccountTreeModel`

**Использования (7 мест):**

- `/home/user/ChaosCash/app/ui/item_models/split_model.py:310`
- `/home/user/ChaosCash/app/ui/main_window.py:383`
- `/home/user/ChaosCash/app/ui/main_window.py:507`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:85`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:49`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:98`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:28`

### AccountTreeModel.get_all_descendants

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:366`

**Тип:** Метод класса `AccountTreeModel`

**Использования (7 мест):**

- `/home/user/ChaosCash/app/repositories/account_repo.py:81`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:173`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:187`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:218`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:376`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:115`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:231`

### AccountTreeModel.get_index_for_account

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:359`

**Тип:** Метод класса `AccountTreeModel`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:627`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:139`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:196`

### AccountTreeModel.get_node

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:113`

**Тип:** Метод класса `AccountTreeModel`

**Использования (10 мест):**

- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:314`
- `/home/user/ChaosCash/app/ui/main_window.py:616`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:111`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:152`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:173`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:186`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:203`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:287`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:292`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:91`

### AccountTreeModel.get_node_by_account_id

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:356`

**Тип:** Метод класса `AccountTreeModel`

**Использования:** Нет (возможно, неиспользуемая функция)

### AccountTreeModel.headerData

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:199`

**Тип:** Метод класса `AccountTreeModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:40`

### AccountTreeModel.index

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:127`

**Тип:** Метод класса `AccountTreeModel`

**Использования (34 мест):**

- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:145`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:283`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:290`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:363`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:117`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:118`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:251`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:266`
- `/home/user/ChaosCash/app/ui/main_window.py:362`
- `/home/user/ChaosCash/app/ui/main_window.py:382`
- `/home/user/ChaosCash/app/ui/main_window.py:502`
- `/home/user/ChaosCash/app/ui/main_window.py:506`
- `/home/user/ChaosCash/app/ui/main_window.py:508`
- `/home/user/ChaosCash/app/ui/main_window.py:597`
- `/home/user/ChaosCash/app/ui/main_window.py:605`
- `/home/user/ChaosCash/app/ui/main_window.py:615`
- `/home/user/ChaosCash/app/ui/main_window.py:641`
- `/home/user/ChaosCash/app/ui/main_window.py:659`
- `/home/user/ChaosCash/app/ui/main_window.py:660`
- `/home/user/ChaosCash/app/ui/main_window.py:685`
- `/home/user/ChaosCash/app/ui/main_window.py:699`
- `/home/user/ChaosCash/app/ui/main_window.py:700`
- `/home/user/ChaosCash/app/ui/main_window.py:701`
- `/home/user/ChaosCash/app/ui/main_window.py:732`
- `/home/user/ChaosCash/app/ui/main_window.py:748`
- `/home/user/ChaosCash/app/ui/main_window.py:749`
- `/home/user/ChaosCash/app/ui/main_window.py:750`
- `/home/user/ChaosCash/app/ui/main_window.py:751`
- `/home/user/ChaosCash/app/ui/main_window.py:752`
- `/home/user/ChaosCash/app/ui/main_window.py:754`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:84`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:48`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:97`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:27`

### AccountTreeModel.mimeData

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:309`

**Тип:** Метод класса `AccountTreeModel`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:264`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:270`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:277`

### AccountTreeModel.mimeTypes

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:306`

**Тип:** Метод класса `AccountTreeModel`

**Использования:** Нет (возможно, неиспользуемая функция)

### AccountTreeModel.parent

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:135`

**Тип:** Метод класса `AccountTreeModel`

**Использования (4 мест):**

- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:50`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:51`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:89`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:74`

### AccountTreeModel.reload

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:60`

**Тип:** Метод класса `AccountTreeModel`

**Использования (8 мест):**

- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:111`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:58`
- `/home/user/ChaosCash/app/ui/main_window.py:606`
- `/home/user/ChaosCash/app/ui/main_window.py:808`
- `/home/user/ChaosCash/app/ui/main_window.py:880`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:192`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:253`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:309`

### AccountTreeModel.rowCount

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:118`

**Тип:** Метод класса `AccountTreeModel`

**Использования (11 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:100`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:65`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:162`
- `/home/user/ChaosCash/app/ui/main_window.py:375`
- `/home/user/ChaosCash/app/ui/main_window.py:503`
- `/home/user/ChaosCash/app/ui/main_window.py:614`
- `/home/user/ChaosCash/app/ui/main_window.py:638`
- `/home/user/ChaosCash/app/ui/main_window.py:639`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:75`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:73`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:17`

### AccountTreeModel.setData

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:221`

**Тип:** Метод класса `AccountTreeModel`

**Использования (8 мест):**

- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:69`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:70`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:79`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:80`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:65`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:106`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:107`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:318`

### AccountTreeModel.set_virtual_nodes

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:106`

**Тип:** Метод класса `AccountTreeModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:823`

### AccountTreeModel.sort

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:324`

**Тип:** Метод класса `AccountTreeModel`

**Использования (5 мест):**

- `/home/user/ChaosCash/app/ui/account_selection.py:38`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:348`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:90`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:506`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:303`

### AccountTreeModel.sort_key

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:327`

**Тип:** Метод класса `AccountTreeModel`

**Использования:** Нет (возможно, неиспользуемая функция)

### AccountTreeModel.sort_recursive

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:347`

**Тип:** Метод класса `AccountTreeModel`

**Использования (4 мест):**

- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:350`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:353`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:92`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:94`

### AccountTreeModel.supportedDropActions

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:303`

**Тип:** Метод класса `AccountTreeModel`

**Использования:** Нет (возможно, неиспользуемая функция)

### AccountTreeView.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:26`

**Тип:** Метод класса `AccountTreeView`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### AccountTreeView._add_account

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:182`

**Тип:** Метод класса `AccountTreeView`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:183`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:169`

### AccountTreeView._delete_account

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:201`

**Тип:** Метод класса `AccountTreeView`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:177`

### AccountTreeView._delete_all_descendants

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:256`

**Тип:** Метод класса `AccountTreeView`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:226`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:260`

### AccountTreeView._on_clicked

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:89`

**Тип:** Метод класса `AccountTreeView`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:112`

### AccountTreeView._on_selection_changed

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:144`

**Тип:** Метод класса `AccountTreeView`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:123`

### AccountTreeView._select_account_ids

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:128`

**Тип:** Метод класса `AccountTreeView`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:118`

### AccountTreeView._show_context_menu

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:162`

**Тип:** Метод класса `AccountTreeView`

**Использования:** Нет (возможно, неиспользуемая функция)

### AccountTreeView._show_header_menu

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:159`

**Тип:** Метод класса `AccountTreeView`

**Использования:** Нет (возможно, неиспользуемая функция)

### AccountTreeView._toggle_column

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:327`

**Тип:** Метод класса `AccountTreeView`

**Использования:** Нет (возможно, неиспользуемая функция)

### AccountTreeView._would_create_cycle

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:313`

**Тип:** Метод класса `AccountTreeView`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:298`

### AccountTreeView.dragEnterEvent

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:263`

**Тип:** Метод класса `AccountTreeView`

**Использования:** Нет (возможно, неиспользуемая функция)

### AccountTreeView.dragMoveEvent

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:269`

**Тип:** Метод класса `AccountTreeView`

**Использования:** Нет (возможно, неиспользуемая функция)

### AccountTreeView.dropEvent

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:275`

**Тип:** Метод класса `AccountTreeView`

**Использования:** Нет (возможно, неиспользуемая функция)

### AccountTreeView.keyPressEvent

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:57`

**Тип:** Метод класса `AccountTreeView`

**Использования (7 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:59`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:65`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:57`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:62`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:80`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:53`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:63`

### AccountTreeView.moveCursor

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:67`

**Тип:** Метод класса `AccountTreeView`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:87`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:89`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:72`

### AccountTreeView.setModel

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:51`

**Тип:** Метод класса `AccountTreeView`

**Использования (5 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:243`
- `/home/user/ChaosCash/app/ui/main_window.py:261`
- `/home/user/ChaosCash/app/ui/main_window.py:279`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:52`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:46`

### AmountDelegate.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:11`

**Тип:** Метод класса `AmountDelegate`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### AmountDelegate._preprocess

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:16`

**Тип:** Метод класса `AmountDelegate`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:50`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:73`

### AmountDelegate.createEditor

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:33`

**Тип:** Метод класса `AmountDelegate`

**Использования:** Нет (возможно, неиспользуемая функция)

### AmountDelegate.eventFilter

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:43`

**Тип:** Метод класса `AmountDelegate`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:58`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:45`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:38`

### AmountDelegate.setEditorData

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:38`

**Тип:** Метод класса `AmountDelegate`

**Использования:** Нет (возможно, неиспользуемая функция)

### AmountDelegate.setModelData

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:60`

**Тип:** Метод класса `AmountDelegate`

**Использования:** Нет (возможно, неиспользуемая функция)

### AmountDelegate.updateEditorGeometry

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:85`

**Тип:** Метод класса `AmountDelegate`

**Использования:** Нет (возможно, неиспользуемая функция)

### AmountFormatter.__init__

**Определено в:** `/home/user/ChaosCash/app/services/amount_formatter.py:11`

**Тип:** Метод класса `AmountFormatter`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### AmountFormatter.format_amount

**Определено в:** `/home/user/ChaosCash/app/services/amount_formatter.py:15`

**Тип:** Метод класса `AmountFormatter`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/services/amount_formatter.py:47`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:173`

### AmountFormatter.format_with_currency

**Определено в:** `/home/user/ChaosCash/app/services/amount_formatter.py:36`

**Тип:** Метод класса `AmountFormatter`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:194`

### AppSettings.__init__

**Определено в:** `/home/user/ChaosCash/app/settings/app_settings.py:22`

**Тип:** Метод класса `AppSettings`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### AppSettings.account_path_sep

**Определено в:** `/home/user/ChaosCash/app/settings/app_settings.py:45`

**Тип:** Метод класса `AppSettings`

**Использования:** Нет (возможно, неиспользуемая функция)

### AppSettings.allow_grouping_accounts_for_splits

**Определено в:** `/home/user/ChaosCash/app/settings/app_settings.py:64`

**Тип:** Метод класса `AppSettings`

**Использования:** Нет (возможно, неиспользуемая функция)

### AppSettings.date_format

**Определено в:** `/home/user/ChaosCash/app/settings/app_settings.py:33`

**Тип:** Метод класса `AppSettings`

**Использования:** Нет (возможно, неиспользуемая функция)

### AppSettings.decimal_sep

**Определено в:** `/home/user/ChaosCash/app/settings/app_settings.py:37`

**Тип:** Метод класса `AppSettings`

**Использования:** Нет (возможно, неиспользуемая функция)

### AppSettings.get

**Определено в:** `/home/user/ChaosCash/app/settings/app_settings.py:25`

**Тип:** Метод класса `AppSettings`

**Использования (43 мест):**

- `/home/user/ChaosCash/app/settings/app_settings.py:26`
- `/home/user/ChaosCash/app/settings/app_settings.py:34`
- `/home/user/ChaosCash/app/settings/app_settings.py:38`
- `/home/user/ChaosCash/app/settings/app_settings.py:42`
- `/home/user/ChaosCash/app/settings/app_settings.py:46`
- `/home/user/ChaosCash/app/settings/app_settings.py:50`
- `/home/user/ChaosCash/app/settings/app_settings.py:60`
- `/home/user/ChaosCash/app/settings/app_settings.py:68`
- `/home/user/ChaosCash/app/ui/account_selection.py:33`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:357`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:360`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:368`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:166`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:181`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:377`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:183`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:185`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:187`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:189`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:190`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:193`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:194`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:197`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:201`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:203`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:211`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:241`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:246`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:249`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:256`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:261`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:264`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:273`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:278`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:289`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:291`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:293`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:295`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:297`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:299`
- `/home/user/ChaosCash/app/utils/account_hierarchy.py:16`

### AppSettings.set

**Определено в:** `/home/user/ChaosCash/app/settings/app_settings.py:28`

**Тип:** Метод класса `AppSettings`

**Использования (18 мест):**

- `/home/user/ChaosCash/app/settings/app_settings.py:55`
- `/home/user/ChaosCash/app/settings/app_settings.py:65`
- `/home/user/ChaosCash/app/settings/app_settings.py:72`
- `/home/user/ChaosCash/app/ui/account_selection.py:16`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:187`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:196`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:218`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:229`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:56`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:57`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:59`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:60`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:85`
- `/home/user/ChaosCash/app/ui/main_window.py:554`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:107`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:243`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:284`
- `/home/user/ChaosCash/generate_function_usage_docs.py:222`

### AppSettings.show_hidden_accounts

**Определено в:** `/home/user/ChaosCash/app/settings/app_settings.py:54`

**Тип:** Метод класса `AppSettings`

**Использования:** Нет (возможно, неиспользуемая функция)

### AppSettings.thousands_sep

**Определено в:** `/home/user/ChaosCash/app/settings/app_settings.py:41`

**Тип:** Метод класса `AppSettings`

**Использования:** Нет (возможно, неиспользуемая функция)

### AppSettings.transaction_view_mode

**Определено в:** `/home/user/ChaosCash/app/settings/app_settings.py:71`

**Тип:** Метод класса `AppSettings`

**Использования:** Нет (возможно, неиспользуемая функция)

### BalanceService.__init__

**Определено в:** `/home/user/ChaosCash/app/services/balance_service.py:10`

**Тип:** Метод класса `BalanceService`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### BalanceService._get_leaf_balance

**Определено в:** `/home/user/ChaosCash/app/services/balance_service.py:43`

**Тип:** Метод класса `BalanceService`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/services/balance_service.py:32`
- `/home/user/ChaosCash/app/services/balance_service.py:35`

### BalanceService.clear

**Определено в:** `/home/user/ChaosCash/app/services/balance_service.py:51`

**Тип:** Метод класса `BalanceService`

**Использования (11 мест):**

- `/home/user/ChaosCash/app/services/balance_service.py:52`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:186`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:212`
- `/home/user/ChaosCash/app/ui/main_window.py:364`
- `/home/user/ChaosCash/app/ui/main_window.py:560`
- `/home/user/ChaosCash/app/ui/main_window.py:578`
- `/home/user/ChaosCash/app/ui/main_window.py:835`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:191`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:252`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:308`
- `/home/user/ChaosCash/main.py:21`

### BalanceService.get_balance

**Определено в:** `/home/user/ChaosCash/app/services/balance_service.py:29`

**Тип:** Метод класса `BalanceService`

**Использования (10 мест):**

- `/home/user/ChaosCash/app/services/balance_service.py:39`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:188`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:334`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:336`
- `/home/user/ChaosCash/tests/test_balance_service.py:43`
- `/home/user/ChaosCash/tests/test_balance_service.py:53`
- `/home/user/ChaosCash/tests/test_balance_service.py:65`
- `/home/user/ChaosCash/tests/test_balance_service.py:80`
- `/home/user/ChaosCash/tests/test_balance_service.py:91`
- `/home/user/ChaosCash/tests/test_balance_service.py:99`

### BalanceService.invalidate

**Определено в:** `/home/user/ChaosCash/app/services/balance_service.py:16`

**Тип:** Метод класса `BalanceService`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/services/balance_service.py:25`
- `/home/user/ChaosCash/tests/test_balance_service.py:98`

### BalanceService.invalidate_account_tree

**Определено в:** `/home/user/ChaosCash/app/services/balance_service.py:23`

**Тип:** Метод класса `BalanceService`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/services/balance_service.py:27`

### CurrencyComboDelegate.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:10`

**Тип:** Метод класса `CurrencyComboDelegate`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### CurrencyComboDelegate._get_items

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:14`

**Тип:** Метод класса `CurrencyComboDelegate`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:25`

### CurrencyEditorDialog.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:21`

**Тип:** Метод класса `CurrencyEditorDialog`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### CurrencyEditorDialog._add_row

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:82`

**Тип:** Метод класса `CurrencyEditorDialog`

**Использования:** Нет (возможно, неиспользуемая функция)

### CurrencyEditorDialog._add_table_row

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:64`

**Тип:** Метод класса `CurrencyEditorDialog`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:62`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:83`

### CurrencyEditorDialog._build_ui

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:31`

**Тип:** Метод класса `CurrencyEditorDialog`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:28`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:17`

### CurrencyEditorDialog._delete_row

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:85`

**Тип:** Метод класса `CurrencyEditorDialog`

**Использования:** Нет (возможно, неиспользуемая функция)

### CurrencyEditorDialog._load

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:57`

**Тип:** Метод класса `CurrencyEditorDialog`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:29`

### CurrencyEditorDialog._save

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:99`

**Тип:** Метод класса `CurrencyEditorDialog`

**Использования:** Нет (возможно, неиспользуемая функция)

### CurrencyRepo.__init__

**Определено в:** `/home/user/ChaosCash/app/repositories/currency_repo.py:17`

**Тип:** Метод класса `CurrencyRepo`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### CurrencyRepo.delete

**Определено в:** `/home/user/ChaosCash/app/repositories/currency_repo.py:37`

**Тип:** Метод класса `CurrencyRepo`

**Использования (7 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:28`
- `/home/user/ChaosCash/app/services/transaction_service.py:46`
- `/home/user/ChaosCash/app/services/transaction_service.py:56`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:95`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:247`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:250`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:261`

### CurrencyRepo.get_all

**Определено в:** `/home/user/ChaosCash/app/repositories/currency_repo.py:20`

**Тип:** Метод класса `CurrencyRepo`

**Использования (9 мест):**

- `/home/user/ChaosCash/app/ui/account_selection.py:15`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:15`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:58`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:64`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:70`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:91`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:51`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:78`
- `/home/user/ChaosCash/app/ui/main_window.py:338`

### CurrencyRepo.get_by_id

**Определено в:** `/home/user/ChaosCash/app/repositories/currency_repo.py:24`

**Тип:** Метод класса `CurrencyRepo`

**Использования (21 мест):**

- `/home/user/ChaosCash/app/repositories/account_repo.py:36`
- `/home/user/ChaosCash/app/repositories/account_repo.py:88`
- `/home/user/ChaosCash/app/repositories/account_repo.py:96`
- `/home/user/ChaosCash/app/services/amount_formatter.py:25`
- `/home/user/ChaosCash/app/services/amount_formatter.py:46`
- `/home/user/ChaosCash/app/services/transaction_service.py:50`
- `/home/user/ChaosCash/app/services/transaction_service.py:83`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:191`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:224`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:236`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:269`
- `/home/user/ChaosCash/app/ui/main_window.py:707`
- `/home/user/ChaosCash/app/ui/main_window.py:726`
- `/home/user/ChaosCash/app/ui/main_window.py:767`
- `/home/user/ChaosCash/tests/test_transaction_service.py:102`
- `/home/user/ChaosCash/tests/test_transaction_service.py:106`
- `/home/user/ChaosCash/tests/test_transaction_service.py:144`
- `/home/user/ChaosCash/tests/test_transaction_service.py:145`
- `/home/user/ChaosCash/tests/test_transaction_service.py:42`
- `/home/user/ChaosCash/tests/test_transaction_service.py:84`
- `/home/user/ChaosCash/tests/test_transaction_service.py:98`

### CurrencyRepo.insert

**Определено в:** `/home/user/ChaosCash/app/repositories/currency_repo.py:28`

**Тип:** Метод класса `CurrencyRepo`

**Использования (73 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:22`
- `/home/user/ChaosCash/app/services/transaction_service.py:33`
- `/home/user/ChaosCash/app/services/transaction_service.py:88`
- `/home/user/ChaosCash/app/services/transaction_service.py:90`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:114`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:190`
- `/home/user/ChaosCash/app/utils/recent_files.py:22`
- `/home/user/ChaosCash/main.py:8`
- `/home/user/ChaosCash/tests/test_balance_service.py:42`
- `/home/user/ChaosCash/tests/test_balance_service.py:48`
- `/home/user/ChaosCash/tests/test_balance_service.py:49`
- `/home/user/ChaosCash/tests/test_balance_service.py:50`
- `/home/user/ChaosCash/tests/test_balance_service.py:51`
- `/home/user/ChaosCash/tests/test_balance_service.py:58`
- `/home/user/ChaosCash/tests/test_balance_service.py:59`
- `/home/user/ChaosCash/tests/test_balance_service.py:6`
- `/home/user/ChaosCash/tests/test_balance_service.py:60`
- `/home/user/ChaosCash/tests/test_balance_service.py:61`
- `/home/user/ChaosCash/tests/test_balance_service.py:62`
- `/home/user/ChaosCash/tests/test_balance_service.py:63`
- `/home/user/ChaosCash/tests/test_balance_service.py:71`
- `/home/user/ChaosCash/tests/test_balance_service.py:72`
- `/home/user/ChaosCash/tests/test_balance_service.py:73`
- `/home/user/ChaosCash/tests/test_balance_service.py:74`
- `/home/user/ChaosCash/tests/test_balance_service.py:76`
- `/home/user/ChaosCash/tests/test_balance_service.py:77`
- `/home/user/ChaosCash/tests/test_balance_service.py:78`
- `/home/user/ChaosCash/tests/test_balance_service.py:85`
- `/home/user/ChaosCash/tests/test_balance_service.py:86`
- `/home/user/ChaosCash/tests/test_balance_service.py:87`
- `/home/user/ChaosCash/tests/test_balance_service.py:88`
- `/home/user/ChaosCash/tests/test_expression_parser.py:5`
- `/home/user/ChaosCash/tests/test_integrity_service.py:46`
- `/home/user/ChaosCash/tests/test_integrity_service.py:47`
- `/home/user/ChaosCash/tests/test_integrity_service.py:48`
- `/home/user/ChaosCash/tests/test_integrity_service.py:49`
- `/home/user/ChaosCash/tests/test_integrity_service.py:54`
- `/home/user/ChaosCash/tests/test_integrity_service.py:55`
- `/home/user/ChaosCash/tests/test_integrity_service.py:56`
- `/home/user/ChaosCash/tests/test_integrity_service.py:57`
- `/home/user/ChaosCash/tests/test_integrity_service.py:58`
- `/home/user/ChaosCash/tests/test_integrity_service.py:59`
- `/home/user/ChaosCash/tests/test_integrity_service.py:6`
- `/home/user/ChaosCash/tests/test_integrity_service.py:64`
- `/home/user/ChaosCash/tests/test_integrity_service.py:73`
- `/home/user/ChaosCash/tests/test_integrity_service.py:74`
- `/home/user/ChaosCash/tests/test_integrity_service.py:75`
- `/home/user/ChaosCash/tests/test_integrity_service.py:76`
- `/home/user/ChaosCash/tests/test_transaction_service.py:111`
- `/home/user/ChaosCash/tests/test_transaction_service.py:112`
- `/home/user/ChaosCash/tests/test_transaction_service.py:113`
- `/home/user/ChaosCash/tests/test_transaction_service.py:114`
- `/home/user/ChaosCash/tests/test_transaction_service.py:133`
- `/home/user/ChaosCash/tests/test_transaction_service.py:134`
- `/home/user/ChaosCash/tests/test_transaction_service.py:135`
- `/home/user/ChaosCash/tests/test_transaction_service.py:151`
- `/home/user/ChaosCash/tests/test_transaction_service.py:152`
- `/home/user/ChaosCash/tests/test_transaction_service.py:153`
- `/home/user/ChaosCash/tests/test_transaction_service.py:164`
- `/home/user/ChaosCash/tests/test_transaction_service.py:165`
- `/home/user/ChaosCash/tests/test_transaction_service.py:166`
- `/home/user/ChaosCash/tests/test_transaction_service.py:167`
- `/home/user/ChaosCash/tests/test_transaction_service.py:48`
- `/home/user/ChaosCash/tests/test_transaction_service.py:49`
- `/home/user/ChaosCash/tests/test_transaction_service.py:59`
- `/home/user/ChaosCash/tests/test_transaction_service.py:6`
- `/home/user/ChaosCash/tests/test_transaction_service.py:60`
- `/home/user/ChaosCash/tests/test_transaction_service.py:61`
- `/home/user/ChaosCash/tests/test_transaction_service.py:76`
- `/home/user/ChaosCash/tests/test_transaction_service.py:77`
- `/home/user/ChaosCash/tests/test_transaction_service.py:78`
- `/home/user/ChaosCash/tests/test_transaction_service.py:93`
- `/home/user/ChaosCash/tests/test_transaction_service.py:94`

### CurrencyRepo.is_used

**Определено в:** `/home/user/ChaosCash/app/repositories/currency_repo.py:41`

**Тип:** Метод класса `CurrencyRepo`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:90`

### CurrencyRepo.update

**Определено в:** `/home/user/ChaosCash/app/repositories/currency_repo.py:33`

**Тип:** Метод класса `CurrencyRepo`

**Использования (6 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:25`
- `/home/user/ChaosCash/app/services/transaction_service.py:39`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:116`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:268`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:115`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:245`

### DateDelegate.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:13`

**Тип:** Метод класса `DateDelegate`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### DateDelegate._local_tz

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:21`

**Тип:** Метод класса `DateDelegate`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:39`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:57`

### DateDelegate._qt_format

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:18`

**Тип:** Метод класса `DateDelegate`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:30`

### DateDelegate.createEditor

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:27`

**Тип:** Метод класса `DateDelegate`

**Использования:** Нет (возможно, неиспользуемая функция)

### DateDelegate.setEditorData

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:34`

**Тип:** Метод класса `DateDelegate`

**Использования:** Нет (возможно, неиспользуемая функция)

### DateDelegate.setModelData

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:52`

**Тип:** Метод класса `DateDelegate`

**Использования:** Нет (возможно, неиспользуемая функция)

### DateDelegate.updateEditorGeometry

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:67`

**Тип:** Метод класса `DateDelegate`

**Использования:** Нет (возможно, неиспользуемая функция)

### DeleteAccountDialog.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:39`

**Тип:** Метод класса `DeleteAccountDialog`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### DeleteAccountDialog._accept

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:261`

**Тип:** Метод класса `DeleteAccountDialog`

**Использования:** Нет (возможно, неиспользуемая функция)

### DeleteAccountDialog._check_has_splits

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:169`

**Тип:** Метод класса `DeleteAccountDialog`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:57`

### DeleteAccountDialog._check_has_subaccounts

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:164`

**Тип:** Метод класса `DeleteAccountDialog`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:56`

### DeleteAccountDialog._on_action_changed

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:244`

**Тип:** Метод класса `DeleteAccountDialog`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:162`

### DeleteAccountDialog._populate_subaccounts_combo

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:181`

**Тип:** Метод класса `DeleteAccountDialog`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:96`

### DeleteAccountDialog._populate_transactions_combo

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:207`

**Тип:** Метод класса `DeleteAccountDialog`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:132`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:242`

### DeleteAccountDialog._update_transactions_combo

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:240`

**Тип:** Метод класса `DeleteAccountDialog`

**Использования:** Нет (возможно, неиспользуемая функция)

### DeleteAccountDialog.action

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:290`

**Тип:** Метод класса `DeleteAccountDialog`

**Использования:** Нет (возможно, неиспользуемая функция)

### DeleteAccountDialog.subaccounts_action

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:294`

**Тип:** Метод класса `DeleteAccountDialog`

**Использования:** Нет (возможно, неиспользуемая функция)

### DeleteAccountDialog.subaccounts_target_id

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:298`

**Тип:** Метод класса `DeleteAccountDialog`

**Использования:** Нет (возможно, неиспользуемая функция)

### DeleteAccountDialog.transactions_action

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:302`

**Тип:** Метод класса `DeleteAccountDialog`

**Использования:** Нет (возможно, неиспользуемая функция)

### DeleteAccountDialog.transactions_target_id

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:306`

**Тип:** Метод класса `DeleteAccountDialog`

**Использования:** Нет (возможно, неиспользуемая функция)

### DisplaySettings.__init__

**Определено в:** `/home/user/ChaosCash/app/settings/display_settings.py:11`

**Тип:** Метод класса `DisplaySettings`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### DisplaySettings._key

**Определено в:** `/home/user/ChaosCash/app/settings/display_settings.py:15`

**Тип:** Метод класса `DisplaySettings`

**Использования (10 мест):**

- `/home/user/ChaosCash/app/settings/display_settings.py:19`
- `/home/user/ChaosCash/app/settings/display_settings.py:25`
- `/home/user/ChaosCash/app/settings/display_settings.py:28`
- `/home/user/ChaosCash/app/settings/display_settings.py:34`
- `/home/user/ChaosCash/app/settings/display_settings.py:37`
- `/home/user/ChaosCash/app/settings/display_settings.py:43`
- `/home/user/ChaosCash/app/settings/display_settings.py:46`
- `/home/user/ChaosCash/app/settings/display_settings.py:49`
- `/home/user/ChaosCash/app/settings/display_settings.py:52`
- `/home/user/ChaosCash/app/settings/display_settings.py:55`

### DisplaySettings.get_column_order

**Определено в:** `/home/user/ChaosCash/app/settings/display_settings.py:18`

**Тип:** Метод класса `DisplaySettings`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:434`

### DisplaySettings.get_column_widths

**Определено в:** `/home/user/ChaosCash/app/settings/display_settings.py:27`

**Тип:** Метод класса `DisplaySettings`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:447`

### DisplaySettings.get_hidden_columns

**Определено в:** `/home/user/ChaosCash/app/settings/display_settings.py:36`

**Тип:** Метод класса `DisplaySettings`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:441`

### DisplaySettings.get_sort_column

**Определено в:** `/home/user/ChaosCash/app/settings/display_settings.py:45`

**Тип:** Метод класса `DisplaySettings`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:452`

### DisplaySettings.get_sort_order

**Определено в:** `/home/user/ChaosCash/app/settings/display_settings.py:51`

**Тип:** Метод класса `DisplaySettings`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:454`

### DisplaySettings.set_column_order

**Определено в:** `/home/user/ChaosCash/app/settings/display_settings.py:24`

**Тип:** Метод класса `DisplaySettings`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:473`

### DisplaySettings.set_column_widths

**Определено в:** `/home/user/ChaosCash/app/settings/display_settings.py:33`

**Тип:** Метод класса `DisplaySettings`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:475`

### DisplaySettings.set_hidden_columns

**Определено в:** `/home/user/ChaosCash/app/settings/display_settings.py:42`

**Тип:** Метод класса `DisplaySettings`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:474`

### DisplaySettings.set_sort_column

**Определено в:** `/home/user/ChaosCash/app/settings/display_settings.py:48`

**Тип:** Метод класса `DisplaySettings`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:476`

### DisplaySettings.set_sort_order

**Определено в:** `/home/user/ChaosCash/app/settings/display_settings.py:54`

**Тип:** Метод класса `DisplaySettings`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:477`

### FunctionUsageAnalyzer.__init__

**Определено в:** `/home/user/ChaosCash/generate_function_usage_docs.py:17`

**Тип:** Метод класса `FunctionUsageAnalyzer`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### FunctionUsageAnalyzer.visit_AsyncFunctionDef

**Определено в:** `/home/user/ChaosCash/generate_function_usage_docs.py:34`

**Тип:** Метод класса `FunctionUsageAnalyzer`

**Использования:** Нет (возможно, неиспользуемая функция)

### FunctionUsageAnalyzer.visit_Call

**Определено в:** `/home/user/ChaosCash/generate_function_usage_docs.py:51`

**Тип:** Метод класса `FunctionUsageAnalyzer`

**Использования:** Нет (возможно, неиспользуемая функция)

### FunctionUsageAnalyzer.visit_ClassDef

**Определено в:** `/home/user/ChaosCash/generate_function_usage_docs.py:44`

**Тип:** Метод класса `FunctionUsageAnalyzer`

**Использования:** Нет (возможно, неиспользуемая функция)

### FunctionUsageAnalyzer.visit_FunctionDef

**Определено в:** `/home/user/ChaosCash/generate_function_usage_docs.py:24`

**Тип:** Метод класса `FunctionUsageAnalyzer`

**Использования:** Нет (возможно, неиспользуемая функция)

### FunctionUsageAnalyzer.visit_Import

**Определено в:** `/home/user/ChaosCash/generate_function_usage_docs.py:62`

**Тип:** Метод класса `FunctionUsageAnalyzer`

**Использования:** Нет (возможно, неиспользуемая функция)

### FunctionUsageAnalyzer.visit_ImportFrom

**Определено в:** `/home/user/ChaosCash/generate_function_usage_docs.py:68`

**Тип:** Метод класса `FunctionUsageAnalyzer`

**Использования:** Нет (возможно, неиспользуемая функция)

### IntegrityService.__init__

**Определено в:** `/home/user/ChaosCash/app/services/integrity_service.py:9`

**Тип:** Метод класса `IntegrityService`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### IntegrityService.check_foreign_keys

**Определено в:** `/home/user/ChaosCash/app/services/integrity_service.py:28`

**Тип:** Метод класса `IntegrityService`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:827`

### IntegrityService.get_empty_transactions

**Определено в:** `/home/user/ChaosCash/app/services/integrity_service.py:20`

**Тип:** Метод класса `IntegrityService`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/services/integrity_service.py:37`
- `/home/user/ChaosCash/app/ui/main_window.py:535`
- `/home/user/ChaosCash/app/ui/main_window.py:588`

### IntegrityService.get_imbalanced_trans_ids

**Определено в:** `/home/user/ChaosCash/app/services/integrity_service.py:15`

**Тип:** Метод класса `IntegrityService`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/services/integrity_service.py:34`
- `/home/user/ChaosCash/app/ui/main_window.py:533`
- `/home/user/ChaosCash/app/ui/main_window.py:586`

### IntegrityService.get_zero_split_ids

**Определено в:** `/home/user/ChaosCash/app/services/integrity_service.py:24`

**Тип:** Метод класса `IntegrityService`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:554`
- `/home/user/ChaosCash/tests/test_integrity_service.py:77`

### IntegrityService.has_empty_transactions

**Определено в:** `/home/user/ChaosCash/app/services/integrity_service.py:36`

**Тип:** Метод класса `IntegrityService`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:822`
- `/home/user/ChaosCash/tests/test_integrity_service.py:65`
- `/home/user/ChaosCash/tests/test_integrity_service.py:69`

### IntegrityService.has_imbalance

**Определено в:** `/home/user/ChaosCash/app/services/integrity_service.py:33`

**Тип:** Метод класса `IntegrityService`

**Использования (4 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:821`
- `/home/user/ChaosCash/tests/test_integrity_service.py:42`
- `/home/user/ChaosCash/tests/test_integrity_service.py:50`
- `/home/user/ChaosCash/tests/test_integrity_service.py:60`

### MainWindow.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:51`

**Тип:** Метод класса `MainWindow`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### MainWindow._apply_display_settings

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:425`

**Тип:** Метод класса `MainWindow`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:400`
- `/home/user/ChaosCash/app/ui/main_window.py:408`
- `/home/user/ChaosCash/app/ui/main_window.py:416`

### MainWindow._connect_signals

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:310`

**Тип:** Метод класса `MainWindow`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:88`

### MainWindow._focus_accounts

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:489`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._focus_current_transaction_splits

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:495`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._focus_split_cell

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:370`

**Тип:** Метод класса `MainWindow`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:368`
- `/home/user/ChaosCash/app/ui/main_window.py:651`

### MainWindow._focus_transactions

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:492`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._load_transactions

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:525`

**Тип:** Метод класса `MainWindow`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:517`
- `/home/user/ChaosCash/app/ui/main_window.py:562`
- `/home/user/ChaosCash/app/ui/main_window.py:818`

### MainWindow._load_virtual_transactions

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:530`

**Тип:** Метод класса `MainWindow`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:523`

### MainWindow._new_file

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:843`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._on_accounts_selected

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:512`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._on_new_transaction_requested

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:329`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._on_split_changed

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:564`

**Тип:** Метод класса `MainWindow`

**Использования (5 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:695`
- `/home/user/ChaosCash/app/ui/main_window.py:718`
- `/home/user/ChaosCash/app/ui/main_window.py:744`
- `/home/user/ChaosCash/app/ui/main_window.py:804`
- `/home/user/ChaosCash/app/ui/main_window.py:875`

### MainWindow._on_split_data_changed

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:664`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._on_trans_data_changed

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:653`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._on_transaction_cleared

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:543`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._on_transaction_selected

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:549`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._on_transactions_changed

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:557`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._on_virtual_node_selected

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:519`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._open_currency_editor

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:872`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._open_file

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:851`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._open_file_path

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:859`

**Тип:** Метод класса `MainWindow`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:838`
- `/home/user/ChaosCash/app/ui/main_window.py:849`
- `/home/user/ChaosCash/app/ui/main_window.py:857`

### MainWindow._open_settings

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:877`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._refresh_integrity

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:820`

**Тип:** Метод класса `MainWindow`

**Использования (4 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:365`
- `/home/user/ChaosCash/app/ui/main_window.py:561`
- `/home/user/ChaosCash/app/ui/main_window.py:579`
- `/home/user/ChaosCash/app/ui/main_window.py:89`

### MainWindow._refresh_recent_menu

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:834`

**Тип:** Метод класса `MainWindow`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:178`

### MainWindow._restore_view_settings

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:399`

**Тип:** Метод класса `MainWindow`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:293`

### MainWindow._restore_window_layout

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:387`

**Тип:** Метод класса `MainWindow`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:94`

### MainWindow._save_view_settings

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:459`

**Тип:** Метод класса `MainWindow`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:888`

### MainWindow._save_window_layout

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:479`

**Тип:** Метод класса `MainWindow`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:889`

### MainWindow._set_view_mode

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:814`

**Тип:** Метод класса `MainWindow`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:221`
- `/home/user/ChaosCash/app/ui/main_window.py:222`

### MainWindow._setup_delegates

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:295`

**Тип:** Метод класса `MainWindow`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:87`

### MainWindow._setup_menu

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:159`

**Тип:** Метод класса `MainWindow`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:85`

### MainWindow._setup_models

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:237`

**Тип:** Метод класса `MainWindow`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:86`

### MainWindow._setup_ui

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:98`

**Тип:** Метод класса `MainWindow`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:84`

### MainWindow._store_display_settings

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:464`

**Тип:** Метод класса `MainWindow`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:460`
- `/home/user/ChaosCash/app/ui/main_window.py:461`
- `/home/user/ChaosCash/app/ui/main_window.py:462`

### MainWindow._toggle_allow_grouping_for_splits

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:811`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow._toggle_show_hidden

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:806`

**Тип:** Метод класса `MainWindow`

**Использования:** Нет (возможно, неиспользуемая функция)

### MainWindow.closeEvent

**Определено в:** `/home/user/ChaosCash/app/ui/main_window.py:887`

**Тип:** Метод класса `MainWindow`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:894`

### SearchableComboDelegate.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:13`

**Тип:** Метод класса `SearchableComboDelegate`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### SearchableComboDelegate._apply_current_completion

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:63`

**Тип:** Метод класса `SearchableComboDelegate`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:41`

### SearchableComboDelegate._extract_combo

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:47`

**Тип:** Метод класса `SearchableComboDelegate`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:39`

### SearchableComboDelegate._get_items

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:17`

**Тип:** Метод класса `SearchableComboDelegate`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:25`

### SearchableComboDelegate._sync_index_with_text

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:54`

**Тип:** Метод класса `SearchableComboDelegate`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:78`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:98`

### SearchableComboDelegate.createEditor

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:21`

**Тип:** Метод класса `SearchableComboDelegate`

**Использования:** Нет (возможно, неиспользуемая функция)

### SearchableComboDelegate.eventFilter

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:37`

**Тип:** Метод класса `SearchableComboDelegate`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:58`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:45`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:38`

### SearchableComboDelegate.setEditorData

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:80`

**Тип:** Метод класса `SearchableComboDelegate`

**Использования:** Нет (возможно, неиспользуемая функция)

### SearchableComboDelegate.setModelData

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:97`

**Тип:** Метод класса `SearchableComboDelegate`

**Использования:** Нет (возможно, неиспользуемая функция)

### SearchableComboDelegate.updateEditorGeometry

**Определено в:** `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:109`

**Тип:** Метод класса `SearchableComboDelegate`

**Использования:** Нет (возможно, неиспользуемая функция)

### SettingsDialog.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:11`

**Тип:** Метод класса `SettingsDialog`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### SettingsDialog._build_ui

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:19`

**Тип:** Метод класса `SettingsDialog`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:28`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:17`

### SettingsDialog._save_and_accept

**Определено в:** `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:55`

**Тип:** Метод класса `SettingsDialog`

**Использования:** Нет (возможно, неиспользуемая функция)

### SplitModel.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:65`

**Тип:** Метод класса `SplitModel`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### SplitModel._add_phantom_rows

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:103`

**Тип:** Метод класса `SplitModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/item_models/split_model.py:100`

### SplitModel._currency_code

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:163`

**Тип:** Метод класса `SplitModel`

**Использования (4 мест):**

- `/home/user/ChaosCash/app/ui/item_models/split_model.py:199`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:212`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:231`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:502`

### SplitModel._edit_amt

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:177`

**Тип:** Метод класса `SplitModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/item_models/split_model.py:243`

### SplitModel._enum_value

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:129`

**Тип:** Метод класса `SplitModel`

**Использования (4 мест):**

- `/home/user/ChaosCash/app/ui/item_models/split_model.py:303`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:426`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:434`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:479`

### SplitModel._format_amt

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:169`

**Тип:** Метод класса `SplitModel`

**Использования (4 мест):**

- `/home/user/ChaosCash/app/ui/item_models/split_model.py:197`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:229`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:191`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:195`

### SplitModel._to_checkstate

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:133`

**Тип:** Метод класса `SplitModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/item_models/split_model.py:321`

### SplitModel.columnCount

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:125`

**Тип:** Метод класса `SplitModel`

**Использования (13 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:247`
- `/home/user/ChaosCash/app/ui/main_window.py:283`
- `/home/user/ChaosCash/app/ui/main_window.py:402`
- `/home/user/ChaosCash/app/ui/main_window.py:410`
- `/home/user/ChaosCash/app/ui/main_window.py:418`
- `/home/user/ChaosCash/app/ui/main_window.py:432`
- `/home/user/ChaosCash/app/ui/main_window.py:468`
- `/home/user/ChaosCash/app/ui/main_window.py:640`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:76`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:47`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:18`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:39`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:56`

### SplitModel.data

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:187`

**Тип:** Метод класса `SplitModel`

**Использования (21 мест):**

- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:39`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:65`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:35`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:63`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:72`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:81`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:87`
- `/home/user/ChaosCash/app/ui/main_window.py:659`
- `/home/user/ChaosCash/app/ui/main_window.py:660`
- `/home/user/ChaosCash/app/ui/main_window.py:685`
- `/home/user/ChaosCash/app/ui/main_window.py:699`
- `/home/user/ChaosCash/app/ui/main_window.py:700`
- `/home/user/ChaosCash/app/ui/main_window.py:701`
- `/home/user/ChaosCash/app/ui/main_window.py:732`
- `/home/user/ChaosCash/app/ui/main_window.py:748`
- `/home/user/ChaosCash/app/ui/main_window.py:749`
- `/home/user/ChaosCash/app/ui/main_window.py:750`
- `/home/user/ChaosCash/app/ui/main_window.py:751`
- `/home/user/ChaosCash/app/ui/main_window.py:752`
- `/home/user/ChaosCash/app/ui/main_window.py:754`

### SplitModel.flags

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:439`

**Тип:** Метод класса `SplitModel`

**Использования (7 мест):**

- `/home/user/ChaosCash/app/ui/item_models/split_model.py:310`
- `/home/user/ChaosCash/app/ui/main_window.py:383`
- `/home/user/ChaosCash/app/ui/main_window.py:507`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:85`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:49`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:98`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:28`

### SplitModel.get_phantom_info

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:473`

**Тип:** Метод класса `SplitModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:686`

### SplitModel.get_row_type

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:468`

**Тип:** Метод класса `SplitModel`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:376`
- `/home/user/ChaosCash/app/ui/main_window.py:680`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:101`

### SplitModel.get_split

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:463`

**Тип:** Метод класса `SplitModel`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:681`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:105`

### SplitModel.headerData

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:145`

**Тип:** Метод класса `SplitModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:40`

### SplitModel.key

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:484`

**Тип:** Метод класса `SplitModel`

**Использования (11 мест):**

- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:46`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:40`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:53`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:61`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:54`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:56`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:64`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:68`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:51`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:55`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:59`

### SplitModel.load

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:87`

**Тип:** Метод класса `SplitModel`

**Использования (11 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:357`
- `/home/user/ChaosCash/app/ui/main_window.py:359`
- `/home/user/ChaosCash/app/ui/main_window.py:526`
- `/home/user/ChaosCash/app/ui/main_window.py:527`
- `/home/user/ChaosCash/app/ui/main_window.py:540`
- `/home/user/ChaosCash/app/ui/main_window.py:547`
- `/home/user/ChaosCash/app/ui/main_window.py:553`
- `/home/user/ChaosCash/app/ui/main_window.py:581`
- `/home/user/ChaosCash/app/ui/main_window.py:599`
- `/home/user/ChaosCash/app/ui/main_window.py:883`
- `/home/user/ChaosCash/app/ui/main_window.py:885`

### SplitModel.rowCount

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:122`

**Тип:** Метод класса `SplitModel`

**Использования (11 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:100`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:65`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:162`
- `/home/user/ChaosCash/app/ui/main_window.py:375`
- `/home/user/ChaosCash/app/ui/main_window.py:503`
- `/home/user/ChaosCash/app/ui/main_window.py:614`
- `/home/user/ChaosCash/app/ui/main_window.py:638`
- `/home/user/ChaosCash/app/ui/main_window.py:639`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:75`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:73`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:17`

### SplitModel.setData

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:293`

**Тип:** Метод класса `SplitModel`

**Использования (8 мест):**

- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:69`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:70`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:79`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:80`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:65`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:106`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:107`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:318`

### SplitModel.set_filter

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:510`

**Тип:** Метод класса `SplitModel`

**Использования:** Нет (возможно, неиспользуемая функция)

### SplitModel.set_zero_split_ids

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:112`

**Тип:** Метод класса `SplitModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:555`

### SplitModel.sort

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/split_model.py:477`

**Тип:** Метод класса `SplitModel`

**Использования (5 мест):**

- `/home/user/ChaosCash/app/ui/account_selection.py:38`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:348`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:90`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:506`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:303`

### SplitRepo.__init__

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:20`

**Тип:** Метод класса `SplitRepo`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### SplitRepo.delete

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:62`

**Тип:** Метод класса `SplitRepo`

**Использования (7 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:28`
- `/home/user/ChaosCash/app/services/transaction_service.py:46`
- `/home/user/ChaosCash/app/services/transaction_service.py:56`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:95`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:247`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:250`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:261`

### SplitRepo.delete_by_account

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:66`

**Тип:** Метод класса `SplitRepo`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:241`

### SplitRepo.get_balance_by_account

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:70`

**Тип:** Метод класса `SplitRepo`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/services/balance_service.py:46`

### SplitRepo.get_by_id

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:23`

**Тип:** Метод класса `SplitRepo`

**Использования (21 мест):**

- `/home/user/ChaosCash/app/repositories/account_repo.py:36`
- `/home/user/ChaosCash/app/repositories/account_repo.py:88`
- `/home/user/ChaosCash/app/repositories/account_repo.py:96`
- `/home/user/ChaosCash/app/services/amount_formatter.py:25`
- `/home/user/ChaosCash/app/services/amount_formatter.py:46`
- `/home/user/ChaosCash/app/services/transaction_service.py:50`
- `/home/user/ChaosCash/app/services/transaction_service.py:83`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:191`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:224`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:236`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:269`
- `/home/user/ChaosCash/app/ui/main_window.py:707`
- `/home/user/ChaosCash/app/ui/main_window.py:726`
- `/home/user/ChaosCash/app/ui/main_window.py:767`
- `/home/user/ChaosCash/tests/test_transaction_service.py:102`
- `/home/user/ChaosCash/tests/test_transaction_service.py:106`
- `/home/user/ChaosCash/tests/test_transaction_service.py:144`
- `/home/user/ChaosCash/tests/test_transaction_service.py:145`
- `/home/user/ChaosCash/tests/test_transaction_service.py:42`
- `/home/user/ChaosCash/tests/test_transaction_service.py:84`
- `/home/user/ChaosCash/tests/test_transaction_service.py:98`

### SplitRepo.get_by_transaction

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:27`

**Тип:** Метод класса `SplitRepo`

**Использования (7 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:87`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:98`
- `/home/user/ChaosCash/tests/test_transaction_service.py:125`
- `/home/user/ChaosCash/tests/test_transaction_service.py:54`
- `/home/user/ChaosCash/tests/test_transaction_service.py:69`
- `/home/user/ChaosCash/tests/test_transaction_service.py:70`
- `/home/user/ChaosCash/tests/test_transaction_service.py:87`

### SplitRepo.get_by_transaction_and_currency

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:31`

**Тип:** Метод класса `SplitRepo`

**Использования (5 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:115`
- `/home/user/ChaosCash/app/services/transaction_service.py:58`
- `/home/user/ChaosCash/app/ui/main_window.py:737`
- `/home/user/ChaosCash/app/ui/main_window.py:796`
- `/home/user/ChaosCash/tests/test_transaction_service.py:177`

### SplitRepo.get_last_currency_for_account

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:75`

**Тип:** Метод класса `SplitRepo`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:336`

### SplitRepo.get_splits_with_zero_amount

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:79`

**Тип:** Метод класса `SplitRepo`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/services/integrity_service.py:26`

### SplitRepo.has_splits_for_account

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:83`

**Тип:** Метод класса `SplitRepo`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:177`

### SplitRepo.insert

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:35`

**Тип:** Метод класса `SplitRepo`

**Использования (73 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:22`
- `/home/user/ChaosCash/app/services/transaction_service.py:33`
- `/home/user/ChaosCash/app/services/transaction_service.py:88`
- `/home/user/ChaosCash/app/services/transaction_service.py:90`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:114`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:190`
- `/home/user/ChaosCash/app/utils/recent_files.py:22`
- `/home/user/ChaosCash/main.py:8`
- `/home/user/ChaosCash/tests/test_balance_service.py:42`
- `/home/user/ChaosCash/tests/test_balance_service.py:48`
- `/home/user/ChaosCash/tests/test_balance_service.py:49`
- `/home/user/ChaosCash/tests/test_balance_service.py:50`
- `/home/user/ChaosCash/tests/test_balance_service.py:51`
- `/home/user/ChaosCash/tests/test_balance_service.py:58`
- `/home/user/ChaosCash/tests/test_balance_service.py:59`
- `/home/user/ChaosCash/tests/test_balance_service.py:6`
- `/home/user/ChaosCash/tests/test_balance_service.py:60`
- `/home/user/ChaosCash/tests/test_balance_service.py:61`
- `/home/user/ChaosCash/tests/test_balance_service.py:62`
- `/home/user/ChaosCash/tests/test_balance_service.py:63`
- `/home/user/ChaosCash/tests/test_balance_service.py:71`
- `/home/user/ChaosCash/tests/test_balance_service.py:72`
- `/home/user/ChaosCash/tests/test_balance_service.py:73`
- `/home/user/ChaosCash/tests/test_balance_service.py:74`
- `/home/user/ChaosCash/tests/test_balance_service.py:76`
- `/home/user/ChaosCash/tests/test_balance_service.py:77`
- `/home/user/ChaosCash/tests/test_balance_service.py:78`
- `/home/user/ChaosCash/tests/test_balance_service.py:85`
- `/home/user/ChaosCash/tests/test_balance_service.py:86`
- `/home/user/ChaosCash/tests/test_balance_service.py:87`
- `/home/user/ChaosCash/tests/test_balance_service.py:88`
- `/home/user/ChaosCash/tests/test_expression_parser.py:5`
- `/home/user/ChaosCash/tests/test_integrity_service.py:46`
- `/home/user/ChaosCash/tests/test_integrity_service.py:47`
- `/home/user/ChaosCash/tests/test_integrity_service.py:48`
- `/home/user/ChaosCash/tests/test_integrity_service.py:49`
- `/home/user/ChaosCash/tests/test_integrity_service.py:54`
- `/home/user/ChaosCash/tests/test_integrity_service.py:55`
- `/home/user/ChaosCash/tests/test_integrity_service.py:56`
- `/home/user/ChaosCash/tests/test_integrity_service.py:57`
- `/home/user/ChaosCash/tests/test_integrity_service.py:58`
- `/home/user/ChaosCash/tests/test_integrity_service.py:59`
- `/home/user/ChaosCash/tests/test_integrity_service.py:6`
- `/home/user/ChaosCash/tests/test_integrity_service.py:64`
- `/home/user/ChaosCash/tests/test_integrity_service.py:73`
- `/home/user/ChaosCash/tests/test_integrity_service.py:74`
- `/home/user/ChaosCash/tests/test_integrity_service.py:75`
- `/home/user/ChaosCash/tests/test_integrity_service.py:76`
- `/home/user/ChaosCash/tests/test_transaction_service.py:111`
- `/home/user/ChaosCash/tests/test_transaction_service.py:112`
- `/home/user/ChaosCash/tests/test_transaction_service.py:113`
- `/home/user/ChaosCash/tests/test_transaction_service.py:114`
- `/home/user/ChaosCash/tests/test_transaction_service.py:133`
- `/home/user/ChaosCash/tests/test_transaction_service.py:134`
- `/home/user/ChaosCash/tests/test_transaction_service.py:135`
- `/home/user/ChaosCash/tests/test_transaction_service.py:151`
- `/home/user/ChaosCash/tests/test_transaction_service.py:152`
- `/home/user/ChaosCash/tests/test_transaction_service.py:153`
- `/home/user/ChaosCash/tests/test_transaction_service.py:164`
- `/home/user/ChaosCash/tests/test_transaction_service.py:165`
- `/home/user/ChaosCash/tests/test_transaction_service.py:166`
- `/home/user/ChaosCash/tests/test_transaction_service.py:167`
- `/home/user/ChaosCash/tests/test_transaction_service.py:48`
- `/home/user/ChaosCash/tests/test_transaction_service.py:49`
- `/home/user/ChaosCash/tests/test_transaction_service.py:59`
- `/home/user/ChaosCash/tests/test_transaction_service.py:6`
- `/home/user/ChaosCash/tests/test_transaction_service.py:60`
- `/home/user/ChaosCash/tests/test_transaction_service.py:61`
- `/home/user/ChaosCash/tests/test_transaction_service.py:76`
- `/home/user/ChaosCash/tests/test_transaction_service.py:77`
- `/home/user/ChaosCash/tests/test_transaction_service.py:78`
- `/home/user/ChaosCash/tests/test_transaction_service.py:93`
- `/home/user/ChaosCash/tests/test_transaction_service.py:94`

### SplitRepo.update

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:43`

**Тип:** Метод класса `SplitRepo`

**Использования (6 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:25`
- `/home/user/ChaosCash/app/services/transaction_service.py:39`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:116`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:268`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:115`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:245`

### SplitRepo.update_account

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:58`

**Тип:** Метод класса `SplitRepo`

**Использования:** Нет (возможно, неиспользуемая функция)

### SplitRepo.update_amount

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:50`

**Тип:** Метод класса `SplitRepo`

**Использования (4 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:126`
- `/home/user/ChaosCash/app/services/transaction_service.py:131`
- `/home/user/ChaosCash/app/services/transaction_service.py:133`
- `/home/user/ChaosCash/tests/test_balance_service.py:95`

### SplitRepo.update_amount_fixed

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:54`

**Тип:** Метод класса `SplitRepo`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:43`

### SplitView.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/split_view.py:24`

**Тип:** Метод класса `SplitView`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### SplitView._delete_split

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/split_view.py:115`

**Тип:** Метод класса `SplitView`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/split_view.py:111`

### SplitView._first_editable_in_row

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/split_view.py:43`

**Тип:** Метод класса `SplitView`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/split_view.py:74`

### SplitView._show_context_menu

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/split_view.py:95`

**Тип:** Метод класса `SplitView`

**Использования:** Нет (возможно, неиспользуемая функция)

### SplitView._show_header_menu

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/split_view.py:120`

**Тип:** Метод класса `SplitView`

**Использования:** Нет (возможно, неиспользуемая функция)

### SplitView._toggle_column

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/split_view.py:123`

**Тип:** Метод класса `SplitView`

**Использования:** Нет (возможно, неиспользуемая функция)

### SplitView.keyPressEvent

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/split_view.py:53`

**Тип:** Метод класса `SplitView`

**Использования (7 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:59`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:65`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:57`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:62`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:80`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:53`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:63`

### SplitView.mousePressEvent

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/split_view.py:91`

**Тип:** Метод класса `SplitView`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/split_view.py:93`

### SplitView.moveCursor

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/split_view.py:82`

**Тип:** Метод класса `SplitView`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:87`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:89`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:72`

### StartupDialog.__init__

**Определено в:** `/home/user/ChaosCash/main.py:90`

**Тип:** Метод класса `StartupDialog`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### StartupDialog._new

**Определено в:** `/home/user/ChaosCash/main.py:117`

**Тип:** Метод класса `StartupDialog`

**Использования:** Нет (возможно, неиспользуемая функция)

### StartupDialog._open

**Определено в:** `/home/user/ChaosCash/main.py:108`

**Тип:** Метод класса `StartupDialog`

**Использования:** Нет (возможно, неиспользуемая функция)

### TransactionModel.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:36`

**Тип:** Метод класса `TransactionModel`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### TransactionModel._format_amt

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:149`

**Тип:** Метод класса `TransactionModel`

**Использования (4 мест):**

- `/home/user/ChaosCash/app/ui/item_models/split_model.py:197`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:229`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:191`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:195`

### TransactionModel._format_date

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:138`

**Тип:** Метод класса `TransactionModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:185`

### TransactionModel._is_phantom_row

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:126`

**Тип:** Метод класса `TransactionModel`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:167`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:219`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:230`

### TransactionModel._phantom_date

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:129`

**Тип:** Метод класса `TransactionModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:170`

### TransactionModel.canFetchMore

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:99`

**Тип:** Метод класса `TransactionModel`

**Использования:** Нет (возможно, неиспользуемая функция)

### TransactionModel.columnCount

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:116`

**Тип:** Метод класса `TransactionModel`

**Использования (13 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:247`
- `/home/user/ChaosCash/app/ui/main_window.py:283`
- `/home/user/ChaosCash/app/ui/main_window.py:402`
- `/home/user/ChaosCash/app/ui/main_window.py:410`
- `/home/user/ChaosCash/app/ui/main_window.py:418`
- `/home/user/ChaosCash/app/ui/main_window.py:432`
- `/home/user/ChaosCash/app/ui/main_window.py:468`
- `/home/user/ChaosCash/app/ui/main_window.py:640`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:76`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:47`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:18`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:39`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:56`

### TransactionModel.data

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:161`

**Тип:** Метод класса `TransactionModel`

**Использования (21 мест):**

- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:39`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:65`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:35`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:63`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:72`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:81`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:87`
- `/home/user/ChaosCash/app/ui/main_window.py:659`
- `/home/user/ChaosCash/app/ui/main_window.py:660`
- `/home/user/ChaosCash/app/ui/main_window.py:685`
- `/home/user/ChaosCash/app/ui/main_window.py:699`
- `/home/user/ChaosCash/app/ui/main_window.py:700`
- `/home/user/ChaosCash/app/ui/main_window.py:701`
- `/home/user/ChaosCash/app/ui/main_window.py:732`
- `/home/user/ChaosCash/app/ui/main_window.py:748`
- `/home/user/ChaosCash/app/ui/main_window.py:749`
- `/home/user/ChaosCash/app/ui/main_window.py:750`
- `/home/user/ChaosCash/app/ui/main_window.py:751`
- `/home/user/ChaosCash/app/ui/main_window.py:752`
- `/home/user/ChaosCash/app/ui/main_window.py:754`

### TransactionModel.fetchMore

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:102`

**Тип:** Метод класса `TransactionModel`

**Использования:** Нет (возможно, неиспользуемая функция)

### TransactionModel.find_row_for_trans

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:276`

**Тип:** Метод класса `TransactionModel`

**Использования (4 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:360`
- `/home/user/ChaosCash/app/ui/main_window.py:500`
- `/home/user/ChaosCash/app/ui/main_window.py:594`
- `/home/user/ChaosCash/app/ui/main_window.py:602`

### TransactionModel.flags

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:215`

**Тип:** Метод класса `TransactionModel`

**Использования (7 мест):**

- `/home/user/ChaosCash/app/ui/item_models/split_model.py:310`
- `/home/user/ChaosCash/app/ui/main_window.py:383`
- `/home/user/ChaosCash/app/ui/main_window.py:507`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:85`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:49`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:98`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:28`

### TransactionModel.get_trans_id

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:271`

**Тип:** Метод класса `TransactionModel`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:656`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:117`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:128`

### TransactionModel.headerData

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:119`

**Тип:** Метод класса `TransactionModel`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:40`

### TransactionModel.key

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:287`

**Тип:** Метод класса `TransactionModel`

**Использования (11 мест):**

- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:46`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:40`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:53`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:61`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:54`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:56`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:64`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:68`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:51`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:55`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:59`

### TransactionModel.load

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:48`

**Тип:** Метод класса `TransactionModel`

**Использования (11 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:357`
- `/home/user/ChaosCash/app/ui/main_window.py:359`
- `/home/user/ChaosCash/app/ui/main_window.py:526`
- `/home/user/ChaosCash/app/ui/main_window.py:527`
- `/home/user/ChaosCash/app/ui/main_window.py:540`
- `/home/user/ChaosCash/app/ui/main_window.py:547`
- `/home/user/ChaosCash/app/ui/main_window.py:553`
- `/home/user/ChaosCash/app/ui/main_window.py:581`
- `/home/user/ChaosCash/app/ui/main_window.py:599`
- `/home/user/ChaosCash/app/ui/main_window.py:883`
- `/home/user/ChaosCash/app/ui/main_window.py:885`

### TransactionModel.load_by_ids

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:74`

**Тип:** Метод класса `TransactionModel`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:539`
- `/home/user/ChaosCash/app/ui/main_window.py:592`

### TransactionModel.rowCount

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:110`

**Тип:** Метод класса `TransactionModel`

**Использования (11 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:100`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:65`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:162`
- `/home/user/ChaosCash/app/ui/main_window.py:375`
- `/home/user/ChaosCash/app/ui/main_window.py:503`
- `/home/user/ChaosCash/app/ui/main_window.py:614`
- `/home/user/ChaosCash/app/ui/main_window.py:638`
- `/home/user/ChaosCash/app/ui/main_window.py:639`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:75`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:73`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:17`

### TransactionModel.setData

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:227`

**Тип:** Метод класса `TransactionModel`

**Использования (8 мест):**

- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:69`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:70`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:79`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:80`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:65`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:106`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:107`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:318`

### TransactionModel.set_filter

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:308`

**Тип:** Метод класса `TransactionModel`

**Использования:** Нет (возможно, неиспользуемая функция)

### TransactionModel.sort

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:283`

**Тип:** Метод класса `TransactionModel`

**Использования (5 мест):**

- `/home/user/ChaosCash/app/ui/account_selection.py:38`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:348`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:90`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:506`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:303`

### TransactionRepo.__init__

**Определено в:** `/home/user/ChaosCash/app/repositories/transaction_repo.py:15`

**Тип:** Метод класса `TransactionRepo`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### TransactionRepo._fetch_dicts_with_ids

**Определено в:** `/home/user/ChaosCash/app/repositories/transaction_repo.py:18`

**Тип:** Метод класса `TransactionRepo`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/repositories/transaction_repo.py:44`
- `/home/user/ChaosCash/app/repositories/transaction_repo.py:47`
- `/home/user/ChaosCash/app/repositories/transaction_repo.py:50`

### TransactionRepo.delete

**Определено в:** `/home/user/ChaosCash/app/repositories/transaction_repo.py:39`

**Тип:** Метод класса `TransactionRepo`

**Использования (7 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:28`
- `/home/user/ChaosCash/app/services/transaction_service.py:46`
- `/home/user/ChaosCash/app/services/transaction_service.py:56`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:95`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:247`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:250`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:261`

### TransactionRepo.get_by_id

**Определено в:** `/home/user/ChaosCash/app/repositories/transaction_repo.py:26`

**Тип:** Метод класса `TransactionRepo`

**Использования (21 мест):**

- `/home/user/ChaosCash/app/repositories/account_repo.py:36`
- `/home/user/ChaosCash/app/repositories/account_repo.py:88`
- `/home/user/ChaosCash/app/repositories/account_repo.py:96`
- `/home/user/ChaosCash/app/services/amount_formatter.py:25`
- `/home/user/ChaosCash/app/services/amount_formatter.py:46`
- `/home/user/ChaosCash/app/services/transaction_service.py:50`
- `/home/user/ChaosCash/app/services/transaction_service.py:83`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:191`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:224`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:236`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:269`
- `/home/user/ChaosCash/app/ui/main_window.py:707`
- `/home/user/ChaosCash/app/ui/main_window.py:726`
- `/home/user/ChaosCash/app/ui/main_window.py:767`
- `/home/user/ChaosCash/tests/test_transaction_service.py:102`
- `/home/user/ChaosCash/tests/test_transaction_service.py:106`
- `/home/user/ChaosCash/tests/test_transaction_service.py:144`
- `/home/user/ChaosCash/tests/test_transaction_service.py:145`
- `/home/user/ChaosCash/tests/test_transaction_service.py:42`
- `/home/user/ChaosCash/tests/test_transaction_service.py:84`
- `/home/user/ChaosCash/tests/test_transaction_service.py:98`

### TransactionRepo.get_empty

**Определено в:** `/home/user/ChaosCash/app/repositories/transaction_repo.py:56`

**Тип:** Метод класса `TransactionRepo`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/services/integrity_service.py:22`

### TransactionRepo.get_imbalanced

**Определено в:** `/home/user/ChaosCash/app/repositories/transaction_repo.py:52`

**Тип:** Метод класса `TransactionRepo`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/services/integrity_service.py:17`

### TransactionRepo.get_summary_by_accounts

**Определено в:** `/home/user/ChaosCash/app/repositories/transaction_repo.py:46`

**Тип:** Метод класса `TransactionRepo`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:68`

### TransactionRepo.get_summary_by_ids

**Определено в:** `/home/user/ChaosCash/app/repositories/transaction_repo.py:49`

**Тип:** Метод класса `TransactionRepo`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:93`

### TransactionRepo.get_verbose_by_accounts

**Определено в:** `/home/user/ChaosCash/app/repositories/transaction_repo.py:43`

**Тип:** Метод класса `TransactionRepo`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:66`

### TransactionRepo.insert

**Определено в:** `/home/user/ChaosCash/app/repositories/transaction_repo.py:30`

**Тип:** Метод класса `TransactionRepo`

**Использования (73 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:22`
- `/home/user/ChaosCash/app/services/transaction_service.py:33`
- `/home/user/ChaosCash/app/services/transaction_service.py:88`
- `/home/user/ChaosCash/app/services/transaction_service.py:90`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:114`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:190`
- `/home/user/ChaosCash/app/utils/recent_files.py:22`
- `/home/user/ChaosCash/main.py:8`
- `/home/user/ChaosCash/tests/test_balance_service.py:42`
- `/home/user/ChaosCash/tests/test_balance_service.py:48`
- `/home/user/ChaosCash/tests/test_balance_service.py:49`
- `/home/user/ChaosCash/tests/test_balance_service.py:50`
- `/home/user/ChaosCash/tests/test_balance_service.py:51`
- `/home/user/ChaosCash/tests/test_balance_service.py:58`
- `/home/user/ChaosCash/tests/test_balance_service.py:59`
- `/home/user/ChaosCash/tests/test_balance_service.py:6`
- `/home/user/ChaosCash/tests/test_balance_service.py:60`
- `/home/user/ChaosCash/tests/test_balance_service.py:61`
- `/home/user/ChaosCash/tests/test_balance_service.py:62`
- `/home/user/ChaosCash/tests/test_balance_service.py:63`
- `/home/user/ChaosCash/tests/test_balance_service.py:71`
- `/home/user/ChaosCash/tests/test_balance_service.py:72`
- `/home/user/ChaosCash/tests/test_balance_service.py:73`
- `/home/user/ChaosCash/tests/test_balance_service.py:74`
- `/home/user/ChaosCash/tests/test_balance_service.py:76`
- `/home/user/ChaosCash/tests/test_balance_service.py:77`
- `/home/user/ChaosCash/tests/test_balance_service.py:78`
- `/home/user/ChaosCash/tests/test_balance_service.py:85`
- `/home/user/ChaosCash/tests/test_balance_service.py:86`
- `/home/user/ChaosCash/tests/test_balance_service.py:87`
- `/home/user/ChaosCash/tests/test_balance_service.py:88`
- `/home/user/ChaosCash/tests/test_expression_parser.py:5`
- `/home/user/ChaosCash/tests/test_integrity_service.py:46`
- `/home/user/ChaosCash/tests/test_integrity_service.py:47`
- `/home/user/ChaosCash/tests/test_integrity_service.py:48`
- `/home/user/ChaosCash/tests/test_integrity_service.py:49`
- `/home/user/ChaosCash/tests/test_integrity_service.py:54`
- `/home/user/ChaosCash/tests/test_integrity_service.py:55`
- `/home/user/ChaosCash/tests/test_integrity_service.py:56`
- `/home/user/ChaosCash/tests/test_integrity_service.py:57`
- `/home/user/ChaosCash/tests/test_integrity_service.py:58`
- `/home/user/ChaosCash/tests/test_integrity_service.py:59`
- `/home/user/ChaosCash/tests/test_integrity_service.py:6`
- `/home/user/ChaosCash/tests/test_integrity_service.py:64`
- `/home/user/ChaosCash/tests/test_integrity_service.py:73`
- `/home/user/ChaosCash/tests/test_integrity_service.py:74`
- `/home/user/ChaosCash/tests/test_integrity_service.py:75`
- `/home/user/ChaosCash/tests/test_integrity_service.py:76`
- `/home/user/ChaosCash/tests/test_transaction_service.py:111`
- `/home/user/ChaosCash/tests/test_transaction_service.py:112`
- `/home/user/ChaosCash/tests/test_transaction_service.py:113`
- `/home/user/ChaosCash/tests/test_transaction_service.py:114`
- `/home/user/ChaosCash/tests/test_transaction_service.py:133`
- `/home/user/ChaosCash/tests/test_transaction_service.py:134`
- `/home/user/ChaosCash/tests/test_transaction_service.py:135`
- `/home/user/ChaosCash/tests/test_transaction_service.py:151`
- `/home/user/ChaosCash/tests/test_transaction_service.py:152`
- `/home/user/ChaosCash/tests/test_transaction_service.py:153`
- `/home/user/ChaosCash/tests/test_transaction_service.py:164`
- `/home/user/ChaosCash/tests/test_transaction_service.py:165`
- `/home/user/ChaosCash/tests/test_transaction_service.py:166`
- `/home/user/ChaosCash/tests/test_transaction_service.py:167`
- `/home/user/ChaosCash/tests/test_transaction_service.py:48`
- `/home/user/ChaosCash/tests/test_transaction_service.py:49`
- `/home/user/ChaosCash/tests/test_transaction_service.py:59`
- `/home/user/ChaosCash/tests/test_transaction_service.py:6`
- `/home/user/ChaosCash/tests/test_transaction_service.py:60`
- `/home/user/ChaosCash/tests/test_transaction_service.py:61`
- `/home/user/ChaosCash/tests/test_transaction_service.py:76`
- `/home/user/ChaosCash/tests/test_transaction_service.py:77`
- `/home/user/ChaosCash/tests/test_transaction_service.py:78`
- `/home/user/ChaosCash/tests/test_transaction_service.py:93`
- `/home/user/ChaosCash/tests/test_transaction_service.py:94`

### TransactionRepo.update

**Определено в:** `/home/user/ChaosCash/app/repositories/transaction_repo.py:35`

**Тип:** Метод класса `TransactionRepo`

**Использования (6 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:25`
- `/home/user/ChaosCash/app/services/transaction_service.py:39`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:116`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:268`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:115`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:245`

### TransactionService.__init__

**Определено в:** `/home/user/ChaosCash/app/services/transaction_service.py:14`

**Тип:** Метод класса `TransactionService`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### TransactionService._copy_transaction

**Определено в:** `/home/user/ChaosCash/app/services/transaction_service.py:80`

**Тип:** Метод класса `TransactionService`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:64`
- `/home/user/ChaosCash/app/services/transaction_service.py:72`

### TransactionService.add_split

**Определено в:** `/home/user/ChaosCash/app/services/transaction_service.py:30`

**Тип:** Метод класса `TransactionService`

**Использования (19 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:348`
- `/home/user/ChaosCash/app/ui/main_window.py:688`
- `/home/user/ChaosCash/app/ui/main_window.py:711`
- `/home/user/ChaosCash/tests/test_transaction_service.py:117`
- `/home/user/ChaosCash/tests/test_transaction_service.py:118`
- `/home/user/ChaosCash/tests/test_transaction_service.py:119`
- `/home/user/ChaosCash/tests/test_transaction_service.py:138`
- `/home/user/ChaosCash/tests/test_transaction_service.py:139`
- `/home/user/ChaosCash/tests/test_transaction_service.py:156`
- `/home/user/ChaosCash/tests/test_transaction_service.py:157`
- `/home/user/ChaosCash/tests/test_transaction_service.py:170`
- `/home/user/ChaosCash/tests/test_transaction_service.py:171`
- `/home/user/ChaosCash/tests/test_transaction_service.py:172`
- `/home/user/ChaosCash/tests/test_transaction_service.py:51`
- `/home/user/ChaosCash/tests/test_transaction_service.py:63`
- `/home/user/ChaosCash/tests/test_transaction_service.py:64`
- `/home/user/ChaosCash/tests/test_transaction_service.py:80`
- `/home/user/ChaosCash/tests/test_transaction_service.py:81`
- `/home/user/ChaosCash/tests/test_transaction_service.py:96`

### TransactionService.create_transaction

**Определено в:** `/home/user/ChaosCash/app/services/transaction_service.py:18`

**Тип:** Метод класса `TransactionService`

**Использования (10 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:344`
- `/home/user/ChaosCash/tests/test_transaction_service.py:116`
- `/home/user/ChaosCash/tests/test_transaction_service.py:137`
- `/home/user/ChaosCash/tests/test_transaction_service.py:155`
- `/home/user/ChaosCash/tests/test_transaction_service.py:169`
- `/home/user/ChaosCash/tests/test_transaction_service.py:41`
- `/home/user/ChaosCash/tests/test_transaction_service.py:50`
- `/home/user/ChaosCash/tests/test_transaction_service.py:62`
- `/home/user/ChaosCash/tests/test_transaction_service.py:79`
- `/home/user/ChaosCash/tests/test_transaction_service.py:95`

### TransactionService.delete_split

**Определено в:** `/home/user/ChaosCash/app/services/transaction_service.py:45`

**Тип:** Метод класса `TransactionService`

**Использования:** Нет (возможно, неиспользуемая функция)

### TransactionService.delete_split_and_rebalance

**Определено в:** `/home/user/ChaosCash/app/services/transaction_service.py:48`

**Тип:** Метод класса `TransactionService`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/widgets/split_view.py:116`
- `/home/user/ChaosCash/tests/test_transaction_service.py:174`

### TransactionService.delete_transaction

**Определено в:** `/home/user/ChaosCash/app/services/transaction_service.py:27`

**Тип:** Метод класса `TransactionService`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:166`
- `/home/user/ChaosCash/tests/test_transaction_service.py:52`

### TransactionService.duplicate_transaction

**Определено в:** `/home/user/ChaosCash/app/services/transaction_service.py:62`

**Тип:** Метод класса `TransactionService`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:151`
- `/home/user/ChaosCash/tests/test_transaction_service.py:66`

### TransactionService.recalculate_flexible_splits

**Определено в:** `/home/user/ChaosCash/app/services/transaction_service.py:101`

**Тип:** Метод класса `TransactionService`

**Использования (8 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:60`
- `/home/user/ChaosCash/app/ui/main_window.py:715`
- `/home/user/ChaosCash/app/ui/main_window.py:741`
- `/home/user/ChaosCash/app/ui/main_window.py:781`
- `/home/user/ChaosCash/app/ui/main_window.py:800`
- `/home/user/ChaosCash/tests/test_transaction_service.py:122`
- `/home/user/ChaosCash/tests/test_transaction_service.py:141`
- `/home/user/ChaosCash/tests/test_transaction_service.py:159`

### TransactionService.reverse_transaction

**Определено в:** `/home/user/ChaosCash/app/services/transaction_service.py:70`

**Тип:** Метод класса `TransactionService`

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:155`
- `/home/user/ChaosCash/tests/test_transaction_service.py:83`

### TransactionService.update_split

**Определено в:** `/home/user/ChaosCash/app/services/transaction_service.py:36`

**Тип:** Метод класса `TransactionService`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:774`

### TransactionService.update_split_fixed

**Определено в:** `/home/user/ChaosCash/app/services/transaction_service.py:42`

**Тип:** Метод класса `TransactionService`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:735`
- `/home/user/ChaosCash/tests/test_transaction_service.py:101`
- `/home/user/ChaosCash/tests/test_transaction_service.py:105`

### TransactionService.update_transaction

**Определено в:** `/home/user/ChaosCash/app/services/transaction_service.py:24`

**Тип:** Метод класса `TransactionService`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:662`

### TransactionView.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:25`

**Тип:** Метод класса `TransactionView`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### TransactionView._delete

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:158`

**Тип:** Метод класса `TransactionView`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:145`

### TransactionView._duplicate

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:150`

**Тип:** Метод класса `TransactionView`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:135`

### TransactionView._on_clicked

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:114`

**Тип:** Метод класса `TransactionView`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:112`

### TransactionView._on_current_row_changed

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:108`

**Тип:** Метод класса `TransactionView`

**Использования:** Нет (возможно, неиспользуемая функция)

### TransactionView._reverse

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:154`

**Тип:** Метод класса `TransactionView`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:139`

### TransactionView._show_context_menu

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:123`

**Тип:** Метод класса `TransactionView`

**Использования:** Нет (возможно, неиспользуемая функция)

### TransactionView._show_header_menu

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:169`

**Тип:** Метод класса `TransactionView`

**Использования:** Нет (возможно, неиспользуемая функция)

### TransactionView._toggle_column

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:172`

**Тип:** Метод класса `TransactionView`

**Использования:** Нет (возможно, неиспользуемая функция)

### TransactionView.closeEditor

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:75`

**Тип:** Метод класса `TransactionView`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:106`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:84`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:94`

### TransactionView.keyPressEvent

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:50`

**Тип:** Метод класса `TransactionView`

**Использования (7 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:59`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:65`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:57`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:62`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:80`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:53`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:63`

### TransactionView.moveCursor

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:65`

**Тип:** Метод класса `TransactionView`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:87`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:89`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:72`

### TransactionView.setModel

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:45`

**Тип:** Метод класса `TransactionView`

**Использования (5 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:243`
- `/home/user/ChaosCash/app/ui/main_window.py:261`
- `/home/user/ChaosCash/app/ui/main_window.py:279`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:52`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:46`

### UIEventLogger.__init__

**Определено в:** `/home/user/ChaosCash/app/ui/ui_event_logger.py:18`

**Тип:** Метод класса `UIEventLogger`

**Использования (17 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:12`
- `/home/user/ChaosCash/app/ui/delegates/currency_combo_delegate.py:11`
- `/home/user/ChaosCash/app/ui/delegates/date_delegate.py:14`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:22`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:12`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:46`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:74`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:38`
- `/home/user/ChaosCash/app/ui/main_window.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:19`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:29`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:25`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:26`
- `/home/user/ChaosCash/main.py:91`

### UIEventLogger._describe_event

**Определено в:** `/home/user/ChaosCash/app/ui/ui_event_logger.py:70`

**Тип:** Метод класса `UIEventLogger`

**Использования (4 мест):**

- `/home/user/ChaosCash/app/ui/ui_event_logger.py:31`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:37`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:50`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:61`

### UIEventLogger._describe_key_event

**Определено в:** `/home/user/ChaosCash/app/ui/ui_event_logger.py:47`

**Тип:** Метод класса `UIEventLogger`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/ui_event_logger.py:33`

### UIEventLogger._describe_mouse_event

**Определено в:** `/home/user/ChaosCash/app/ui/ui_event_logger.py:58`

**Тип:** Метод класса `UIEventLogger`

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/ui_event_logger.py:35`

### UIEventLogger._object_name

**Определено в:** `/home/user/ChaosCash/app/ui/ui_event_logger.py:104`

**Тип:** Метод класса `UIEventLogger`

**Использования (5 мест):**

- `/home/user/ChaosCash/app/ui/ui_event_logger.py:43`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:44`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:52`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:64`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:72`

### UIEventLogger._on_focus_changed

**Определено в:** `/home/user/ChaosCash/app/ui/ui_event_logger.py:40`

**Тип:** Метод класса `UIEventLogger`

**Использования:** Нет (возможно, неиспользуемая функция)

### UIEventLogger._view_state

**Определено в:** `/home/user/ChaosCash/app/ui/ui_event_logger.py:76`

**Тип:** Метод класса `UIEventLogger`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/ui_event_logger.py:55`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:67`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:73`

### UIEventLogger.eventFilter

**Определено в:** `/home/user/ChaosCash/app/ui/ui_event_logger.py:28`

**Тип:** Метод класса `UIEventLogger`

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:58`
- `/home/user/ChaosCash/app/ui/delegates/searchable_combo_delegate.py:45`
- `/home/user/ChaosCash/app/ui/ui_event_logger.py:38`

### UIEventLogger.install

**Определено в:** `/home/user/ChaosCash/app/ui/ui_event_logger.py:22`

**Тип:** Метод класса `UIEventLogger`

**Использования (1 мест):**

- `/home/user/ChaosCash/main.py:63`

### _apply_pragmas

**Определено в:** `/home/user/ChaosCash/app/database/connection.py:11`

**Тип:** Функция

**Использования (1 мест):**

- `/home/user/ChaosCash/app/database/connection.py:7`

### _ask_file_path

**Определено в:** `/home/user/ChaosCash/main.py:85`

**Тип:** Функция

**Использования (1 мест):**

- `/home/user/ChaosCash/main.py:74`

### _configure_logging

**Определено в:** `/home/user/ChaosCash/main.py:18`

**Тип:** Функция

**Использования (1 мест):**

- `/home/user/ChaosCash/main.py:52`

### _eval_node

**Определено в:** `/home/user/ChaosCash/app/utils/expression_parser.py:29`

**Тип:** Функция

**Использования (4 мест):**

- `/home/user/ChaosCash/app/utils/expression_parser.py:26`
- `/home/user/ChaosCash/app/utils/expression_parser.py:33`
- `/home/user/ChaosCash/app/utils/expression_parser.py:34`
- `/home/user/ChaosCash/app/utils/expression_parser.py:39`

### _make_virtual_account

**Определено в:** `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:380`

**Тип:** Функция

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:103`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:99`

### _parse_args

**Определено в:** `/home/user/ChaosCash/main.py:39`

**Тип:** Функция

**Использования (1 мест):**

- `/home/user/ChaosCash/main.py:51`

### _row_to_account

**Определено в:** `/home/user/ChaosCash/app/repositories/account_repo.py:6`

**Тип:** Функция

**Использования (3 мест):**

- `/home/user/ChaosCash/app/repositories/account_repo.py:25`
- `/home/user/ChaosCash/app/repositories/account_repo.py:29`
- `/home/user/ChaosCash/app/repositories/account_repo.py:33`

### _row_to_currency

**Определено в:** `/home/user/ChaosCash/app/repositories/currency_repo.py:6`

**Тип:** Функция

**Использования (2 мест):**

- `/home/user/ChaosCash/app/repositories/currency_repo.py:22`
- `/home/user/ChaosCash/app/repositories/currency_repo.py:26`

### _row_to_split

**Определено в:** `/home/user/ChaosCash/app/repositories/split_repo.py:6`

**Тип:** Функция

**Использования (3 мест):**

- `/home/user/ChaosCash/app/repositories/split_repo.py:25`
- `/home/user/ChaosCash/app/repositories/split_repo.py:29`
- `/home/user/ChaosCash/app/repositories/split_repo.py:33`

### _row_to_trans

**Определено в:** `/home/user/ChaosCash/app/repositories/transaction_repo.py:6`

**Тип:** Функция

**Использования (2 мест):**

- `/home/user/ChaosCash/app/repositories/transaction_repo.py:28`
- `/home/user/ChaosCash/app/repositories/transaction_repo.py:58`

### _utc_now

**Определено в:** `/home/user/ChaosCash/app/services/transaction_service.py:9`

**Тип:** Функция

**Использования (2 мест):**

- `/home/user/ChaosCash/app/services/transaction_service.py:21`
- `/home/user/ChaosCash/app/services/transaction_service.py:88`

### add_recent_file

**Определено в:** `/home/user/ChaosCash/app/utils/recent_files.py:18`

**Тип:** Функция

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:91`

### analyze_codebase

**Определено в:** `/home/user/ChaosCash/generate_function_usage_docs.py:124`

**Тип:** Функция

**Использования (1 мест):**

- `/home/user/ChaosCash/generate_function_usage_docs.py:234`

### analyze_file

**Определено в:** `/home/user/ChaosCash/generate_function_usage_docs.py:76`

**Тип:** Функция

**Использования (1 мест):**

- `/home/user/ChaosCash/generate_function_usage_docs.py:146`

### balance_service

**Определено в:** `/home/user/ChaosCash/tests/test_balance_service.py:37`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### compute_hidden_account_ids

**Определено в:** `/home/user/ChaosCash/app/utils/account_hierarchy.py:6`

**Тип:** Функция

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/account_selection.py:18`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:74`

### db

**Определено в:** `/home/user/ChaosCash/tests/test_transaction_service.py:17`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### ensure_schema

**Определено в:** `/home/user/ChaosCash/app/database/schema.py:47`

**Тип:** Функция

**Использования (4 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:56`
- `/home/user/ChaosCash/tests/test_balance_service.py:22`
- `/home/user/ChaosCash/tests/test_integrity_service.py:21`
- `/home/user/ChaosCash/tests/test_transaction_service.py:21`

### find_next_editable_table_cell

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:8`

**Тип:** Функция

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/widgets/split_view.py:85`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:68`

### float_to_quants

**Определено в:** `/home/user/ChaosCash/app/utils/amount_math.py:9`

**Тип:** Функция

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/item_models/split_model.py:379`
- `/home/user/ChaosCash/app/ui/main_window.py:709`
- `/home/user/ChaosCash/app/ui/main_window.py:769`

### generate_markdown_report

**Определено в:** `/home/user/ChaosCash/generate_function_usage_docs.py:191`

**Тип:** Функция

**Использования (1 мест):**

- `/home/user/ChaosCash/generate_function_usage_docs.py:239`

### get_last_file

**Определено в:** `/home/user/ChaosCash/app/utils/recent_files.py:28`

**Тип:** Функция

**Использования (1 мест):**

- `/home/user/ChaosCash/main.py:67`

### get_recent_files

**Определено в:** `/home/user/ChaosCash/app/utils/recent_files.py:10`

**Тип:** Функция

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:836`
- `/home/user/ChaosCash/app/utils/recent_files.py:19`
- `/home/user/ChaosCash/app/utils/recent_files.py:29`

### get_selectable_account_items

**Определено в:** `/home/user/ChaosCash/app/ui/account_selection.py:8`

**Тип:** Функция

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/delegates/account_combo_delegate.py:18`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:199`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:232`

### integrity

**Определено в:** `/home/user/ChaosCash/tests/test_integrity_service.py:37`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### main

**Определено в:** `/home/user/ChaosCash/main.py:50`

**Тип:** Функция

**Использования (4 мест):**

- `/home/user/ChaosCash/generate_function_usage_docs.py:260`
- `/home/user/ChaosCash/main.py:133`

### mark_hidden_descendants

**Определено в:** `/home/user/ChaosCash/app/utils/account_hierarchy.py:15`

**Тип:** Функция

**Использования (3 мест):**

- `/home/user/ChaosCash/app/utils/account_hierarchy.py:18`
- `/home/user/ChaosCash/app/utils/account_hierarchy.py:21`
- `/home/user/ChaosCash/app/utils/account_hierarchy.py:24`

### open_connection

**Определено в:** `/home/user/ChaosCash/app/database/connection.py:3`

**Тип:** Функция

**Использования (1 мест):**

- `/home/user/ChaosCash/app/ui/main_window.py:55`

### qt_format_to_strftime

**Определено в:** `/home/user/ChaosCash/app/utils/date_utils.py:4`

**Тип:** Функция

**Использования (2 мест):**

- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:132`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:144`

### quants_to_float

**Определено в:** `/home/user/ChaosCash/app/utils/amount_math.py:4`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### repos

**Определено в:** `/home/user/ChaosCash/tests/test_transaction_service.py:26`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### safe_eval

**Определено в:** `/home/user/ChaosCash/app/utils/expression_parser.py:14`

**Тип:** Функция

**Использования (18 мест):**

- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:50`
- `/home/user/ChaosCash/app/ui/delegates/amount_delegate.py:73`
- `/home/user/ChaosCash/app/ui/main_window.py:704`
- `/home/user/ChaosCash/app/ui/main_window.py:763`
- `/home/user/ChaosCash/tests/test_expression_parser.py:11`
- `/home/user/ChaosCash/tests/test_expression_parser.py:15`
- `/home/user/ChaosCash/tests/test_expression_parser.py:19`
- `/home/user/ChaosCash/tests/test_expression_parser.py:23`
- `/home/user/ChaosCash/tests/test_expression_parser.py:27`
- `/home/user/ChaosCash/tests/test_expression_parser.py:31`
- `/home/user/ChaosCash/tests/test_expression_parser.py:35`
- `/home/user/ChaosCash/tests/test_expression_parser.py:39`
- `/home/user/ChaosCash/tests/test_expression_parser.py:43`
- `/home/user/ChaosCash/tests/test_expression_parser.py:47`
- `/home/user/ChaosCash/tests/test_expression_parser.py:52`
- `/home/user/ChaosCash/tests/test_expression_parser.py:57`
- `/home/user/ChaosCash/tests/test_expression_parser.py:61`
- `/home/user/ChaosCash/tests/test_expression_parser.py:65`

### search_usages_in_file

**Определено в:** `/home/user/ChaosCash/generate_function_usage_docs.py:95`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### service

**Определено в:** `/home/user/ChaosCash/tests/test_transaction_service.py:36`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### set_column_visibility

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:50`

**Тип:** Функция

**Использования (4 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:328`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:124`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:173`
- `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:44`

### show_column_visibility_menu

**Определено в:** `/home/user/ChaosCash/app/ui/widgets/view_helpers.py:32`

**Тип:** Функция

**Использования (3 мест):**

- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:160`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:121`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:170`

### test_addition

**Определено в:** `/home/user/ChaosCash/tests/test_expression_parser.py:18`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_balanced_no_imbalance

**Определено в:** `/home/user/ChaosCash/tests/test_integrity_service.py:53`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_cache_invalidation

**Определено в:** `/home/user/ChaosCash/tests/test_balance_service.py:84`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_comma_as_decimal

**Определено в:** `/home/user/ChaosCash/tests/test_expression_parser.py:46`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_complex_expression

**Определено в:** `/home/user/ChaosCash/tests/test_expression_parser.py:42`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_create_transaction

**Определено в:** `/home/user/ChaosCash/tests/test_transaction_service.py:40`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_delete_split_and_rebalance

**Определено в:** `/home/user/ChaosCash/tests/test_transaction_service.py:163`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_delete_transaction_cascades

**Определено в:** `/home/user/ChaosCash/tests/test_transaction_service.py:47`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_detects_empty_transactions

**Определено в:** `/home/user/ChaosCash/tests/test_integrity_service.py:63`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_detects_imbalance

**Определено в:** `/home/user/ChaosCash/tests/test_integrity_service.py:45`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_division

**Определено в:** `/home/user/ChaosCash/tests/test_expression_parser.py:30`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_division_by_zero

**Определено в:** `/home/user/ChaosCash/tests/test_expression_parser.py:50`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_duplicate_transaction

**Определено в:** `/home/user/ChaosCash/tests/test_transaction_service.py:58`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_empty_account_balance

**Определено в:** `/home/user/ChaosCash/tests/test_balance_service.py:41`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_empty_string

**Определено в:** `/home/user/ChaosCash/tests/test_expression_parser.py:60`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_float_number

**Определено в:** `/home/user/ChaosCash/tests/test_expression_parser.py:14`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_grp_account_balance

**Определено в:** `/home/user/ChaosCash/tests/test_balance_service.py:70`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_invalid_expression

**Определено в:** `/home/user/ChaosCash/tests/test_expression_parser.py:55`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_multi_currency_balance

**Определено в:** `/home/user/ChaosCash/tests/test_balance_service.py:57`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_multiplication

**Определено в:** `/home/user/ChaosCash/tests/test_expression_parser.py:26`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_negative

**Определено в:** `/home/user/ChaosCash/tests/test_expression_parser.py:38`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_no_empty_transactions_initially

**Определено в:** `/home/user/ChaosCash/tests/test_integrity_service.py:68`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_no_imbalance_initially

**Определено в:** `/home/user/ChaosCash/tests/test_integrity_service.py:41`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_parentheses

**Определено в:** `/home/user/ChaosCash/tests/test_expression_parser.py:34`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_recalculate_flexible_splits

**Определено в:** `/home/user/ChaosCash/tests/test_transaction_service.py:110`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_recalculate_flexible_splits_rebalances_existing_imbalance

**Определено в:** `/home/user/ChaosCash/tests/test_transaction_service.py:132`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_recalculate_flexible_splits_returns_false_without_flexible_split

**Определено в:** `/home/user/ChaosCash/tests/test_transaction_service.py:150`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_reverse_transaction

**Определено в:** `/home/user/ChaosCash/tests/test_transaction_service.py:75`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_simple_number

**Определено в:** `/home/user/ChaosCash/tests/test_expression_parser.py:10`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_single_currency_balance

**Определено в:** `/home/user/ChaosCash/tests/test_balance_service.py:47`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_subtraction

**Определено в:** `/home/user/ChaosCash/tests/test_expression_parser.py:22`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_update_split_fixed

**Определено в:** `/home/user/ChaosCash/tests/test_transaction_service.py:92`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_whitespace

**Определено в:** `/home/user/ChaosCash/tests/test_expression_parser.py:64`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### test_zero_split_detection

**Определено в:** `/home/user/ChaosCash/tests/test_integrity_service.py:72`

**Тип:** Функция

**Использования:** Нет (возможно, неиспользуемая функция)

### tr

**Определено в:** `/home/user/ChaosCash/app/i18n/translator.py:4`

**Тип:** Функция

**Использования (92 мест):**

- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:24`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:36`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:42`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:43`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:91`
- `/home/user/ChaosCash/app/ui/dialogs/currency_editor_dialog.py:92`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:116`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:120`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:121`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:122`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:42`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:65`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:69`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:70`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:82`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:86`
- `/home/user/ChaosCash/app/ui/dialogs/delete_account_dialog.py:87`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:14`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:23`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:27`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:31`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:34`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:36`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:41`
- `/home/user/ChaosCash/app/ui/dialogs/settings_dialog.py:45`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:103`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:203`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:204`
- `/home/user/ChaosCash/app/ui/item_models/account_tree_model.py:99`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:153`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:154`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:155`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:156`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:157`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:158`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:159`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:203`
- `/home/user/ChaosCash/app/ui/item_models/split_model.py:214`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:122`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:123`
- `/home/user/ChaosCash/app/ui/item_models/transaction_model.py:23`
- `/home/user/ChaosCash/app/ui/main_window.py:163`
- `/home/user/ChaosCash/app/ui/main_window.py:165`
- `/home/user/ChaosCash/app/ui/main_window.py:170`
- `/home/user/ChaosCash/app/ui/main_window.py:176`
- `/home/user/ChaosCash/app/ui/main_window.py:182`
- `/home/user/ChaosCash/app/ui/main_window.py:188`
- `/home/user/ChaosCash/app/ui/main_window.py:193`
- `/home/user/ChaosCash/app/ui/main_window.py:195`
- `/home/user/ChaosCash/app/ui/main_window.py:201`
- `/home/user/ChaosCash/app/ui/main_window.py:209`
- `/home/user/ChaosCash/app/ui/main_window.py:211`
- `/home/user/ChaosCash/app/ui/main_window.py:212`
- `/home/user/ChaosCash/app/ui/main_window.py:214`
- `/home/user/ChaosCash/app/ui/main_window.py:227`
- `/home/user/ChaosCash/app/ui/main_window.py:229`
- `/home/user/ChaosCash/app/ui/main_window.py:233`
- `/home/user/ChaosCash/app/ui/main_window.py:830`
- `/home/user/ChaosCash/app/ui/main_window.py:831`
- `/home/user/ChaosCash/app/ui/main_window.py:845`
- `/home/user/ChaosCash/app/ui/main_window.py:846`
- `/home/user/ChaosCash/app/ui/main_window.py:853`
- `/home/user/ChaosCash/app/ui/main_window.py:854`
- `/home/user/ChaosCash/app/ui/main_window.py:864`
- `/home/user/ChaosCash/app/ui/main_window.py:865`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:168`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:176`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:190`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:300`
- `/home/user/ChaosCash/app/ui/widgets/account_tree_view.py:301`
- `/home/user/ChaosCash/app/ui/widgets/split_view.py:110`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:134`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:138`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:144`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:161`
- `/home/user/ChaosCash/app/ui/widgets/transaction_view.py:162`

