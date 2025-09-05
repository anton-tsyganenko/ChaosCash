import sqlite3
from decimal import Decimal

class Database:
    """
    Класс для управления базой данных SQLite.
    Отвечает за всю логику работы с данными.
    """
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON;")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Создает необходимые таблицы, если они не существуют."""
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Account (
                ID INTEGER PRIMARY KEY,
                Parent INTEGER REFERENCES Account(ID),
                Name TEXT,
                Code TEXT,
                Description TEXT,
                External_ID TEXT,
                Status TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Currency (
                ID INTEGER PRIMARY KEY,
                Code TEXT,
                Type TEXT,
                Name TEXT,
                Numerator INTEGER,
                Denominator INTEGER
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Trans (
                ID INTEGER PRIMARY KEY,
                Date TEXT,
                Description TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Split (
                ID INTEGER PRIMARY KEY,
                Trans INTEGER NOT NULL REFERENCES Trans(ID),
                Account INTEGER NOT NULL REFERENCES Account(ID),
                Description TEXT,
                External_ID TEXT,
                Amount INTEGER,
                Currency INTEGER NOT NULL REFERENCES Currency(ID),
                amnt_fix BOOLEAN
            )
        """)
        self.conn.commit()
    
    def get_all_currencies(self):
        """Получает все валюты из базы данных."""
        self.cursor.execute("SELECT ID, Code, Type, Denominator FROM Currency ORDER BY ID")
        return self.cursor.fetchall()

    def get_accounts_with_balances(self):
        """
        Получает все счета с их текущим балансом по каждой валюте.
        """
        self.cursor.execute("""
            SELECT 
                a.ID, a.Parent, a.Name, SUM(s.Amount), c.Code, c.Denominator
            FROM Account a
            LEFT JOIN Split s ON a.ID = s.Account
            LEFT JOIN Currency c ON s.Currency = c.ID
            GROUP BY a.ID, c.ID
            ORDER BY a.ID, c.ID
        """)
        return self.cursor.fetchall()
        
    def get_transactions_by_account_with_balance(self, account_id):
        """
        Получает все транзакции для данного счета с кумулятивным балансом.
        Кумулятивный баланс рассчитывается с помощью оконной функции SQL.
        """
        self.cursor.execute("""
            SELECT
                T.ID,
                T.Date,
                T.Description,
                S.Amount,
                SUM(S.Amount) OVER (PARTITION BY C.ID ORDER BY T.Date, T.ID) AS Balance,
                C.Code,
                C.Denominator
            FROM Trans AS T
            JOIN Split AS S ON T.ID = S.Trans
            JOIN Currency AS C ON S.Currency = C.ID
            WHERE S.Account = ?
            ORDER BY T.Date ASC, T.ID ASC, S.ID ASC;
        """, (account_id,))
        results = [(trans_id, date, desc, Decimal(amnt)/denom, Decimal(bal)/denom, curr, denom)
                  for (trans_id, date, desc, amnt, bal, curr, denom)
                  in self.cursor.fetchall()]
        return results

    def get_splits_by_transaction(self, trans_id):
        """Получает все сплиты для данной транзакции."""
        self.cursor.execute("""
            SELECT
                S.ID, S.Description, S.Account, S.External_ID, S.Amount, S.Currency, S.amnt_fix, C.Denominator
            FROM Split S
            JOIN Currency C on S.Currency = C.ID
            WHERE S.Trans = ?
            UNION
            select '' ID, null Description, null Account, null External_ID, -SUM(Amount), Currency, 0 amnt_fix, C.Denominator
            from split S
            JOIN Currency C on S.Currency = C.ID
            where trans=?
            group by currency
            having SUM(Amount) <> 0
            
            order by
            Currency,
            Amount
        """, (trans_id,trans_id))
        return [
            {
                "split_id": r["ID"],
                "split_desc": r["Description"],
                "acc_id": r["Account"],
                "ext_id": r["External_ID"],
                "amount": Decimal(r["Amount"])/r["Denominator"],
                "curr": r["Currency"],
                "amnt_fix": r["amnt_fix"],
                "denom": r["Denominator"]
            }
            for r in self.cursor.fetchall()
        ]

    def add_transaction(self, date, description):
        """Добавляет новую транзакцию."""
        try:
            self.cursor.execute("INSERT INTO Trans (Date, Description) VALUES (?, ?)", (date, description))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding new transaction: {e}")
            return None

    def update_transaction(self, trans_id, date, description):
        """Обновляет запись о транзакции."""
        try:
            self.cursor.execute("UPDATE Trans SET Date = ?, Description = ? WHERE ID = ?",
                                (date, description, trans_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error updating transaction: {e}")
            return False

    def add_split(self, trans_id, account_id, description, ext_id, amount, currency_id, amnt_fix):
        """Добавляет новую запись о сплите."""
        try:
            self.cursor.execute("INSERT INTO Split (Trans, Account, Description, External_ID, Amount, Currency, amnt_fix) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                (trans_id, account_id, description, ext_id, amount, currency_id, amnt_fix))
            self.conn.commit()
            return self.cursor.lastrowid
        except sqlite3.Error as e:
            print(f"Error adding new split: {e}")
            return None

    def update_split(self, split_id, account_id, description, ext_id, amount, currency_id, amnt_fix):
        """Обновляет запись о сплите."""
        try:
            self.cursor.execute("UPDATE Split SET Account = ?, Description = ?, External_ID = ?, Amount = ?, Currency = ?, amnt_fix = ? WHERE ID = ?",
                                (account_id, description, ext_id, amount, currency_id, amnt_fix, split_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error updating split: {e}")
            return False

    def get_splits_by_id(self, split_id):
        """Получает сплит по его ID."""
        self.cursor.execute("SELECT ID, Trans, Account, Description, External_ID, Amount, Currency, amnt_fix FROM Split WHERE ID = ?", (split_id,))
        return self.cursor.fetchone()

    def get_accounts(self):
        """Получает все счета."""
        self.cursor.execute("SELECT ID, Parent, Name FROM Account")
        return self.cursor.fetchall()

    def get_account_data(self, account_id):
        """Получает данные для одного счета."""
        self.cursor.execute("SELECT ID, Name, Description FROM Account WHERE ID = ?", (account_id,))
        return self.cursor.fetchone()
