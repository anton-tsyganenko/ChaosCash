from dataclasses import dataclass


@dataclass(frozen=True)
class Currency:
    id: int
    code: str
    type: str
    name: str | None
    denominator: int
