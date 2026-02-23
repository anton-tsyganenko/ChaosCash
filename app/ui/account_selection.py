"""Helpers for account selection drop-downs."""

from app.models.account import Account
from app.repositories.account_repo import AccountRepo


def compute_hidden_accounts(accounts: list[Account]) -> set[int]:
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


def get_selectable_account_items(
    account_repo: AccountRepo,
    settings,
    *,
    exclude_ids: set[int] | None = None,
) -> list[tuple[str, int]]:
    """Build selectable account list with common filtering rules."""
    all_accounts = account_repo.get_all()
    exclude_ids = exclude_ids or set()

    hidden_ids = compute_hidden_accounts(all_accounts)
    children_by_parent: dict[int, list[int]] = {}
    for acc in all_accounts:
        if acc.parent is not None:
            children_by_parent.setdefault(acc.parent, []).append(acc.id)

    allow_grouping = settings.allow_grouping_accounts_for_splits
    show_hidden = settings.show_hidden_accounts

    items: list[tuple[str, int]] = []
    for acc in all_accounts:
        if acc.id in exclude_ids:
            continue
        if acc.id in hidden_ids and not show_hidden:
            continue
        has_children = bool(children_by_parent.get(acc.id))
        if has_children and not allow_grouping:
            continue
        items.append((account_repo.get_account_path(acc.id), acc.id))

    items.sort(key=lambda x: x[0].lower())
    return items
