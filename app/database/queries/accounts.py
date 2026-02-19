"""Raw SQL queries for accounts."""

GET_ALL = "SELECT ID, Parent, Name, Code, Description, ExternalID, Status FROM Account ORDER BY Name"

GET_BY_ID = "SELECT ID, Parent, Name, Code, Description, ExternalID, Status FROM Account WHERE ID = ?"

GET_CHILDREN = "SELECT ID, Parent, Name, Code, Description, ExternalID, Status FROM Account WHERE Parent = ? ORDER BY Name"

GET_ROOT = "SELECT ID, Parent, Name, Code, Description, ExternalID, Status FROM Account WHERE Parent IS NULL ORDER BY Name"

INSERT = "INSERT INTO Account (Parent, Name, Code, Description, ExternalID, Status) VALUES (?, ?, ?, ?, ?, ?)"

UPDATE = "UPDATE Account SET Parent=?, Name=?, Code=?, Description=?, ExternalID=?, Status=? WHERE ID=?"

UPDATE_PARENT = "UPDATE Account SET Parent=? WHERE ID=?"

UPDATE_STATUS = "UPDATE Account SET Status=? WHERE ID=?"

DELETE = "DELETE FROM Account WHERE ID=?"

GET_BALANCE = """
SELECT C.Code, C.ID AS CurrencyID, SUM(S.Amount) AS TotalQuants, C.Denominator
FROM Split S
JOIN Currency C ON S.Currency = C.ID
WHERE S.Account = ?
GROUP BY S.Currency
"""

MOVE_SPLITS_TO_ACCOUNT = "UPDATE Split SET Account=? WHERE Account=?"

GET_TRANS_IDS_FOR_ACCOUNT = "SELECT DISTINCT Trans FROM Split WHERE Account=?"
