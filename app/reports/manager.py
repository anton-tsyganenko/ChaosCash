"""Report registration and execution orchestration."""
from __future__ import annotations

from collections.abc import Sequence

from PyQt6.QtGui import QDesktopServices
from PyQt6.QtCore import QUrl

from app.reports.contracts import ReportContext, ReportDefinition, ReportResult
from app.reports.dialogs.parameter_dialog import ReportParameterDialog
from app.reports.plugins.account_balances_csv import AccountBalancesCsvReport
from app.reports.runner import ReportRunner


class ReportManager:
    def __init__(self, context: ReportContext, parent=None):
        self._context = context
        self._parent = parent
        self._runner = ReportRunner(context)
        self._reports: list[ReportDefinition] = [
            AccountBalancesCsvReport(),
        ]

    def list_definitions(self) -> Sequence[ReportDefinition]:
        return list(self._reports)

    def run_report_interactive(self, report_id: str) -> ReportResult | None:
        report = next((r for r in self._reports if r.id == report_id), None)
        if report is None:
            return None

        dialog = ReportParameterDialog(
            title=report.title,
            schema=report.parameter_schema(),
            account_repo=self._context.account_repo,
            currency_repo=self._context.currency_repo,
            transaction_repo=self._context.transaction_repo,
            split_repo=self._context.split_repo,
            balance_service=self._context.balance_service,
            amount_formatter=self._context.amount_formatter,
            settings=self._context.settings,
            integrity_service=self._context.integrity_service,
            parent=self._parent,
        )
        if dialog.exec() != dialog.DialogCode.Accepted:
            return None

        params = dialog.get_params()
        result = self._runner.run(report, params)
        if params.get("__open_after_generation", True):
            QDesktopServices.openUrl(QUrl.fromLocalFile(str(result.output_file_path)))
        return result
