"""Dialog for deleting an account with multiple options."""
from PyQt6.QtWidgets import (
    QButtonGroup,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QGroupBox,
    QHBoxLayout,
    QRadioButton,
    QVBoxLayout,
)

from app.i18n import tr
from app.repositories.account_repo import AccountRepo
from app.repositories.split_repo import SplitRepo
from app.ui.account_selection import get_selectable_account_items


class DeleteAccountDialog(QDialog):
    """
    Options:
    - Hide account
    - Delete account (physically delete from database)

    Sub-accounts handling:
    - Move to another account (default: parent)
    - Delete recursively

    Transactions handling:
    - Move splits to another account (default: parent)
    - Delete all splits
    - Delete all transactions
    """
    HIDE = "hide"
    DELETE = "delete"

    # Sub-accounts actions
    MOVE_SUBACCOUNTS = "move_subaccounts"
    DELETE_SUBACCOUNTS = "delete_subaccounts"

    # Transactions actions
    MOVE_SPLITS = "move_splits"
    DELETE_SPLITS = "delete_splits"
    DELETE_TRANS = "delete_trans"

    def __init__(self, account_name: str, account_repo: AccountRepo,
                 split_repo: SplitRepo, settings, exclude_id: int, parent=None):
        super().__init__(parent)
        self.setWindowTitle(tr("Delete Account"))
        self.setModal(True)
        self.account_repo = account_repo
        self.split_repo = split_repo
        self.exclude_id = exclude_id
        self.settings = settings

        self._action = self.HIDE
        self._subaccounts_action = self.MOVE_SUBACCOUNTS
        self._subaccounts_target_id: int | None = None
        self._transactions_action = self.MOVE_SPLITS
        self._transactions_target_id: int | None = None

        # Check if account has sub-accounts and splits
        self._has_subaccounts = self._check_has_subaccounts()
        self._has_splits = self._check_has_splits()

        # Get parent account ID for defaults
        self._parent_id = account_repo.get_parent_id(exclude_id)

        layout = QVBoxLayout(self)

        # Action section
        action_group = QGroupBox(tr("Action"))
        action_layout = QVBoxLayout(action_group)
        self.action_group = QButtonGroup(self)

        self.rb_hide = QRadioButton(tr("Hide (recommended for closed accounts)"))
        self.rb_delete = QRadioButton(tr(f"Delete account {account_name}"))

        self.rb_hide.setChecked(True)
        self.action_group.addButton(self.rb_hide, 0)
        self.action_group.addButton(self.rb_delete, 1)
        action_layout.addWidget(self.rb_hide)
        action_layout.addWidget(self.rb_delete)

        layout.addWidget(action_group)

        # Sub-accounts section (only if sub-accounts exist)
        if self._has_subaccounts:
            subaccounts_group = QGroupBox(tr("Sub-accounts"))
            subaccounts_layout = QVBoxLayout(subaccounts_group)
            self.subaccounts_group = QButtonGroup(self)

            self.rb_move_subaccounts = QRadioButton(tr("Move to:"))
            self.rb_delete_recursive = QRadioButton(tr("Delete recursively"))

            self.subaccounts_group.addButton(self.rb_move_subaccounts, 0)
            self.subaccounts_group.addButton(self.rb_delete_recursive, 1)
            self.rb_move_subaccounts.setChecked(True)

            move_subaccounts_layout = QHBoxLayout()
            move_subaccounts_layout.addWidget(self.rb_move_subaccounts)
            self.subaccounts_combo = QComboBox()
            self._populate_subaccounts_combo()
            move_subaccounts_layout.addWidget(self.subaccounts_combo)
            move_subaccounts_layout.addStretch()
            subaccounts_layout.addLayout(move_subaccounts_layout)
            subaccounts_layout.addWidget(self.rb_delete_recursive)

            layout.addWidget(subaccounts_group)

            # Connect signals
            self.rb_move_subaccounts.toggled.connect(lambda checked: self.subaccounts_combo.setEnabled(checked))
            self.rb_delete_recursive.toggled.connect(lambda checked: self.subaccounts_combo.setEnabled(not checked))
            # Update transactions dropdown when sub-accounts action changes
            self.rb_move_subaccounts.toggled.connect(self._update_transactions_combo)
            self.rb_delete_recursive.toggled.connect(self._update_transactions_combo)
        else:
            self.subaccounts_group = None
            self.subaccounts_combo = None

        # Transactions section (only if splits exist)
        if self._has_splits:
            transactions_group = QGroupBox(tr("Transactions (including sub-accounts)"))
            transactions_layout = QVBoxLayout(transactions_group)
            self.transactions_group = QButtonGroup(self)

            self.rb_move_splits = QRadioButton(tr("Move splits to:"))
            self.rb_delete_splits = QRadioButton(tr("Delete all splits (can create imbalance)"))
            self.rb_delete_trans = QRadioButton(tr("Delete all transactions (can affect balance on other accounts)"))

            self.transactions_group.addButton(self.rb_move_splits, 0)
            self.transactions_group.addButton(self.rb_delete_splits, 1)
            self.transactions_group.addButton(self.rb_delete_trans, 2)
            self.rb_move_splits.setChecked(True)

            move_splits_layout = QHBoxLayout()
            move_splits_layout.addWidget(self.rb_move_splits)
            self.transactions_combo = QComboBox()
            self._populate_transactions_combo()
            move_splits_layout.addWidget(self.transactions_combo)
            move_splits_layout.addStretch()
            transactions_layout.addLayout(move_splits_layout)
            transactions_layout.addWidget(self.rb_delete_splits)
            transactions_layout.addWidget(self.rb_delete_trans)

            layout.addWidget(transactions_group)

            # Connect signals
            self.rb_move_splits.toggled.connect(lambda checked: self.transactions_combo.setEnabled(checked))
            self.rb_delete_splits.toggled.connect(lambda checked: self.transactions_combo.setEnabled(not checked))
            self.rb_delete_trans.toggled.connect(lambda checked: self.transactions_combo.setEnabled(not checked))
        else:
            self.transactions_group = None
            self.transactions_combo = None

        layout.addStretch()

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok |
                                   QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self._accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        # Connect action changes to update sub-sections
        self.rb_hide.toggled.connect(self._on_action_changed)
        self.rb_delete.toggled.connect(self._on_action_changed)

        # Initialize UI state (disable sections since Hide is default)
        self._on_action_changed()

    def _check_has_subaccounts(self) -> bool:
        """Check if account has any sub-accounts."""
        children = self.account_repo.get_children(self.exclude_id)
        return len(children) > 0

    def _check_has_splits(self) -> bool:
        """Check if account or any of its sub-accounts have splits."""
        # Get all descendants including the account itself
        all_account_ids = [self.exclude_id]
        all_account_ids.extend(self.account_repo.get_all_descendants(self.exclude_id))

        # Check if any of these accounts have splits
        for account_id in all_account_ids:
            if self.split_repo.has_splits_for_account(account_id):
                return True
        return False

    def _populate_subaccounts_combo(self):
        """Populate sub-accounts dropdown with accounts to move to."""
        if self.subaccounts_combo is None:
            return

        self.subaccounts_combo.clear()
        descendants = set(self.account_repo.get_all_descendants(self.exclude_id))
        descendants.add(self.exclude_id)

        if self._parent_id is not None and self._parent_id not in descendants:
            parent_acc = self.account_repo.get_by_id(self._parent_id)
            if parent_acc:
                path = self.account_repo.get_account_path(self._parent_id)
                self.subaccounts_combo.addItem(path, self._parent_id)

        excluded_ids = set(descendants)
        if self._parent_id is not None:
            excluded_ids.add(self._parent_id)
        items = get_selectable_account_items(
            self.account_repo,
            self.settings,
            exclude_ids=excluded_ids,
        )
        for path, account_id in items:
            self.subaccounts_combo.addItem(path, account_id)

    def _populate_transactions_combo(self):
        """Populate transactions dropdown with accounts to move splits to."""
        if self.transactions_combo is None:
            return

        self.transactions_combo.clear()

        delete_subaccounts = (self.subaccounts_group is not None and
                             self.rb_delete_recursive.isChecked())

        if delete_subaccounts:
            descendants = set(self.account_repo.get_all_descendants(self.exclude_id))
            descendants.add(self.exclude_id)
        else:
            descendants = {self.exclude_id}

        if self._parent_id is not None and self._parent_id not in descendants:
            parent_acc = self.account_repo.get_by_id(self._parent_id)
            if parent_acc:
                path = self.account_repo.get_account_path(self._parent_id)
                self.transactions_combo.addItem(path, self._parent_id)

        excluded_ids = set(descendants)
        if self._parent_id is not None:
            excluded_ids.add(self._parent_id)
        items = get_selectable_account_items(
            self.account_repo,
            self.settings,
            exclude_ids=excluded_ids,
        )
        for path, account_id in items:
            self.transactions_combo.addItem(path, account_id)

    def _update_transactions_combo(self):
        """Update transactions dropdown when sub-accounts action changes."""
        self._populate_transactions_combo()

    def _on_action_changed(self):
        """Handle action change to enable/disable sub-sections."""
        is_hide = self.rb_hide.isChecked()

        # Disable sub-sections when hide is selected
        if self.subaccounts_group is not None:
            for button in self.subaccounts_group.buttons():
                button.setEnabled(not is_hide)
            if self.subaccounts_combo:
                self.subaccounts_combo.setEnabled(not is_hide and self.rb_move_subaccounts.isChecked())

        if self.transactions_group is not None:
            for button in self.transactions_group.buttons():
                button.setEnabled(not is_hide)
            if self.transactions_combo:
                self.transactions_combo.setEnabled(not is_hide and self.rb_move_splits.isChecked())

    def _accept(self):
        """Handle OK button click."""
        # Action
        if self.rb_hide.isChecked():
            self._action = self.HIDE
        else:
            self._action = self.DELETE

        # Sub-accounts action
        if self.subaccounts_group is not None:
            if self.rb_move_subaccounts.isChecked():
                self._subaccounts_action = self.MOVE_SUBACCOUNTS
                self._subaccounts_target_id = self.subaccounts_combo.currentData()
            else:
                self._subaccounts_action = self.DELETE_SUBACCOUNTS

        # Transactions action
        if self.transactions_group is not None:
            if self.rb_move_splits.isChecked():
                self._transactions_action = self.MOVE_SPLITS
                self._transactions_target_id = self.transactions_combo.currentData()
            elif self.rb_delete_splits.isChecked():
                self._transactions_action = self.DELETE_SPLITS
            else:
                self._transactions_action = self.DELETE_TRANS

        self.accept()

    @property
    def action(self) -> str:
        return self._action

    @property
    def subaccounts_action(self) -> str:
        return self._subaccounts_action

    @property
    def subaccounts_target_id(self) -> int | None:
        return self._subaccounts_target_id

    @property
    def transactions_action(self) -> str:
        return self._transactions_action

    @property
    def transactions_target_id(self) -> int | None:
        return self._transactions_target_id
