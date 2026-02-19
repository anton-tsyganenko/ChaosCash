from dataclasses import dataclass


@dataclass(frozen=True)
class Transaction:
    id: int
    date: str  # UTC ISO string 'YYYY-MM-DD HH:MM:SS'
    description: str | None
