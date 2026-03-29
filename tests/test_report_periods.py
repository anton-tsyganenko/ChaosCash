from datetime import datetime, timezone

from app.reports.periods import split_period
from app.reports.schemas import PeriodRange, PeriodSplitStrategy, RelativeDeltaSpec


def test_split_period_monthly():
    period = PeriodRange(
        start=datetime(2026, 1, 1, tzinfo=timezone.utc),
        end=datetime(2026, 4, 1, tzinfo=timezone.utc),
    )
    parts = split_period(period, PeriodSplitStrategy(kind="monthly"))
    assert len(parts) == 3
    assert parts[0].start.month == 1
    assert parts[1].start.month == 2
    assert parts[2].start.month == 3


def test_split_period_custom_delta():
    period = PeriodRange(
        start=datetime(2026, 1, 1, tzinfo=timezone.utc),
        end=datetime(2026, 1, 10, tzinfo=timezone.utc),
    )
    parts = split_period(
        period,
        PeriodSplitStrategy(kind="custom_relative_delta", delta=RelativeDeltaSpec(days=3)),
    )
    assert len(parts) == 3
    assert parts[-1].end == period.end
