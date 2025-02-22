# db/database.py
import sqlite3

class Database:
    def __init__(self, db_name="finance.db"):
        self.db_name = db_name
        self.init_db()

    def get_connection(self):
        """Returns a new database connection."""
        return sqlite3.connect(self.db_name)

    def init_db(self):
        """Initializes the database with the transactions table."""
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    date TEXT NOT NULL,
                    description TEXT NOT NULL
                )
            """)
            conn.commit()

    def add_transaction(self, amount, category, description):
        """Inserts a new transaction."""
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute("INSERT INTO transactions (amount, category, date, description) VALUES (?, ?, date('now'), ?)",
                      (amount, category, description))
            conn.commit()

    def get_balance(self):
        """Calculates the total balance."""
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute("SELECT SUM(amount) FROM transactions")
            return c.fetchone()[0] or 0

    def get_transactions(self, category=None):
        """Fetches all transactions or filtered by category."""
        with self.get_connection() as conn:
            c = conn.cursor()
            if category:
                c.execute("SELECT amount, category, date, description, id FROM transactions WHERE category = ? ORDER BY date DESC",
                          (category,))
            else:
                c.execute("SELECT amount, category, date, description, id FROM transactions ORDER BY date DESC")
            return c.fetchall()

    def delete_transaction(self, transaction_id):
        """Deletes a transaction by ID."""
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
            conn.commit()

    def get_monthly_expenses(self):
        """Aggregates expenses by month for prediction."""
        with self.get_connection() as conn:
            c = conn.cursor()
            c.execute("""
                SELECT strftime('%Y-%m', date) AS month, SUM(amount) 
                FROM transactions 
                WHERE amount < 0 
                GROUP BY month 
                ORDER BY month
            """)
            return c.fetchall()