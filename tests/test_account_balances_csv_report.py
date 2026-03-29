from datetime import timedelta
from pathlib import Path
from types import SimpleNamespace

from app.reports.plugins.account_balances_csv import AccountBalancesCsvReport
from app.reports.schemas import PriceRules, ReportParams


class FakeAccountRepo:
    def get_all(self):
        return [SimpleNamespace(id=1)]

    def get_account_path(self, account_id):
        return "Assets:Cash"


class FakeBalanceService:
    def get_balance(self, account_id, include_children=True):
        assert account_id == 1
        assert include_children is True
        return {1: 10000, 2: 2000}  # 100.00 USD + 20.00 EUR


class FakeCurrencyRepo:
    def __init__(self):
        self._curr = {
            1: SimpleNamespace(id=1, code="USD", denominator=100),
            2: SimpleNamespace(id=2, code="EUR", denominator=100),
        }

    def get_by_id(self, currency_id):
        return self._curr.get(currency_id)


class FakeFormatter:
    def format_amount(self, quants, currency_id):
        assert currency_id == 1
        return f"{quants / 100:.2f}"


class FakePriceService:
    def get_price(self, of_curr, in_curr, **kwargs):
        if of_curr == 2 and in_curr == 1:
            return SimpleNamespace(value=1.5)
        return None


class FakeContext:
    account_repo = FakeAccountRepo()
    balance_service = FakeBalanceService()
    currency_repo = FakeCurrencyRepo()
    amount_formatter = FakeFormatter()
    price_service = FakePriceService()


def test_account_balances_csv_report_converts_to_report_currency(tmp_path: Path):
    report = AccountBalancesCsvReport()
    output = tmp_path / "report.csv"

    params = ReportParams(values={
        "accounts": [1],
        "report_currency": 1,
        "price_rules": PriceRules(
            sources=["manual"],
            max_delta_before=timedelta(days=30),
            max_delta_after=timedelta(hours=12),
        ),
    })

    warnings = report.generate_to_file(params=params, context=FakeContext(), output_path=output)

    assert warnings == []
    lines = output.read_text(encoding="utf-8").strip().splitlines()
    assert lines[0] == "Account,Balance (USD)"
    assert lines[1] == "Assets:Cash,130.00"
