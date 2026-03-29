from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Price:
    id: int
    of_curr: int
    value: float
    in_curr: int
    date: datetime
    source: str | None
