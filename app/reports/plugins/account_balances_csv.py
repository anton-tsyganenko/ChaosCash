"""Built-in report: current balances by account (CSV)."""
from __future__ import annotations

import csv
from datetime import datetime, timedelta, timezone
from pathlib import Path

from app.reports.contracts import OutputWriterSpec, ReportContext
from app.reports.schemas import (
    AccountSetField,
    CurrencyField,
    PriceRulesField,
    ReportParameterSchema,
    ReportParams,
)


class AccountBalancesCsvReport:
    id = "balances.converted.csv"
    title = "Account Balances in Report Currency (CSV)"

    def parameter_schema(self) -> ReportParameterSchema:
        return ReportParameterSchema(fields=[
            AccountSetField(key="accounts", label="Accounts"),
            CurrencyField(key="report_currency", label="Report currency", required=True, allow_auto=False),
            PriceRulesField(key="price_rules", label="Price rules", required=False),
        ])

    def output_writer(self) -> OutputWriterSpec:
        return OutputWriterSpec(extension=".csv", mime_type="text/csv")

    def generate_to_file(self, params: ReportParams, context: ReportContext, output_path: Path) -> list[str]:
        selected_ids = set(params.get("accounts", []))
        if not selected_ids:
            raise ValueError("No accounts selected")
        report_currency_id = params.get("report_currency")
        if report_currency_id is None:
            raise ValueError("Report currency is required")
        target_curr = context.currency_repo.get_by_id(report_currency_id)
        if target_curr is None:
            raise ValueError("Report currency not found")

        price_rules = params.get("price_rules")
        max_before = None
        max_after = None
        sources = None
        if price_rules is not None:
            max_before = (
                timedelta(days=price_rules.max_delta_before_days)
                if price_rules.max_delta_before_days is not None
                else None
            )
            max_after = (
                timedelta(days=price_rules.max_delta_after_days)
                if price_rules.max_delta_after_days is not None
                else None
            )
            sources = price_rules.sources or None

        warnings: list[str] = []
        rows: list[tuple[str, str]] = []
        now_utc = datetime.now(timezone.utc)

        for acc in context.account_repo.get_all():
            if acc.id not in selected_ids:
                continue
            balance = context.balance_service.get_balance(acc.id, include_children=True)
            account_path = context.account_repo.get_account_path(acc.id)
            total_quants = 0
            for currency_id, quants in sorted(balance.items()):
                if currency_id == report_currency_id:
                    total_quants += quants
                    continue

                source_curr = context.currency_repo.get_by_id(currency_id)
                if source_curr is None:
                    warnings.append(f"Unknown currency {currency_id} for account '{account_path}'")
                    continue
                source_amount = quants / source_curr.denominator
                price_result = context.price_service.get_price(
                    of_curr=currency_id,
                    in_curr=report_currency_id,
                    date=now_utc,
                    max_delta_before=max_before,
                    max_delta_after=max_after,
                    sources=sources,
                )
                if price_result is None:
                    warnings.append(
                        f"No price from {source_curr.code} to {target_curr.code} for account '{account_path}'"
                    )
                    continue
                converted_amount = source_amount * price_result.value
                total_quants += round(converted_amount * target_curr.denominator)
            amount = context.amount_formatter.format_amount(total_quants, report_currency_id)
            rows.append((account_path, amount))

        with output_path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Account", f"Balance ({target_curr.code})"])
            writer.writerows(rows)

        return warnings
