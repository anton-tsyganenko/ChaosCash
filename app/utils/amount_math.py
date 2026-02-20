"""Amount formatting and conversion utilities."""
import math


def quants_to_float(quants: int, denominator: int) -> float:
    """Convert integer quants to float value."""
    return quants / denominator


def float_to_quants(value: float, denominator: int) -> int:
    """Convert float value to integer quants (rounds to nearest)."""
    return round(value * denominator)


def format_amount(quants: int, denominator: int,
                  decimal_sep: str = ".", thousands_sep: str = "",
                  show_thousands: bool = True) -> str:
    """Format a quants amount as a human-readable string."""
    if denominator <= 0:
        denominator = 1
    decimal_places = max(0, math.ceil(math.log10(denominator))) if denominator > 1 else 0
    value = quants / denominator
    if show_thousands and thousands_sep:
        formatted = f"{value:,.{decimal_places}f}"
        # Replace default separators with user-specified ones
        formatted = formatted.replace(",", "\x00").replace(".", decimal_sep).replace("\x00", thousands_sep)
    else:
        formatted = f"{value:.{decimal_places}f}"
        if decimal_sep != ".":
            formatted = formatted.replace(".", decimal_sep)
    return formatted
