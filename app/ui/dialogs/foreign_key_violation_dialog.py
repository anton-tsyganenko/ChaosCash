"""Foreign key violation display dialog."""
from PyQt6.QtWidgets import (
    QDialog,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
)

from app.i18n import tr


class ForeignKeyViolationDialog(QDialog):
    """Dialog to display foreign key violations in a table."""

    def __init__(self, violations: list[dict], parent=None):
        super().__init__(parent)
        self.violations = violations
        self.setWindowTitle(tr("Database Integrity Warning"))
        self.setMinimumWidth(400)

        layout = QVBoxLayout(self)

        label = QLabel(tr("Foreign Key violations found:"))
        layout.addWidget(label)

        # Create table with columns
        table = QTableWidget(self)
        table.setColumnCount(4)
        table.setHorizontalHeaderLabels(
            [tr("Table"), tr("Row ID"), tr("Parent Table"), tr("FK ID")]
        )
        table.setRowCount(len(violations))

        # Populate table with violation data
        for row, violation in enumerate(violations):
            table.setItem(row, 0, QTableWidgetItem(str(violation["table"])))
            table.setItem(row, 1, QTableWidgetItem(str(violation["rowid"])))
            table.setItem(row, 2, QTableWidgetItem(str(violation["parent"])))
            table.setItem(row, 3, QTableWidgetItem(str(violation["fkid"])))

        # Resize columns to content
        table.resizeColumnsToContents()
        layout.addWidget(table)
