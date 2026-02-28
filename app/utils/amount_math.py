"""Amount conversion utilities."""


def quants_to_float(quants: int, denominator: int) -> float:
    """Convert integer quants to float value."""
    return quants / denominator


def float_to_quants(value: float, denominator: int) -> int:
    """Convert float value to integer quants (rounds to nearest)."""
    return round(value * denominator)
