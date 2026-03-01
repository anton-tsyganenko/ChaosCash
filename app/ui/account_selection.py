"""Helpers for account selection drop-downs."""

from app.repositories.account_repo import AccountRepo
from app.utils.account_hierarchy import compute_hidden_account_ids


def get_selectable_account_items(
    account_repo: AccountRepo,
    settings,
    *,
    exclude_ids: set[int] | None = None,
) -> list[tuple[str, int]]:
    """Build selectable account list with common filtering rules."""
    all_accounts = account_repo.get_all()
    exclude_ids = exclude_ids or set()

    hidden_ids = compute_hidden_account_ids(all_accounts)
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
