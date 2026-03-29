"""Core report contracts and context objects."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Protocol

from app.repositories.account_repo import AccountRepo
from app.repositories.currency_repo import CurrencyRepo
from app.repositories.price_repo import PriceRepo
from app.repositories.split_repo import SplitRepo
from app.repositories.transaction_repo import TransactionRepo
from app.reports.schemas import ReportParameterSchema, ReportParams
from app.services.amount_formatter import AmountFormatter
from app.services.balance_service import BalanceService
from app.services.integrity_service import IntegrityService
from app.services.price_service import PriceService
from app.settings.app_settings import AppSettings


@dataclass(frozen=True)
class OutputWriterSpec:
    extension: str
    mime_type: str


@dataclass(frozen=True)
class ReportResult:
    output_file_path: Path
    mime_type: str
    warnings: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class ReportContext:
    account_repo: AccountRepo
    transaction_repo: TransactionRepo
    split_repo: SplitRepo
    currency_repo: CurrencyRepo
    price_repo: PriceRepo
    balance_service: BalanceService
    integrity_service: IntegrityService
    price_service: PriceService
    amount_formatter: AmountFormatter
    settings: AppSettings


class ReportDefinition(Protocol):
    id: str
    title: str

    def parameter_schema(self) -> ReportParameterSchema:
        ...

    def output_writer(self) -> OutputWriterSpec:
        ...

    def generate_to_file(self, params: ReportParams, context: ReportContext, output_path: Path) -> list[str]:
        """Generate report directly into output_path and return warnings list."""
        ...
