"""Raw SQL queries for transactions."""

GET_BY_ID = "SELECT ID, Date, Description FROM Trans WHERE ID=?"

INSERT = "INSERT INTO Trans (Date, Description) VALUES (?, ?)"

UPDATE = "UPDATE Trans SET Date=?, Description=? WHERE ID=?"

DELETE = "DELETE FROM Trans WHERE ID=?"

GET_VERBOSE_BY_ACCOUNTS = """
SELECT
    T.ID,
    T.Date,
    T.Description,
    S.ID AS SplitID,
    S.Amount,
    SUM(S.Amount) OVER (PARTITION BY S.Account, S.Currency ORDER BY T.Date, T.ID, S.ID) AS Balance,
    C.Code AS CurrencyCode,
    C.Denominator,
    S.Account AS AccountID
FROM Trans AS T
JOIN Split AS S ON T.ID = S.Trans
JOIN Currency AS C ON S.Currency = C.ID
WHERE S.Account IN ({placeholders})
ORDER BY T.Date ASC, T.ID ASC, S.ID ASC
"""

GET_SUMMARY_BY_ACCOUNTS = """
WITH q AS (
    SELECT
        T.ID,
        T.Date,
        T.Description,
        SUM(S.Amount) AS TotalAmount,
        S.Currency,
        C.Code AS CurrencyCode,
        C.Denominator
    FROM Trans AS T
    JOIN Split AS S ON T.ID = S.Trans
    JOIN Currency AS C ON S.Currency = C.ID
    WHERE S.Account IN ({placeholders})
    GROUP BY T.ID, S.Currency
    HAVING SUM(S.Amount) <> 0
)
SELECT
    ID, Date, Description, TotalAmount,
    SUM(TotalAmount) OVER (PARTITION BY Currency ORDER BY Date, ID) AS Balance,
    CurrencyCode, Denominator, Currency
FROM q
ORDER BY Date ASC, ID ASC
"""

GET_IMBALANCED = """
SELECT Trans, Currency, SUM(Amount) AS Imbalance
FROM Split
GROUP BY Trans, Currency
HAVING SUM(Amount) <> 0
"""

GET_EMPTY = """
SELECT T.ID, T.Date, T.Description
FROM Trans T
LEFT JOIN Split S ON T.ID = S.Trans
WHERE S.ID IS NULL
"""

GET_VERBOSE_BY_IDS = """
SELECT
    T.ID,
    T.Date,
    T.Description,
    S.ID AS SplitID,
    S.Amount,
    SUM(S.Amount) OVER (PARTITION BY S.Account, S.Currency ORDER BY T.Date, T.ID, S.ID) AS Balance,
    C.Code AS CurrencyCode,
    C.Denominator,
    S.Account AS AccountID
FROM Trans AS T
LEFT JOIN Split AS S ON T.ID = S.Trans
LEFT JOIN Currency AS C ON S.Currency = C.ID
WHERE T.ID IN ({placeholders})
ORDER BY T.Date ASC, T.ID ASC, S.ID ASC
"""

GET_SUMMARY_BY_IDS = """
WITH q AS (
    SELECT
        T.ID,
        T.Date,
        T.Description,
        SUM(S.Amount) AS TotalAmount,
        S.Currency,
        C.Code AS CurrencyCode,
        C.Denominator
    FROM Trans AS T
    LEFT JOIN Split AS S ON T.ID = S.Trans
    LEFT JOIN Currency AS C ON S.Currency = C.ID
    WHERE T.ID IN ({placeholders})
    GROUP BY T.ID, S.Currency
)
SELECT
    ID, Date, Description, TotalAmount,
    SUM(TotalAmount) OVER (PARTITION BY Currency ORDER BY Date, ID) AS Balance,
    CurrencyCode, Denominator, Currency
FROM q
ORDER BY Date ASC, ID ASC
"""

GET_AUTOCOMPLETE = """
SELECT DISTINCT T.ID, T.Date, T.Description
FROM Trans T
JOIN Split S ON T.ID = S.Trans
WHERE S.Account = ? AND T.Description LIKE ?
ORDER BY T.Date DESC, T.ID DESC
LIMIT 20
"""

GET_SPLITS_FOR_TRANS = """
SELECT S.ID, S.Trans, S.Account, S.Currency, S.Description, S.ExternalID, S.Amount, S.AmountFixed
FROM Split S
WHERE S.Trans = ?
ORDER BY S.Currency, S.ID
"""
