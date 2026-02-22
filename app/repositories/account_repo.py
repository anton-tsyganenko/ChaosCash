import sqlite3
from app.models.account import Account
from app.database.queries import accounts as Q


def _row_to_account(row) -> Account:
    return Account(
        id=row["ID"],
        parent=row["Parent"],
        name=row["Name"],
        code=row["Code"],
        description=row["Description"],
        external_id=row["ExternalID"],
        status=row["Status"],
    )


class AccountRepo:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def get_all(self) -> list[Account]:
        rows = self.conn.execute(Q.GET_ALL).fetchall()
        return [_row_to_account(r) for r in rows]

    def get_by_id(self, account_id: int) -> Account | None:
        row = self.conn.execute(Q.GET_BY_ID, (account_id,)).fetchone()
        return _row_to_account(row) if row else None

    def get_children(self, account_id: int) -> list[Account]:
        rows = self.conn.execute(Q.GET_CHILDREN, (account_id,)).fetchall()
        return [_row_to_account(r) for r in rows]

    def get_root_accounts(self) -> list[Account]:
        rows = self.conn.execute(Q.GET_ROOT).fetchall()
        return [_row_to_account(r) for r in rows]

    def get_parent_id(self, account_id: int) -> int | None:
        acc = self.get_by_id(account_id)
        return acc.parent if acc else None

    def insert(self, parent: int | None, name: str, code: str | None,
               description: str | None, external_id: str | None, status: str = "ACT") -> int:
        cur = self.conn.execute(Q.INSERT, (parent, name, code, description, external_id, status))
        self.conn.commit()
        return cur.lastrowid

    def update(self, account_id: int, parent: int | None, name: str, code: str | None,
               description: str | None, external_id: str | None, status: str) -> None:
        self.conn.execute(Q.UPDATE, (parent, name, code, description, external_id, status, account_id))
        self.conn.commit()

    def update_parent(self, account_id: int, new_parent: int | None) -> None:
        self.conn.execute(Q.UPDATE_PARENT, (new_parent, account_id))
        self.conn.commit()

    def update_status(self, account_id: int, status: str) -> None:
        self.conn.execute(Q.UPDATE_STATUS, (status, account_id))
        self.conn.commit()

    def delete(self, account_id: int) -> None:
        self.conn.execute(Q.DELETE, (account_id,))
        self.conn.commit()

    def get_balance(self, account_id: int) -> dict[int, tuple[int, int]]:
        """Returns {currency_id: (total_quants, denominator)}"""
        rows = self.conn.execute(Q.GET_BALANCE, (account_id,)).fetchall()
        return {r["CurrencyID"]: (r["TotalQuants"], r["Denominator"]) for r in rows}

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

    def get_account_path(self, account_id: int, separator: str = " / ") -> str:
        """Get full path of account (e.g., 'Assets / Current / Bank Account')."""
        if account_id is None:
            return ""
        acc = self.get_by_id(account_id)
        if acc is None:
            return str(account_id)
        parts = []
        current_id = account_id
        while current_id is not None:
            acc = self.get_by_id(current_id)
            if acc is None:
                break
            parts.append(acc.name)
            current_id = acc.parent
        return separator.join(reversed(parts))
