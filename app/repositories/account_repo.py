import sqlite3

from app.database.queries import accounts as Q
from app.models.account import Account


def _row_to_account(row) -> Account:
    return Account(
        id=row["ID"],
        parent=row["Parent"],
        name=row["Name"],
        code=row["Code"],
        description=row["Description"],
        external_id=row["ExternalID"],
        is_hidden=bool(row["IsHidden"]),
    )


class AccountRepo:
    def __init__(self, conn: sqlite3.Connection, settings=None):
        self.conn = conn
        self.settings = settings

    def get_all(self) -> list[Account]:
        rows = self.conn.execute(Q.GET_ALL).fetchall()
        return [_row_to_account(r) for r in rows]

    def get_by_id(self, account_id: int) -> Account | None:
        row = self.conn.execute(Q.GET_BY_ID, (account_id,)).fetchone()
        return _row_to_account(row) if row else None

    def get_children(self, account_id: int) -> list[Account]:
        rows = self.conn.execute(Q.GET_CHILDREN, (account_id,)).fetchall()
        return [_row_to_account(r) for r in rows]

    def get_parent_id(self, account_id: int) -> int | None:
        acc = self.get_by_id(account_id)
        return acc.parent if acc else None

    def insert(self, parent: int | None, name: str, code: str | None,
               description: str | None, external_id: str | None, is_hidden: bool = False) -> int:
        cur = self.conn.execute(Q.INSERT, (parent, name, code, description, external_id, int(is_hidden)))
        self.conn.commit()
        return cur.lastrowid

    def update(self, account_id: int, parent: int | None, name: str, code: str | None,
               description: str | None, external_id: str | None, is_hidden: bool) -> None:
        self.conn.execute(Q.UPDATE, (parent, name, code, description, external_id, int(is_hidden), account_id))
        self.conn.commit()

    def update_parent(self, account_id: int, new_parent: int | None) -> None:
        self.conn.execute(Q.UPDATE_PARENT, (new_parent, account_id))
        self.conn.commit()

    def update_hidden(self, account_id: int, is_hidden: bool) -> None:
        self.conn.execute(Q.UPDATE_HIDDEN, (int(is_hidden), account_id))
        self.conn.commit()

    def delete(self, account_id: int) -> None:
        self.conn.execute(Q.DELETE, (account_id,))
        self.conn.commit()

    def get_balance(self, account_id: int) -> dict[int, int]:
        """Returns {currency_id: total_quants}"""
        rows = self.conn.execute(Q.GET_BALANCE, (account_id,)).fetchall()
        return {r["Currency"]: r["TotalQuants"] for r in rows}

    def move_splits_to_account(self, from_account_id: int, to_account_id: int) -> None:
        self.conn.execute(Q.MOVE_SPLITS_TO_ACCOUNT, (to_account_id, from_account_id))
        self.conn.commit()

    def get_transaction_ids_for_account(self, account_id: int) -> list[int]:
        rows = self.conn.execute(Q.GET_TRANS_IDS_FOR_ACCOUNT, (account_id,)).fetchall()
        return [r[0] for r in rows]

    def get_all_descendants(self, account_id: int) -> list[int]:
        """Get all descendants of an account (recursive)."""
        result = []
        children = self.get_children(account_id)
        for child in children:
            result.append(child.id)
            result.extend(self.get_all_descendants(child.id))
        return result

    def get_account_path(self, account_id: int) -> str:
        """Get full path of account (e.g., 'Assets / Current / Bank Account')."""
        if account_id is None:
            return ""
        acc = self.get_by_id(account_id)
        if acc is None:
            return str(account_id)

        separator = self.settings.account_path_sep if self.settings else " / "
        parts = []
        current_id = account_id
        while current_id is not None:
            acc = self.get_by_id(current_id)
            if acc is None:
                break
            parts.append(acc.name)
            current_id = acc.parent
        return separator.join(reversed(parts))
