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

    @classmethod
    def for_batch(cls, account_ids: list[int], account_repo: AccountRepo,
                  split_repo: SplitRepo, settings, parent=None):
        names = []
        for aid in account_ids:
            acc = account_repo.get_by_id(aid)
            if acc:
                names.append(acc.name or str(aid))
        names_str = ", ".join(names)
        if len(names_str) > 120:
            names_str = names_str[:117] + "..."
        display_name = names_str
        return cls(display_name, account_repo, split_repo, settings,
                   account_ids[0], parent, batch_account_ids=list(account_ids))

    def __init__(self, account_name: str, account_repo: AccountRepo,
                 split_repo: SplitRepo, settings, exclude_id: int, parent=None,
                 batch_account_ids: list[int] | None = None):
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
        self.batch_account_ids = batch_account_ids

        # Get parent account ID for defaults
        self._parent_id = account_repo.get_parent_id(exclude_id)

        if self.batch_account_ids and self._all_descendants_selected():
            self._subaccounts_collapsed = True
        else:
            self._subaccounts_collapsed = False

        # Check if account has sub-accounts and splits
        self._has_subaccounts = self._check_has_subaccounts() and not self._subaccounts_collapsed
        self._has_splits = self._check_has_splits()

        layout = QVBoxLayout(self)

        # Action section
        action_group = QGroupBox(tr("Action"))
        action_layout = QVBoxLayout(action_group)
        self.action_group = QButtonGroup(self)

        self.rb_hide = QRadioButton(tr("Hide (recommended for closed accounts)"))
        self.rb_delete = QRadioButton(tr("Delete account(s): ") + account_name)

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
            transactions_group = QGroupBox(tr("Transactions from deleted accounts"))
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

    def _account_ids(self) -> list[int]:
        if self.batch_account_ids:
            return self.batch_account_ids
        return [self.exclude_id]

    def _check_has_subaccounts(self) -> bool:
        """Check if any account has any sub-accounts."""
        ids = self._account_ids()
        for aid in ids:
            children = self.account_repo.get_children(aid)
            if children:
                return True
        return False

    def _check_has_splits(self) -> bool:
        """Check if any account or their sub-accounts have splits."""
        ids = self._account_ids()
        all_ids = []
        for aid in ids:
            all_ids.append(aid)
            all_ids.extend(self.account_repo.get_all_descendants(aid))
        for account_id in all_ids:
            if self.split_repo.has_splits_for_account(account_id):
                return True
        return False

    def _has_splits_for_accounts(self, account_ids: list[int]) -> bool:
        """Check if any account in list has splits."""
        for account_id in account_ids:
            if self.split_repo.has_splits_for_account(account_id):
                return True
        return False

    def _populate_subaccounts_combo(self):
        """Populate sub-accounts dropdown with accounts to move to."""
        if self.subaccounts_combo is None:
            return

        self.subaccounts_combo.clear()

        excluded_ids = self._build_excluded_ids()

        default_index = 0
        self.subaccounts_combo.addItem(tr("No parent (top level)"), None)

        if self._parent_id is not None and self._parent_id not in excluded_ids:
            parent_acc = self.account_repo.get_by_id(self._parent_id)
            if parent_acc:
                path = self.account_repo.get_account_path(self._parent_id)
                self.subaccounts_combo.addItem(path, self._parent_id)
                default_index = self.subaccounts_combo.count() - 1

        items = get_selectable_account_items(
            self.account_repo,
            self.settings,
            exclude_ids=excluded_ids,
        )
        for path, account_id in items:
            self.subaccounts_combo.addItem(path, account_id)

        if self.subaccounts_combo.count() > 0:
            self.subaccounts_combo.setCurrentIndex(default_index)

    def _all_descendants_selected(self) -> bool:
        """Check if all descendants of all selected accounts are included in selection."""
        ids = self._account_ids() or [self.exclude_id]
        for aid in ids:
            descendants = self.account_repo.get_all_descendants(aid)
            if descendants and not all(d in ids for d in descendants):
                return False
        return True

    def _build_excluded_ids(self) -> set[int]:
        """Return set of IDs that must be excluded from combo lists."""
        excluded = set()
        excluded.add(self.exclude_id)
        if self.batch_account_ids:
            excluded.update(self.batch_account_ids)
        for aid in list(excluded):
            excluded.update(self.account_repo.get_all_descendants(aid))
        return excluded

    def _populate_transactions_combo(self):
        """Populate transactions dropdown with accounts to move splits to."""
        if self.transactions_combo is None:
            return

        self.transactions_combo.clear()

        excluded_ids = self._build_excluded_ids()

        if self._parent_id is not None and self._parent_id not in excluded_ids:
            parent_acc = self.account_repo.get_by_id(self._parent_id)
            if parent_acc:
                path = self.account_repo.get_account_path(self._parent_id)
                self.transactions_combo.addItem(path, self._parent_id)

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
        self._update_transactions_section_state()

    def _deleted_accounts_for_current_choice(self) -> list[int]:
        """Return account IDs that will be deleted with current sub-accounts choice."""
        account_ids = self._account_ids()
        if self.subaccounts_group is not None and self.rb_delete_recursive.isChecked():
            for aid in list(account_ids):
                account_ids.extend(self.account_repo.get_all_descendants(aid))
        return account_ids

    def _update_transactions_section_state(self):
        """Enable transactions section only when deleted accounts have splits."""
        if self.transactions_group is None:
            return

        has_deleted_splits = self._has_splits_for_accounts(self._deleted_accounts_for_current_choice())
        is_hide = self.rb_hide.isChecked()
        section_enabled = (not is_hide) and has_deleted_splits

        for button in self.transactions_group.buttons():
            button.setEnabled(section_enabled)
        if self.transactions_combo:
            self.transactions_combo.setEnabled(section_enabled and self.rb_move_splits.isChecked())

    def _on_action_changed(self):
        """Handle action change to enable/disable sub-sections."""
        is_hide = self.rb_hide.isChecked()

        # Disable sub-sections when hide is selected
        if self.subaccounts_group is not None:
            for button in self.subaccounts_group.buttons():
                button.setEnabled(not is_hide)
            if self.subaccounts_combo:
                self.subaccounts_combo.setEnabled(not is_hide and self.rb_move_subaccounts.isChecked())

        self._update_transactions_section_state()

    def _accept(self):
        """Handle OK button click."""
        # Action
        if self.rb_hide.isChecked():
            self._action = self.HIDE
        else:
            self._action = self.DELETE

        # Sub-accounts action
        if self._subaccounts_collapsed:
            self._subaccounts_action = self.DELETE_SUBACCOUNTS
        elif self.subaccounts_group is not None:
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
