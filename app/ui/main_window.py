"""Main application window."""
import sqlite3
import os
from PyQt6.QtWidgets import (
    QMainWindow, QSplitter, QVBoxLayout, QWidget, QHeaderView,
    QFileDialog, QMessageBox, QApplication, QMenu
)
from PyQt6.QtCore import Qt, QModelIndex, QTimer, QItemSelectionModel
from PyQt6.QtGui import QAction

from app.i18n import tr
from app.settings.app_settings import AppSettings
from app.database.connection import open_connection
from app.database.schema import ensure_schema
from app.repositories.account_repo import AccountRepo
from app.repositories.transaction_repo import TransactionRepo
from app.repositories.split_repo import SplitRepo
from app.repositories.currency_repo import CurrencyRepo
from app.services.balance_service import BalanceService
from app.services.transaction_service import TransactionService
from app.services.integrity_service import IntegrityService
from app.ui.item_models.account_tree_model import AccountTreeModel
from app.ui.item_models.transaction_model import TransactionModel
from app.ui.item_models.split_model import (
    SplitModel, ROW_PHANTOM, ROW_NEW, COL_ACCOUNT, COL_AMOUNT, COL_CURRENCY, COL_FIXED
)
from app.ui.widgets.account_tree_view import AccountTreeView
from app.ui.widgets.transaction_view import TransactionView
from app.ui.widgets.split_view import SplitView
from app.ui.delegates.date_delegate import DateDelegate
from app.ui.delegates.amount_delegate import AmountDelegate
from app.ui.delegates.account_combo_delegate import AccountComboDelegate
from app.ui.delegates.currency_combo_delegate import CurrencyComboDelegate
from app.ui.dialogs.settings_dialog import SettingsDialog
from app.ui.dialogs.currency_editor_dialog import CurrencyEditorDialog
from app.utils.recent_files import add_recent_file, get_recent_files
from app.utils.amount_math import float_to_quants
from app.utils.expression_parser import safe_eval
from app.ui.item_models.account_tree_model import VIRTUAL_IMBALANCE_ID, VIRTUAL_EMPTY_ID
from datetime import datetime, timezone

UTC = timezone.utc


class MainWindow(QMainWindow):
    """One main window per open database file."""

    def __init__(self, db_path: str, settings: AppSettings, parent=None):
        super().__init__(parent)
        self.db_path = db_path
        self.settings = settings
        self._conn: sqlite3.Connection = open_connection(db_path)
        ensure_schema(self._conn)

        # Repos
        self.account_repo = AccountRepo(self._conn)
        self.trans_repo = TransactionRepo(self._conn)
        self.split_repo = SplitRepo(self._conn)
        self.currency_repo = CurrencyRepo(self._conn)

        # Services
        self.balance_service = BalanceService(self.account_repo, self.split_repo)
        self.trans_service = TransactionService(self.trans_repo, self.split_repo)
        self.integrity_service = IntegrityService(self.trans_repo, self.split_repo, self._conn)

        # State
        self._selected_account_ids: list[int] = []
        self._current_trans_id: int | None = None
        self._virtual_mode: int | None = None  # VIRTUAL_IMBALANCE_ID or VIRTUAL_EMPTY_ID

        # New-transaction entry flow state
        self._new_trans_entry_mode: bool = False
        # (row, col) to focus in split view after next split_model.load(); row=-1 means last
        self._post_reload_focus: tuple[int, int] | None = None

        self._setup_ui()
        self._setup_menu()
        self._setup_models()
        self._setup_delegates()
        self._connect_signals()
        self._refresh_integrity()

        add_recent_file(db_path)
        self.setWindowTitle(os.path.basename(db_path))
        self.resize(1400, 900)

    # --- UI Setup ---

    def _setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_splitter = QSplitter(Qt.Orientation.Horizontal)

        # Left: account tree
        self.account_tree = AccountTreeView(
            self.account_repo, self.trans_repo, self.split_repo,
            self.balance_service, self.settings
        )

        # Right: transactions + splits
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0, 0, 0, 0)

        self.right_splitter = QSplitter(Qt.Orientation.Vertical)

        self.transaction_view = TransactionView(self.trans_service)
        self.split_view = SplitView(self.trans_service)

        self.right_splitter.addWidget(self.transaction_view)
        self.right_splitter.addWidget(self.split_view)
        self.right_splitter.setSizes([500, 300])
        right_layout.addWidget(self.right_splitter)

        self.main_splitter.addWidget(self.account_tree)
        self.main_splitter.addWidget(right_widget)
        self.main_splitter.setSizes([300, 1100])

        main_layout.addWidget(self.main_splitter)

    def _setup_menu(self):
        menubar = self.menuBar()

        # File menu
        file_menu = menubar.addMenu(tr("&File"))

        new_action = QAction(tr("&New..."), self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self._new_file)
        file_menu.addAction(new_action)

        open_action = QAction(tr("&Open..."), self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self._open_file)
        file_menu.addAction(open_action)

        # Recent files submenu
        self.recent_menu = QMenu(tr("Recent Files"), self)
        file_menu.addMenu(self.recent_menu)
        self._refresh_recent_menu()

        file_menu.addSeparator()

        add_acc_action = QAction(tr("&Add Account"), self)
        add_acc_action.triggered.connect(lambda: self.account_tree._add_account(QModelIndex()))
        file_menu.addAction(add_acc_action)

        file_menu.addSeparator()

        close_action = QAction(tr("&Close"), self)
        close_action.triggered.connect(self.close)
        file_menu.addAction(close_action)

        # View menu
        view_menu = menubar.addMenu(tr("&View"))

        self.act_show_hidden = QAction(tr("Show &Hidden Accounts"), self)
        self.act_show_hidden.setCheckable(True)
        self.act_show_hidden.setChecked(self.settings.show_hidden_accounts)
        self.act_show_hidden.toggled.connect(self._toggle_show_hidden)
        view_menu.addAction(self.act_show_hidden)

        self.act_show_balances = QAction(tr("Show &Balances"), self)
        self.act_show_balances.setCheckable(True)
        self.act_show_balances.setChecked(self.settings.show_balances)
        self.act_show_balances.toggled.connect(self._toggle_show_balances)
        view_menu.addAction(self.act_show_balances)

        view_menu.addSeparator()

        self.act_verbose = QAction(tr("&Verbose Mode"), self)
        self.act_verbose.setCheckable(True)
        self.act_summary = QAction(tr("&Summary Mode"), self)
        self.act_summary.setCheckable(True)

        mode = self.settings.transaction_view_mode
        self.act_verbose.setChecked(mode == "verbose")
        self.act_summary.setChecked(mode == "summary")

        self.act_verbose.triggered.connect(lambda: self._set_view_mode("verbose"))
        self.act_summary.triggered.connect(lambda: self._set_view_mode("summary"))
        view_menu.addAction(self.act_verbose)
        view_menu.addAction(self.act_summary)

        # Tools menu
        tools_menu = menubar.addMenu(tr("&Tools"))

        currencies_action = QAction(tr("&Currency Editor..."), self)
        currencies_action.triggered.connect(self._open_currency_editor)
        tools_menu.addAction(currencies_action)

        settings_action = QAction(tr("&Settings..."), self)
        settings_action.triggered.connect(self._open_settings)
        tools_menu.addAction(settings_action)

    def _setup_models(self):
        # Account tree model
        self.account_model = AccountTreeModel(
            self.account_repo, self.balance_service,
            self.currency_repo, self.settings
        )
        self.account_tree.setModel(self.account_model)
        self.account_tree.expandAll()
        hdr = self.account_tree.header()
        hdr.setStretchLastSection(False)
        hdr.setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)
        hdr.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
        hdr.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)
        hdr.resizeSection(0, 200)
        hdr.resizeSection(1, 120)
        hdr.resizeSection(2, 70)

        # Transaction model
        self.trans_model = TransactionModel(
            self.trans_repo, self.currency_repo, self.settings
        )
        self.transaction_view.setModel(self.trans_model)
        th = self.transaction_view.horizontalHeader()
        th.setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        # Auto-size date column to fit the configured date format
        try:
            fmt = self.settings.date_format
            fmt = fmt.replace("yyyy", "%Y").replace("MM", "%m").replace("dd", "%d")
            fmt = fmt.replace("HH", "%H").replace("mm", "%M").replace("ss", "%S")
            sample = datetime.now().strftime(fmt)
            date_width = self.transaction_view.fontMetrics().horizontalAdvance(sample) + 20
        except Exception:
            date_width = 150
        th.setSectionResizeMode(1, QHeaderView.ResizeMode.Interactive)
        th.resizeSection(1, date_width)

        # Split model
        self.split_model = SplitModel(
            self.split_repo, self.account_repo, self.currency_repo, self.settings
        )
        self.split_view.setModel(self.split_model)
        sh = self.split_view.horizontalHeader()
        sh.setStretchLastSection(False)
        # Description (col 1) gets all the extra space
        sh.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        sh.setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)
        sh.setSectionResizeMode(2, QHeaderView.ResizeMode.Interactive)
        sh.setSectionResizeMode(3, QHeaderView.ResizeMode.Interactive)
        sh.setSectionResizeMode(4, QHeaderView.ResizeMode.Interactive)
        sh.setSectionResizeMode(5, QHeaderView.ResizeMode.Interactive)
        sh.resizeSection(0, 80)   # Ext. ID
        sh.resizeSection(2, 150)  # Account
        sh.resizeSection(3, 50)   # Fixed
        sh.resizeSection(4, 100)  # Amount
        sh.resizeSection(5, 70)   # Currency

    def _setup_delegates(self):
        # Transaction view delegates
        date_delegate = DateDelegate(self.settings, self.transaction_view)
        self.transaction_view.setItemDelegateForColumn(1, date_delegate)

        # Split view delegates
        amount_delegate = AmountDelegate(self.settings, self.split_view)
        self.split_view.setItemDelegateForColumn(4, amount_delegate)

        account_delegate = AccountComboDelegate(self.account_repo, self.settings, self.split_view)
        self.split_view.setItemDelegateForColumn(2, account_delegate)

        currency_delegate = CurrencyComboDelegate(self.currency_repo, self.split_view)
        self.split_view.setItemDelegateForColumn(5, currency_delegate)

    def _connect_signals(self):
        self.account_tree.account_selected.connect(self._on_accounts_selected)
        self.account_tree.virtual_node_selected.connect(self._on_virtual_node_selected)
        self.transaction_view.transaction_selected.connect(self._on_transaction_selected)
        self.transaction_view.transactions_changed.connect(self._on_transactions_changed)
        self.split_view.split_changed.connect(self._on_split_changed)

        # React to model data changes
        self.split_model.dataChanged.connect(self._on_split_data_changed)
        self.trans_model.dataChanged.connect(self._on_trans_data_changed)
        self.trans_model.new_transaction_requested.connect(self._on_new_transaction_requested)

    # --- New transaction entry flow ---

    def _on_new_transaction_requested(self, description: str, date: str):
        """Called when user commits description in the phantom transaction row."""
        if not self._selected_account_ids:
            return
        active_account_id = self._selected_account_ids[0]

        # Get last used currency for this account, fall back to first available
        cur_id = self.split_repo.get_last_currency_for_account(active_account_id)
        if cur_id is None:
            currencies = self.currency_repo.get_all()
            if not currencies:
                return
            cur_id = currencies[0].id

        # Create transaction
        trans_id = self.trans_service.create_transaction(description, date)
        self._current_trans_id = trans_id

        # Create first split on the active account with amount=0 (user will fill it)
        self.trans_service.add_split(
            trans_id, active_account_id, cur_id, amount=0, amount_fixed=False
        )

        self._new_trans_entry_mode = True
        # After reload focus: row 0 (first real split), col COL_AMOUNT
        self._post_reload_focus = (0, COL_AMOUNT)

        # Load split panel and refresh transaction list
        self.split_model.load(trans_id)
        if self._selected_account_ids:
            self.trans_model.load(self._selected_account_ids)
            row = self.trans_model.find_row_for_trans(trans_id)
            if row >= 0:
                self.transaction_view.setCurrentIndex(self.trans_model.index(row, 0))

        self.balance_service.clear()
        self._refresh_integrity()

        # Focus the amount cell of the first split
        QTimer.singleShot(0, lambda: self._focus_split_cell(0, COL_AMOUNT))

    def _focus_split_cell(self, row: int, col: int):
        """Focus and start editing a cell in the split view.
        row=-1 means: search for the first phantom row."""
        if row == -1:
            row = -1
            for i in range(self.split_model.rowCount()):
                if self.split_model.get_row_type(i) == ROW_PHANTOM:
                    row = i
                    break
            if row == -1:
                self._new_trans_entry_mode = False
                return
        idx = self.split_model.index(row, col)
        if idx.isValid() and (self.split_model.flags(idx) & Qt.ItemFlag.ItemIsEditable):
            self.split_view.setCurrentIndex(idx)
            self.split_view.edit(idx)

    # --- Slots ---

    def _on_accounts_selected(self, account_ids: list[int]):
        self._new_trans_entry_mode = False
        self._post_reload_focus = None
        self._selected_account_ids = account_ids
        self._virtual_mode = None
        self._load_transactions()

    def _on_virtual_node_selected(self, virtual_id: int):
        self._new_trans_entry_mode = False
        self._post_reload_focus = None
        self._virtual_mode = virtual_id
        self._load_virtual_transactions(virtual_id)

    def _load_transactions(self):
        self.trans_model.load(self._selected_account_ids)
        self.split_model.load(None)
        self._current_trans_id = None

    def _load_virtual_transactions(self, virtual_id: int):
        """Load transactions for virtual nodes (imbalance, empty)."""
        if virtual_id == VIRTUAL_IMBALANCE_ID:
            trans_ids = self.integrity_service.get_imbalanced_trans_ids()
        elif virtual_id == VIRTUAL_EMPTY_ID:
            empty = self.integrity_service.get_empty_transactions()
            trans_ids = [t.id for t in empty]
        else:
            trans_ids = []
        self.trans_model.load_by_ids(trans_ids)
        self.split_model.load(None)
        self._current_trans_id = None

    def _on_transaction_selected(self, trans_id: int):
        self._new_trans_entry_mode = False
        self._post_reload_focus = None
        self._current_trans_id = trans_id
        self.split_model.load(trans_id)
        zero_ids = set(self.integrity_service.get_zero_split_ids())
        self.split_model.set_zero_split_ids(zero_ids)

    def _on_transactions_changed(self):
        self._new_trans_entry_mode = False
        self._post_reload_focus = None
        self.balance_service.clear()
        self._refresh_integrity()
        self._load_transactions()

    def _on_split_changed(self):
        self.balance_service.clear()
        self._refresh_integrity()
        if self._current_trans_id:
            self.split_model.load(self._current_trans_id)
        if self._virtual_mode is not None:
            # Reload only the transaction list; do NOT reset split_model or
            # _current_trans_id — that would wipe the split panel while editing.
            if self._virtual_mode == VIRTUAL_IMBALANCE_ID:
                trans_ids = self.integrity_service.get_imbalanced_trans_ids()
            elif self._virtual_mode == VIRTUAL_EMPTY_ID:
                empty = self.integrity_service.get_empty_transactions()
                trans_ids = [t.id for t in empty]
            else:
                trans_ids = []
            self.trans_model.load_by_ids(trans_ids)
            if self._current_trans_id:
                row = self.trans_model.find_row_for_trans(self._current_trans_id)
                if row >= 0:
                    self.transaction_view.setCurrentIndex(
                        self.trans_model.index(row, 0))
        elif self._selected_account_ids:
            self.trans_model.load(self._selected_account_ids)
            # Re-select current transaction after model reload
            if self._current_trans_id:
                row = self.trans_model.find_row_for_trans(self._current_trans_id)
                if row >= 0:
                    self.transaction_view.setCurrentIndex(
                        self.trans_model.index(row, 0))
        self.account_model.reload()
        self.account_tree.expandAll()

        # Restore account tree selection after account_model.reload() wipes it.
        sel_model = self.account_tree.selectionModel()
        if self._virtual_mode is not None:
            # Virtual node: selectionChanged fires but _on_selection_changed filters
            # out virtual nodes, so account_selected is not emitted → no re-load.
            for row in range(self.account_model.rowCount()):
                idx = self.account_model.index(row, 0)
                node = self.account_model.get_node(idx)
                if node and node.is_virtual and node.virtual_id == self._virtual_mode:
                    sel_model.select(idx, QItemSelectionModel.SelectionFlag.ClearAndSelect)
                    break
        elif self._selected_account_ids:
            # Regular accounts: block signals to prevent _on_selection_changed from
            # emitting account_selected, which would re-load transactions and clear splits.
            sel_model.blockSignals(True)
            try:
                first = True
                for acc_id in self._selected_account_ids:
                    idx = self.account_model.get_index_for_account(acc_id)
                    if idx.isValid():
                        flag = (QItemSelectionModel.SelectionFlag.ClearAndSelect if first
                                else QItemSelectionModel.SelectionFlag.Select)
                        sel_model.select(idx, flag)
                        first = False
            finally:
                sel_model.blockSignals(False)

        # Apply deferred split cell focus for new-transaction entry flow
        if self._post_reload_focus is not None:
            r, c = self._post_reload_focus
            self._post_reload_focus = None
            QTimer.singleShot(0, lambda row=r, col=c: self._focus_split_cell(row, col))

    def _on_trans_data_changed(self, top_left: QModelIndex, bottom_right: QModelIndex, roles):
        """Handle inline edits in transaction table (real rows only)."""
        row = top_left.row()
        trans_id = self.trans_model.get_trans_id(row)
        if trans_id is None:
            return
        date_val = self.trans_model.index(row, 1).data(Qt.ItemDataRole.EditRole)
        desc_val = self.trans_model.index(row, 2).data()
        if date_val and desc_val is not None:
            self.trans_service.update_transaction(trans_id, date_val, desc_val)
        QTimer.singleShot(0, self._on_split_changed)

    def _on_split_data_changed(self, top_left: QModelIndex, bottom_right: QModelIndex, roles):
        """Handle inline edits in split table."""
        # Ignore display-only role updates (e.g. BackgroundRole from set_zero_split_ids)
        if roles and Qt.ItemDataRole.EditRole not in roles \
                and Qt.ItemDataRole.CheckStateRole not in roles \
                and Qt.ItemDataRole.UserRole not in roles:
            return
        row = top_left.row()
        col = top_left.column()
        if col == COL_AMOUNT and roles and Qt.ItemDataRole.EditRole not in roles \
                and Qt.ItemDataRole.CheckStateRole not in roles:
            return
        model = self.split_model

        row_type = model.get_row_type(row)
        split = model.get_split(row)

        if row_type == ROW_PHANTOM:
            if col == COL_ACCOUNT:
                acc_id = model.index(row, COL_ACCOUNT).data(Qt.ItemDataRole.UserRole)
                cur_id, amount = model.get_phantom_info(row)
                if acc_id and cur_id and self._current_trans_id:
                    self.trans_service.add_split(
                        self._current_trans_id, acc_id, cur_id,
                        amount=amount, amount_fixed=False
                    )
                    if self._new_trans_entry_mode:
                        self._post_reload_focus = (1, COL_AMOUNT)
                        self._new_trans_entry_mode = False
                    QTimer.singleShot(0, self._on_split_changed)
            return

        if row_type == ROW_NEW:
            acc_id = model.index(row, COL_ACCOUNT).data(Qt.ItemDataRole.UserRole)
            cur_id = model.index(row, COL_CURRENCY).data(Qt.ItemDataRole.UserRole)
            amount_str = model.index(row, COL_AMOUNT).data(Qt.ItemDataRole.EditRole) or ""
            if acc_id and cur_id and amount_str and amount_str != "0" and self._current_trans_id:
                try:
                    amount_float = safe_eval(amount_str)
                except ValueError:
                    return
                cur = self.currency_repo.get_by_id(cur_id)
                denom = cur.denominator if cur else 100
                amount_quants = float_to_quants(amount_float, denom)
                if amount_quants != 0:
                    self.trans_service.add_split(
                        self._current_trans_id, acc_id, cur_id,
                        amount=amount_quants, amount_fixed=True
                    )
                    self.trans_service.recalculate_flexible_splits(
                        amount_quants, cur_id, self._current_trans_id
                    )
                    QTimer.singleShot(0, self._on_split_changed)
            return

        if split is None:
            return

        # Handle Fixed checkbox toggle directly — avoids re-parsing amount
        if col == COL_FIXED:
            fixed_state = model.index(row, COL_FIXED).data(Qt.ItemDataRole.CheckStateRole)
            if fixed_state is not None:
                fixed_checked = fixed_state == Qt.CheckState.Checked
                self.trans_service.update_split_fixed(split.id, fixed_checked)
                if self._current_trans_id and not fixed_checked:
                    currency_splits = self.split_repo.get_by_transaction_and_currency(
                        self._current_trans_id, split.currency
                    )
                    imbalance = sum(s.amount for s in currency_splits)
                    self.trans_service.recalculate_flexible_splits(
                        imbalance, split.currency, self._current_trans_id
                    )
                QTimer.singleShot(0, self._on_split_changed)
            return

        # Gather current values from model
        ext_id = model.index(row, 0).data() or None
        desc = model.index(row, 1).data() or None
        acc_id = model.index(row, COL_ACCOUNT).data(Qt.ItemDataRole.UserRole) or split.account
        amount_str = model.index(row, COL_AMOUNT).data() or "0"
        cur_id = model.index(row, COL_CURRENCY).data(Qt.ItemDataRole.UserRole) or split.currency

        fixed_state = model.index(row, 3).data(Qt.ItemDataRole.CheckStateRole)
        amount_fixed = (fixed_state == Qt.CheckState.Checked
                        if fixed_state is not None else split.amount_fixed)

        try:
            amount_float = safe_eval(amount_str)
        except ValueError:
            return

        cur = self.currency_repo.get_by_id(cur_id)
        denom = cur.denominator if cur else 100
        amount_quants = float_to_quants(amount_float, denom)

        if col == COL_AMOUNT:
            prev_amount_text = model._format_amt(split.amount, split.currency)
            raw_amount_input = model.index(row, COL_AMOUNT).data(Qt.ItemDataRole.UserRole)
            edited_text = raw_amount_input if isinstance(raw_amount_input, str) else amount_str
            if str(edited_text).strip() != str(prev_amount_text).strip():
                amount_fixed = True

        self.trans_service.update_split(
            split.id, acc_id, cur_id, desc, ext_id, amount_quants, amount_fixed
        )

        # Proportional recalculation / imbalance auto-distribution when amount changes
        if col == COL_AMOUNT and self._current_trans_id:
            delta_amount = amount_quants - split.amount
            self.trans_service.recalculate_flexible_splits(
                delta_amount, cur_id, self._current_trans_id
            )

        # New-transaction entry flow: advance focus after each step
        if self._new_trans_entry_mode:
            if col == COL_AMOUNT:
                self._post_reload_focus = (row, COL_CURRENCY)
            elif col == COL_CURRENCY:
                # After currency is set → focus phantom counter-split account
                self._post_reload_focus = (-1, COL_ACCOUNT)

        if self._current_trans_id:
            affected_currencies = {cur_id, split.currency}
            for affected_currency in affected_currencies:
                currency_splits = self.split_repo.get_by_transaction_and_currency(
                    self._current_trans_id, affected_currency
                )
                imbalance = sum(s.amount for s in currency_splits)
                self.trans_service.recalculate_flexible_splits(
                    imbalance, affected_currency, self._current_trans_id
                )

        QTimer.singleShot(0, self._on_split_changed)

    def _toggle_show_hidden(self, checked: bool):
        self.settings.show_hidden_accounts = checked
        self.account_model.reload()
        self.account_tree.expandAll()

    def _toggle_show_balances(self, checked: bool):
        self.settings.show_balances = checked
        self.account_model.reload()

    def _set_view_mode(self, mode: str):
        self.settings.transaction_view_mode = mode
        self.act_verbose.setChecked(mode == "verbose")
        self.act_summary.setChecked(mode == "summary")
        self._load_transactions()

    def _refresh_integrity(self):
        has_imbalance = self.integrity_service.has_imbalance()
        has_empty = self.integrity_service.has_empty_transactions()
        self.account_model.set_virtual_nodes(has_imbalance, has_empty)
        self.account_tree.expandAll()

        # Check FK violations on startup
        violations = self.integrity_service.check_foreign_keys()
        if violations:
            QMessageBox.warning(
                self, tr("Database Integrity Warning"),
                tr("Foreign key violations detected:\n") + "\n".join(violations[:10])
            )

    def _refresh_recent_menu(self):
        self.recent_menu.clear()
        for path in get_recent_files():
            action = QAction(path, self)
            action.triggered.connect(lambda checked, p=path: self._open_file_path(p))
            self.recent_menu.addAction(action)

    # --- File operations ---

    def _new_file(self):
        path, _ = QFileDialog.getSaveFileName(
            self, tr("New Database"), "",
            tr("ChaosCash Database (*.ccash *.db);;All Files (*)")
        )
        if path:
            self._open_file_path(path)

    def _open_file(self):
        path, _ = QFileDialog.getOpenFileName(
            self, tr("Open Database"), "",
            tr("ChaosCash Database (*.ccash *.db);;All Files (*)")
        )
        if path:
            self._open_file_path(path)

    def _open_file_path(self, path: str):
        app = QApplication.instance()
        for widget in app.topLevelWidgets():
            if isinstance(widget, MainWindow) and widget.db_path == path and widget is not self:
                QMessageBox.warning(
                    self, tr("File Already Open"),
                    tr(f"'{path}' is already open in another window.")
                )
                widget.raise_()
                return
        new_window = MainWindow(path, self.settings)
        new_window.show()

    def _open_currency_editor(self):
        dlg = CurrencyEditorDialog(self.currency_repo, self)
        if dlg.exec():
            self._on_split_changed()

    def _open_settings(self):
        dlg = SettingsDialog(self.settings, self)
        if dlg.exec():
            self.account_model.reload()
            self.account_tree.expandAll()
            if self._selected_account_ids:
                self.trans_model.load(self._selected_account_ids)
            if self._current_trans_id:
                self.split_model.load(self._current_trans_id)

    def closeEvent(self, event):
        try:
            self._conn.close()
        except Exception:
            pass
        super().closeEvent(event)
