"""Raw SQL queries for splits."""

GET_BY_ID = """
SELECT S.ID, S.Trans, S.Account, S.Currency, S.Description, S.ExternalID, S.Amount, S.AmountFixed
FROM Split S WHERE S.ID=?
"""

GET_BY_TRANSACTION = """
SELECT S.ID, S.Trans, S.Account, S.Currency, S.Description, S.ExternalID, S.Amount, S.AmountFixed
FROM Split S WHERE S.Trans=? ORDER BY S.Currency, S.ID
"""

GET_BY_TRANSACTION_AND_CURRENCY = """
SELECT S.ID, S.Trans, S.Account, S.Currency, S.Description, S.ExternalID, S.Amount, S.AmountFixed
FROM Split S WHERE S.Trans=? AND S.Currency=? ORDER BY S.ID
"""

INSERT = """
INSERT INTO Split (Trans, Account, Currency, Description, ExternalID, Amount, AmountFixed)
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

UPDATE = """
UPDATE Split SET Account=?, Currency=?, Description=?, ExternalID=?, Amount=?, AmountFixed=? WHERE ID=?
"""

UPDATE_AMOUNT = "UPDATE Split SET Amount=? WHERE ID=?"

UPDATE_AMOUNT_FIXED = "UPDATE Split SET AmountFixed=? WHERE ID=?"

UPDATE_ACCOUNT = "UPDATE Split SET Account=? WHERE ID=?"

DELETE = "DELETE FROM Split WHERE ID=?"

DELETE_BY_ACCOUNT = "DELETE FROM Split WHERE Account=?"

GET_LAST_CURRENCY_FOR_ACCOUNT = """
SELECT S.Currency FROM Split S
JOIN Trans T ON S.Trans = T.ID
WHERE S.Account=?
ORDER BY T.Date DESC, T.ID DESC, S.ID DESC
LIMIT 1
"""

CHECK_ZERO_AMOUNTS = """
SELECT ID FROM Split WHERE Amount=0
"""

HAS_SPLITS_FOR_ACCOUNT = "SELECT 1 FROM Split WHERE Account=? LIMIT 1"
