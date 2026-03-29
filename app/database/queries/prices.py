"""Raw SQL queries for prices."""

INSERT = """
INSERT INTO Price (OfCurr, Value, InCurr, Date, Source)
VALUES (?, ?, ?, ?, ?)
"""

GET_CANDIDATES_BASE = """
SELECT ID, OfCurr, Value, InCurr, Date, Source
FROM Price
WHERE 1 = 1
"""
