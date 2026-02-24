"""Amount formatting service for UI models."""
import math

from app.repositories import CurrencyRepo
from app.settings import AppSettings


class AmountFormatter:
    """Formats amounts with proper decimal places and separators."""

    def __init__(self, settings: AppSettings, currencies_repo: CurrencyRepo):
        self.settings = settings
        self.currencies = currencies_repo

    def format_amount(self, quants: int, currency_id: int) -> str:
        """Format amount in specific currency (without currency code).

        Args:
            quants: Amount in quants (smallest units)
            currency_id: Currency ID

        Returns:
            Formatted amount string (e.g., "1000.50")
        """
        cur = self.currencies.get_by_id(currency_id)
        denominator = cur.denominator
        decimal_places = math.ceil(math.log10(denominator))
        value = quants / denominator

        formatted = f"{value:,.{decimal_places}f}".translate(
            str.maketrans({",": self.settings.thousands_sep,
                          ".": self.settings.decimal_sep})
        )
        return formatted

    def format_with_currency(self, quants: int, currency_id: int) -> str:
        """Format amount with currency code (e.g., "1000.50 USD").

        Args:
            quants: Amount in quants (smallest units)
            currency_id: Currency ID

        Returns:
            Formatted amount with currency code (e.g., "1000.50 USD")
        """
        cur = self.currencies.get_by_id(currency_id)
        return f"{self.format_amount(quants, currency_id)} {cur.code}"
