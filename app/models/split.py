from dataclasses import dataclass


@dataclass(frozen=True)
class Split:
    id: int
    trans: int
    account: int
    currency: int
    description: str | None
    external_id: str | None
    amount: int        # quants
    amount_fixed: bool
