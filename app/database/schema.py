import sqlite3

DDL = """
CREATE TABLE IF NOT EXISTS Currency (
    ID          INTEGER PRIMARY KEY AUTOINCREMENT,
    Code        TEXT NOT NULL UNIQUE,
    Type        TEXT NOT NULL,
    Name        TEXT,
    Denominator INTEGER NOT NULL DEFAULT 100 CHECK (Denominator >= 1)
);

CREATE TABLE IF NOT EXISTS Account (
    ID          INTEGER PRIMARY KEY AUTOINCREMENT,
    Parent      INTEGER REFERENCES Account(ID),
    Name        TEXT NOT NULL,
    Code        TEXT,
    Description TEXT,
    ExternalID  TEXT,
    IsHidden    INTEGER NOT NULL DEFAULT 0 CHECK (IsHidden IN (0, 1))
);

CREATE TABLE IF NOT EXISTS Trans (
    ID          INTEGER PRIMARY KEY AUTOINCREMENT,
    Date        TEXT NOT NULL,
    Description TEXT
);

CREATE TABLE IF NOT EXISTS Split (
    ID          INTEGER PRIMARY KEY AUTOINCREMENT,
    Trans       INTEGER NOT NULL REFERENCES Trans(ID) ON DELETE CASCADE,
    Account     INTEGER NOT NULL REFERENCES Account(ID),
    Currency    INTEGER NOT NULL REFERENCES Currency(ID),
    Description TEXT,
    ExternalID  TEXT,
    Amount      INTEGER NOT NULL,
    AmountFixed INTEGER NOT NULL DEFAULT 0
);

CREATE INDEX IF NOT EXISTS idx_split_trans    ON Split(Trans);
CREATE INDEX IF NOT EXISTS idx_split_account  ON Split(Account);
CREATE INDEX IF NOT EXISTS idx_split_currency ON Split(Currency);
CREATE INDEX IF NOT EXISTS idx_trans_date     ON Trans(Date, ID);
CREATE INDEX IF NOT EXISTS idx_account_parent ON Account(Parent);
"""


def ensure_schema(conn: sqlite3.Connection) -> None:
    """Create tables and indexes if they do not exist."""
    conn.executescript(DDL)
    conn.commit()
