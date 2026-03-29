import sqlite3
from datetime import datetime, timedelta, timezone

from app.database.queries import prices as Q
from app.models.price import Price



def _to_storage_datetime(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat(sep=" ", timespec="seconds")



def _from_storage_datetime(value: str) -> datetime:
    return datetime.fromisoformat(value).replace(tzinfo=timezone.utc)



def _row_to_price(row) -> Price:
    return Price(
        id=row["ID"],
        of_curr=row["OfCurr"],
        value=row["Value"],
        in_curr=row["InCurr"],
        date=_from_storage_datetime(row["Date"]),
        source=row["Source"],
    )


class PriceRepo:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def insert(
        self,
        of_curr: int,
        value: float,
        in_curr: int,
        date: datetime,
        source: str | None = None,
    ) -> int:
        cur = self.conn.execute(Q.INSERT, (of_curr, value, in_curr, _to_storage_datetime(date), source))
        self.conn.commit()
        return cur.lastrowid

    def get_candidates(
        self,
        target_date: datetime,
        max_delta_before: timedelta | None = None,
        max_delta_after: timedelta | None = None,
        sources: list[str] | None = None,
    ) -> list[Price]:
        sql = Q.GET_CANDIDATES_BASE
        params: list[str] = []

        if max_delta_before is not None:
            sql += " AND Date >= ?"
            params.append(_to_storage_datetime(target_date - max_delta_before))

        if max_delta_after is not None:
            sql += " AND Date <= ?"
            params.append(_to_storage_datetime(target_date + max_delta_after))

        if sources:
            placeholders = ",".join("?" for _ in sources)
            sql += f" AND Source IN ({placeholders})"
            params.extend(sources)

        rows = self.conn.execute(sql, params).fetchall()
        return [_row_to_price(row) for row in rows]
