"""Raw SQL queries for accounts."""

GET_ALL = "SELECT ID, Parent, Name, Code, Description, ExternalID, IsHidden FROM Account ORDER BY Name"

GET_BY_ID = "SELECT ID, Parent, Name, Code, Description, ExternalID, IsHidden FROM Account WHERE ID = ?"

GET_CHILDREN = "SELECT ID, Parent, Name, Code, Description, ExternalID, IsHidden FROM Account WHERE Parent = ? ORDER BY Name"

INSERT = "INSERT INTO Account (Parent, Name, Code, Description, ExternalID, IsHidden) VALUES (?, ?, ?, ?, ?, ?)"

UPDATE = "UPDATE Account SET Parent=?, Name=?, Code=?, Description=?, ExternalID=?, IsHidden=? WHERE ID=?"

UPDATE_PARENT = "UPDATE Account SET Parent=? WHERE ID=?"

UPDATE_HIDDEN = "UPDATE Account SET IsHidden=? WHERE ID=?"

DELETE = "DELETE FROM Account WHERE ID=?"

GET_BALANCE = """
SELECT S.Currency, SUM(S.Amount) AS TotalQuants
FROM Split S
WHERE S.Account = ?
GROUP BY S.Currency
"""

MOVE_SPLITS_TO_ACCOUNT = "UPDATE Split SET Account=? WHERE Account=?"

GET_TRANS_IDS_FOR_ACCOUNT = "SELECT DISTINCT Trans FROM Split WHERE Account=?"
