"""Utilities for working with account hierarchies."""

from app.models.account import Account


def compute_hidden_account_ids(accounts: list[Account]) -> set[int]:
    """Compute IDs of all hidden accounts including their descendants."""
    children: dict[int, list[int]] = {}
    for acc in accounts:
        if acc.parent is not None:
            children.setdefault(acc.parent, []).append(acc.id)

    hidden: set[int] = {acc.id for acc in accounts if acc.is_hidden}

    def mark_hidden_descendants(account_id: int) -> None:
        for child_id in children.get(account_id, []):
            if child_id in hidden:
                mark_hidden_descendants(child_id)
                continue
            hidden.add(child_id)
            mark_hidden_descendants(child_id)

    for hidden_id in list(hidden):
        mark_hidden_descendants(hidden_id)
    return hidden
