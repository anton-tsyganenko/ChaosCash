"""Utilities for date and time formatting."""


def qt_format_to_strftime(qt_format: str) -> str:
    """Convert Qt date format (yyyy-MM-dd) to strftime format (%Y-%m-%d)."""
    result = qt_format
    result = result.replace("yyyy", "%Y").replace("MM", "%m").replace("dd", "%d")
    result = result.replace("HH", "%H").replace("mm", "%M").replace("ss", "%S")
    return result
