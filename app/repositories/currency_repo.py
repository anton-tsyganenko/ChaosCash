import sqlite3
from app.models.currency import Currency
from app.database.queries import currencies as Q


def _row_to_currency(row) -> Currency:
    return Currency(
        id=row["ID"],
        code=row["Code"],
        type=row["Type"],
        name=row["Name"],
        denominator=row["Denominator"],
    )


class CurrencyRepo:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def get_all(self) -> list[Currency]:
        rows = self.conn.execute(Q.GET_ALL).fetchall()
        return [_row_to_currency(r) for r in rows]

    def get_by_id(self, currency_id: int) -> Currency | None:
        row = self.conn.execute(Q.GET_BY_ID, (currency_id,)).fetchone()
        return _row_to_currency(row) if row else None

    def insert(self, code: str, type_: str, name: str | None, denominator: int) -> int:
        cur = self.conn.execute(Q.INSERT, (code, type_, name, denominator))
        self.conn.commit()
        return cur.lastrowid

    def update(self, currency_id: int, code: str, type_: str, name: str | None, denominator: int) -> None:
        self.conn.execute(Q.UPDATE, (code, type_, name, denominator, currency_id))
        self.conn.commit()

    def delete(self, currency_id: int) -> None:
        self.conn.execute(Q.DELETE, (currency_id,))
        self.conn.commit()

    def is_used(self, currency_id: int) -> bool:
        row = self.conn.execute(Q.IS_USED, (currency_id,)).fetchone()
        return row[0] > 0 if row else False
