"""Period splitting helpers for reports."""
from __future__ import annotations

import calendar
from datetime import datetime, timedelta

from app.reports.schemas import PeriodRange, PeriodSplitStrategy


def split_period(period: PeriodRange, strategy: PeriodSplitStrategy) -> list[PeriodRange]:
    if strategy.kind == "none":
        return [period]

    ranges: list[PeriodRange] = []
    cursor = period.start
    while cursor < period.end:
        nxt = _step(cursor, strategy)
        if nxt <= cursor:
            break
        if nxt > period.end:
            nxt = period.end
        ranges.append(PeriodRange(start=cursor, end=nxt))
        cursor = nxt
    return ranges or [period]


def _step(current: datetime, strategy: PeriodSplitStrategy) -> datetime:
    kind = strategy.kind
    if kind == "daily":
        return current + timedelta(days=1)
    if kind == "weekly":
        return current + timedelta(weeks=1)
    if kind == "monthly":
        return _add_months(current, 1)
    if kind == "quarterly":
        return _add_months(current, 3)
    if kind == "yearly":
        return _add_months(current, 12)
    if kind == "custom_relative_delta" and strategy.delta is not None:
        result = _add_months(current, strategy.delta.months + strategy.delta.years * 12)
        return result + timedelta(weeks=strategy.delta.weeks, days=strategy.delta.days)
    return current


def _add_months(value: datetime, months: int) -> datetime:
    total = (value.year * 12 + (value.month - 1)) + months
    year = total // 12
    month = total % 12 + 1
    day = min(value.day, calendar.monthrange(year, month)[1])
    return value.replace(year=year, month=month, day=day)
