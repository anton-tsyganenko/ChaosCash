"""Declarative report parameter schemas."""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Literal


PeriodSplitKind = Literal[
    "none",
    "daily",
    "weekly",
    "monthly",
    "quarterly",
    "yearly",
    "custom_relative_delta",
]


@dataclass(frozen=True)
class RelativeDeltaSpec:
    years: int = 0
    months: int = 0
    weeks: int = 0
    days: int = 0


@dataclass(frozen=True)
class PeriodSplitStrategy:
    kind: PeriodSplitKind
    delta: RelativeDeltaSpec | None = None


@dataclass(frozen=True)
class PeriodRange:
    start: datetime
    end: datetime


@dataclass(frozen=True)
class PriceRules:
    sources: list[str] = field(default_factory=list)
    max_delta_before_days: int | None = None
    max_delta_after_days: int | None = None


@dataclass(frozen=True)
class ReportField:
    key: str
    label: str
    required: bool = True


@dataclass(frozen=True)
class AccountSetField(ReportField):
    pass


@dataclass(frozen=True)
class PeriodField(ReportField):
    default_split: PeriodSplitKind = "none"


@dataclass(frozen=True)
class PriceRulesField(ReportField):
    pass


@dataclass(frozen=True)
class CurrencyField(ReportField):
    allow_auto: bool = True


@dataclass(frozen=True)
class CustomField(ReportField):
    type_id: str = ""
    payload: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class ReportParameterSchema:
    fields: list[ReportField]


@dataclass(frozen=True)
class ReportParams:
    values: dict[str, Any]

    def get(self, key: str, default=None):
        return self.values.get(key, default)
