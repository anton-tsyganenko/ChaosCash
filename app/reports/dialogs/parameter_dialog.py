"""Generic report parameter dialog built from schema fields."""
from __future__ import annotations

from datetime import timedelta, timezone

from PyQt6.QtCore import QDateTime, Qt
from PyQt6.QtWidgets import (
    QAbstractItemView,
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from app.i18n import tr
from app.repositories.account_repo import AccountRepo
from app.repositories.currency_repo import CurrencyRepo
from app.repositories.split_repo import SplitRepo
from app.repositories.transaction_repo import TransactionRepo
from app.reports.schemas import (
    AccountSetField,
    CurrencyField,
    PeriodField,
    PeriodRange,
    PeriodSplitStrategy,
    PriceRules,
    PriceRulesField,
    RelativeDeltaSpec,
    ReportField,
    ReportParameterSchema,
    ReportParams,
)
from app.services.amount_formatter import AmountFormatter
from app.services.balance_service import BalanceService
from app.settings.display_settings import DisplaySettings
from app.ui.item_models.account_tree_model import AccountTreeModel
from app.ui.widgets.account_tree_view import AccountTreeView
from app.ui.widgets.view_helpers import apply_account_tree_display_settings


class ReportParameterDialog(QDialog):
    def __init__(
        self,
        title: str,
        schema: ReportParameterSchema,
        account_repo: AccountRepo,
        currency_repo: CurrencyRepo,
        transaction_repo: TransactionRepo,
        split_repo: SplitRepo,
        balance_service: BalanceService,
        amount_formatter: AmountFormatter,
        settings,
        integrity_service,
        parent=None,
    ):
        super().__init__(parent)
        self.setWindowTitle(tr(title))
        self.setModal(True)
        self.setMinimumWidth(520)

        self._schema = schema
        self._account_repo = account_repo
        self._currency_repo = currency_repo
        self._transaction_repo = transaction_repo
        self._split_repo = split_repo
        self._balance_service = balance_service
        self._amount_formatter = amount_formatter
        self._settings = settings
        self._integrity_service = integrity_service
        self._widgets: dict[str, object] = {}

        layout = QVBoxLayout(self)
        form = QFormLayout()
        layout.addLayout(form)

        for field in schema.fields:
            widget = self._build_widget(field)
            if widget is None:
                continue
            form.addRow(field.label + ":", widget)

        self.open_after_generation = QCheckBox(tr("Open after generation"))
        self.open_after_generation.setChecked(True)
        form.addRow("", self.open_after_generation)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        buttons.accepted.connect(self._on_accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def _build_widget(self, field: ReportField) -> QWidget | None:
        if isinstance(field, AccountSetField):
            tree = _AccountSelectionTree(
                account_repo=self._account_repo,
                transaction_repo=self._transaction_repo,
                split_repo=self._split_repo,
                balance_service=self._balance_service,
                currency_repo=self._currency_repo,
                amount_formatter=self._amount_formatter,
                settings=self._settings,
                integrity_service=self._integrity_service,
            )
            tree.setMinimumHeight(180)
            self._widgets[field.key] = tree
            return tree

        if isinstance(field, PeriodField):
            container = QWidget()
            lay = QHBoxLayout(container)
            lay.setContentsMargins(0, 0, 0, 0)

            start_edit = QDateTimeEdit(QDateTime.currentDateTimeUtc().addDays(-30))
            end_edit = QDateTimeEdit(QDateTime.currentDateTimeUtc())
            for edit in (start_edit, end_edit):
                edit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
                edit.setCalendarPopup(True)
                edit.setTimeSpec(Qt.TimeSpec.UTC)

            split_combo = QComboBox()
            split_combo.addItem(tr("No split"), "none")
            split_combo.addItem(tr("Daily"), "daily")
            split_combo.addItem(tr("Weekly"), "weekly")
            split_combo.addItem(tr("Monthly"), "monthly")
            split_combo.addItem(tr("Quarterly"), "quarterly")
            split_combo.addItem(tr("Yearly"), "yearly")
            split_combo.addItem(tr("Custom step"), "custom_relative_delta")
            split_combo.setCurrentIndex(max(split_combo.findData(field.default_split), 0))

            delta_days = QSpinBox()
            delta_days.setRange(1, 3650)
            delta_days.setValue(30)
            delta_days.setEnabled(field.default_split == "custom_relative_delta")
            split_combo.currentIndexChanged.connect(
                lambda *_: delta_days.setEnabled(split_combo.currentData() == "custom_relative_delta")
            )

            lay.addWidget(QLabel(tr("From")))
            lay.addWidget(start_edit)
            lay.addWidget(QLabel(tr("To")))
            lay.addWidget(end_edit)
            lay.addWidget(QLabel(tr("Split")))
            lay.addWidget(split_combo)
            lay.addWidget(QLabel(tr("Days")))
            lay.addWidget(delta_days)
            self._widgets[field.key] = (start_edit, end_edit, split_combo, delta_days)
            return container

        if isinstance(field, PriceRulesField):
            container = QWidget()
            lay = QHBoxLayout(container)
            lay.setContentsMargins(0, 0, 0, 0)
            sources = QLineEdit()
            sources.setPlaceholderText(tr("source1,source2"))
            before = QSpinBox()
            before.setRange(0, 3650)
            before.setValue(15)
            before_unit = QComboBox()
            before_unit.addItem(tr("minutes"), "minutes")
            before_unit.addItem(tr("hours"), "hours")
            before_unit.addItem(tr("days"), "days")
            before_unit.addItem(tr("weeks"), "weeks")
            before_unit.setCurrentIndex(before_unit.findData("days"))
            after = QSpinBox()
            after.setRange(0, 3650)
            after.setValue(12)
            after_unit = QComboBox()
            after_unit.addItem(tr("minutes"), "minutes")
            after_unit.addItem(tr("hours"), "hours")
            after_unit.addItem(tr("days"), "days")
            after_unit.addItem(tr("weeks"), "weeks")
            after_unit.setCurrentIndex(after_unit.findData("hours"))
            lay.addWidget(QLabel(tr("Sources")))
            lay.addWidget(sources)
            lay.addWidget(QLabel(tr("Before")))
            lay.addWidget(before)
            lay.addWidget(before_unit)
            lay.addWidget(QLabel(tr("After")))
            lay.addWidget(after)
            lay.addWidget(after_unit)
            self._widgets[field.key] = (sources, before, before_unit, after, after_unit)
            return container

        if isinstance(field, CurrencyField):
            combo = QComboBox()
            if field.allow_auto:
                combo.addItem(tr("Auto"), None)
            for curr in self._currency_repo.get_all():
                combo.addItem(curr.code, curr.id)
            self._widgets[field.key] = combo
            return combo

        fallback = QLineEdit()
        self._widgets[field.key] = fallback
        return fallback

    def _on_accept(self):
        try:
            _ = self.get_params()
        except ValueError as exc:
            QMessageBox.warning(self, tr("Invalid Parameters"), str(exc))
            return
        self.accept()

    def get_params(self) -> ReportParams:
        values: dict[str, object] = {}
        for field in self._schema.fields:
            widget = self._widgets.get(field.key)
            if isinstance(field, AccountSetField):
                assert isinstance(widget, _AccountSelectionTree)
                account_ids = widget.get_selected_account_ids()
                if field.required and not account_ids:
                    raise ValueError(tr("Please select at least one account."))
                values[field.key] = account_ids
            elif isinstance(field, PeriodField):
                assert isinstance(widget, tuple)
                start_edit, end_edit, split_combo, delta_days = widget
                start_dt = start_edit.dateTime().toPyDateTime().replace(tzinfo=timezone.utc)
                end_dt = end_edit.dateTime().toPyDateTime().replace(tzinfo=timezone.utc)
                if start_dt > end_dt:
                    raise ValueError(tr("Start date must be before end date."))
                split_kind = split_combo.currentData()
                delta = RelativeDeltaSpec(days=delta_days.value()) if split_kind == "custom_relative_delta" else None
                values[field.key] = {
                    "period": PeriodRange(start=start_dt, end=end_dt),
                    "split": PeriodSplitStrategy(kind=split_kind, delta=delta),
                }
            elif isinstance(field, PriceRulesField):
                assert isinstance(widget, tuple)
                src, before, before_unit, after, after_unit = widget
                sources = [x.strip() for x in src.text().split(",") if x.strip()]
                values[field.key] = PriceRules(
                    sources=sources,
                    max_delta_before=self._build_timedelta(before.value(), before_unit.currentData()),
                    max_delta_after=self._build_timedelta(after.value(), after_unit.currentData()),
                )
            elif isinstance(field, CurrencyField):
                assert isinstance(widget, QComboBox)
                values[field.key] = widget.currentData()
            elif isinstance(widget, QLineEdit):
                text_value = widget.text().strip()
                if field.required and not text_value:
                    raise ValueError(tr("Required parameter is empty: ") + field.label)
                values[field.key] = text_value
        values["__open_after_generation"] = self.open_after_generation.isChecked()
        return ReportParams(values=values)

    @staticmethod
    def _build_timedelta(value: int, unit: str) -> timedelta | None:
        if value <= 0:
            return None
        if unit == "minutes":
            return timedelta(minutes=value)
        if unit == "hours":
            return timedelta(hours=value)
        if unit == "weeks":
            return timedelta(weeks=value)
        return timedelta(days=value)


class _AccountSelectionTree(QWidget):
    """Wrapper around app AccountTreeView for report account selection."""

    def __init__(
        self,
        account_repo: AccountRepo,
        transaction_repo: TransactionRepo,
        split_repo: SplitRepo,
        balance_service: BalanceService,
        currency_repo: CurrencyRepo,
        amount_formatter: AmountFormatter,
        settings,
        integrity_service,
    ):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        self.tree = AccountTreeView(
            account_repo=account_repo,
            trans_repo=transaction_repo,
            split_repo=split_repo,
            balance_service=balance_service,
            settings=settings,
            parent=self,
        )
        self.model = AccountTreeModel(
            account_repo=account_repo,
            balance_service=balance_service,
            currency_repo=currency_repo,
            settings=settings,
            formatter=amount_formatter,
            integrity_service=integrity_service,
            parent=self.tree,
        )
        self.tree.setModel(self.model)
        self.tree.expandAll()
        self.tree.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tree.setDragEnabled(False)
        self.tree.setAcceptDrops(False)
        self.tree.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.tree.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        layout.addWidget(self.tree)
        self._apply_display_settings()

    def _apply_display_settings(self):
        apply_account_tree_display_settings(self.tree, self.tree.header(), DisplaySettings("accounts"))

    def get_selected_account_ids(self) -> list[int]:
        selected_ids: set[int] = set()
        for index in self.tree.selectedIndexes():
            if index.column() != 0:
                continue
            node = self.model.get_node(index)
            if node and node.account and not node.is_virtual:
                selected_ids.add(node.account.id)
        return sorted(selected_ids)
