"""Raw SQL queries for currencies."""

GET_ALL = "SELECT ID, Code, Type, Name, Denominator FROM Currency ORDER BY Code"

GET_BY_ID = "SELECT ID, Code, Type, Name, Denominator FROM Currency WHERE ID=?"

INSERT = "INSERT INTO Currency (Code, Type, Name, Denominator) VALUES (?, ?, ?, ?)"

UPDATE = "UPDATE Currency SET Code=?, Type=?, Name=?, Denominator=? WHERE ID=?"

DELETE = "DELETE FROM Currency WHERE ID=?"

IS_USED = "SELECT COUNT(*) FROM Split WHERE Currency=?"
