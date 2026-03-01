"""Amount conversion utilities."""


def float_to_quants(value: float, denominator: int) -> int:
    """Convert float value to integer quants (rounds to nearest)."""
    return round(value * denominator)
