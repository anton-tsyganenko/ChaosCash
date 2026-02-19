"""Dialog for deleting an account with multiple options."""
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QRadioButton, QButtonGroup, QComboBox, QDialogButtonBox, QGroupBox
)
from PyQt6.QtCore import Qt
from app.i18n import tr
from app.repositories.account_repo import AccountRepo


class DeleteAccountDialog(QDialog):
    """
    Options:
    - Hide account (Status -> HID)
    - Move all splits to another account
    - Delete all splits for this account
    - Delete all transactions with splits on this account
    """
    HIDE = "hide"
    MOVE = "move"
    DELETE_SPLITS = "delete_splits"
    DELETE_TRANS = "delete_trans"

    def __init__(self, account_name: str, account_repo: AccountRepo,
                 exclude_id: int, parent=None):
        super().__init__(parent)
        self.setWindowTitle(tr("Delete Account"))
        self.setModal(True)
        self.account_repo = account_repo
        self.exclude_id = exclude_id
        self._action = self.HIDE
        self._target_account_id: int | None = None

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(tr(f"What to do with account '{account_name}'?")))

        group_box = QGroupBox(tr("Action"))
        group_layout = QVBoxLayout(group_box)

        self.btn_group = QButtonGroup(self)

        self.rb_hide = QRadioButton(tr("Hide account (recommended)"))
        self.rb_move = QRadioButton(tr("Move all splits to another account"))
        self.rb_del_splits = QRadioButton(tr("Delete all splits for this account"))
        self.rb_del_trans = QRadioButton(tr("Delete all transactions involving this account"))

        self.rb_hide.setChecked(True)
        for i, rb in enumerate([self.rb_hide, self.rb_move, self.rb_del_splits, self.rb_del_trans]):
            self.btn_group.addButton(rb, i)
            group_layout.addWidget(rb)

        # Account selector for MOVE option
        self.target_combo = QComboBox()
        self._populate_accounts()
        self.target_combo.setEnabled(False)
        group_layout.addWidget(self.target_combo)

        layout.addWidget(group_box)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok |
                                   QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self._accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

        self.rb_move.toggled.connect(lambda checked: self.target_combo.setEnabled(checked))

    def _populate_accounts(self):
        accounts = self.account_repo.get_all()
        for acc in accounts:
            if acc.id == self.exclude_id or acc.status == "GRP":
                continue
            self.target_combo.addItem(acc.name, acc.id)

    def _accept(self):
        checked_id = self.btn_group.checkedId()
        if checked_id == 0:
            self._action = self.HIDE
        elif checked_id == 1:
            self._action = self.MOVE
            self._target_account_id = self.target_combo.currentData()
        elif checked_id == 2:
            self._action = self.DELETE_SPLITS
        elif checked_id == 3:
            self._action = self.DELETE_TRANS
        self.accept()

    @property
    def action(self) -> str:
        return self._action

    @property
    def target_account_id(self) -> int | None:
        return self._target_account_id
