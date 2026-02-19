"""Currency editor dialog."""
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QPushButton, QMessageBox, QDialogButtonBox, QHeaderView, QSpinBox,
    QLineEdit, QComboBox
)
from PyQt6.QtCore import Qt
from app.i18n import tr
from app.repositories.currency_repo import CurrencyRepo

COL_CODE = 0
COL_TYPE = 1
COL_NAME = 2
COL_DENOM = 3
NUM_COLS = 4

CURRENCY_TYPES = ["CURR", "STOCK", "BOND", "CRYPTO"]


class CurrencyEditorDialog(QDialog):
    def __init__(self, currency_repo: CurrencyRepo, parent=None):
        super().__init__(parent)
        self.currency_repo = currency_repo
        self.setWindowTitle(tr("Currency Editor"))
        self.setModal(True)
        self.resize(600, 400)
        self._currency_ids: list[int | None] = []
        self._build_ui()
        self._load()

    def _build_ui(self):
        layout = QVBoxLayout(self)

        self.table = QTableWidget(0, NUM_COLS)
        self.table.setHorizontalHeaderLabels([
            tr("Code"), tr("Type"), tr("Name"), tr("Denominator")
        ])
        self.table.horizontalHeader().setSectionResizeMode(COL_NAME, QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.table)

        btn_layout = QHBoxLayout()
        self.btn_add = QPushButton(tr("Add"))
        self.btn_delete = QPushButton(tr("Delete"))
        self.btn_add.clicked.connect(self._add_row)
        self.btn_delete.clicked.connect(self._delete_row)
        btn_layout.addWidget(self.btn_add)
        btn_layout.addWidget(self.btn_delete)
        btn_layout.addStretch()
        layout.addLayout(btn_layout)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self._save)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def _load(self):
        currencies = self.currency_repo.get_all()
        self._currency_ids = []
        self.table.setRowCount(0)
        for cur in currencies:
            self._add_table_row(cur.id, cur.code, cur.type, cur.name or "", cur.denominator)

    def _add_table_row(self, cur_id: int | None, code: str, type_: str, name: str, denom: int):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self._currency_ids.append(cur_id)
        self.table.setItem(row, COL_CODE, QTableWidgetItem(code))
        type_combo = QComboBox()
        type_combo.addItems(CURRENCY_TYPES)
        idx = type_combo.findText(type_)
        if idx >= 0:
            type_combo.setCurrentIndex(idx)
        self.table.setCellWidget(row, COL_TYPE, type_combo)
        self.table.setItem(row, COL_NAME, QTableWidgetItem(name))
        denom_spin = QSpinBox()
        denom_spin.setMinimum(1)
        denom_spin.setMaximum(10_000_000)
        denom_spin.setValue(denom)
        self.table.setCellWidget(row, COL_DENOM, denom_spin)

    def _add_row(self):
        self._add_table_row(None, "", "CURR", "", 100)

    def _delete_row(self):
        row = self.table.currentRow()
        if row < 0:
            return
        cur_id = self._currency_ids[row] if row < len(self._currency_ids) else None
        if cur_id is not None and self.currency_repo.is_used(cur_id):
            QMessageBox.warning(self, tr("Cannot Delete"),
                                tr("This currency is used in existing splits and cannot be deleted."))
            return
        if cur_id is not None:
            self.currency_repo.delete(cur_id)
        self.table.removeRow(row)
        self._currency_ids.pop(row)

    def _save(self):
        for row in range(self.table.rowCount()):
            code_item = self.table.item(row, COL_CODE)
            code = code_item.text().strip() if code_item else ""
            if not code:
                continue
            type_widget = self.table.cellWidget(row, COL_TYPE)
            type_ = type_widget.currentText() if type_widget else "CURR"
            name_item = self.table.item(row, COL_NAME)
            name = name_item.text().strip() if name_item else ""
            denom_widget = self.table.cellWidget(row, COL_DENOM)
            denom = denom_widget.value() if denom_widget else 100

            cur_id = self._currency_ids[row] if row < len(self._currency_ids) else None
            if cur_id is None:
                self.currency_repo.insert(code, type_, name or None, denom)
            else:
                self.currency_repo.update(cur_id, code, type_, name or None, denom)
        self.accept()
