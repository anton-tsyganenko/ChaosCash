"""Amount formatting and conversion utilities."""
import math


def quants_to_float(quants: int, denominator: int) -> float:
    """Convert integer quants to float value."""
    return quants / denominator


def float_to_quants(value: float, denominator: int) -> int:
    """Convert float value to integer quants (rounds to nearest)."""
    return round(value * denominator)


def format_amount(quants: int, denominator: int,
                  decimal_sep: str = ".", thousands_sep: str = "") -> str:
    """Format a quants amount as a human-readable string."""
    if denominator <= 0:
        denominator = 1
    decimal_places = math.ceil(math.log10(denominator))
    value = quants / denominator

    formatted = f"{value:,.{decimal_places}f}".translate(
        str.maketrans({",": thousands_sep, ".": decimal_sep})
    )

    return formatted
