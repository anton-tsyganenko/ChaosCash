from dataclasses import dataclass


@dataclass(frozen=True)
class Account:
    id: int
    parent: int | None
    name: str
    code: str | None
    description: str | None
    external_id: str | None
    status: str  # ACT, HID, GRP
