import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Data (id INTEGER PRIMARY KEY, date, itemBought, amountSpent INT, remainingBalance INT)")
        self.conn.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM Data")
        fetched_data = self.cursor.fetchall()
        return fetched_data
    
    def insert(self, date, item_bought, amount_spent, remaining_balance):
        self.cursor.execute("INSERT INTO Data VALUES (NULL, ?, ?, ?, ?) ", (date, item_bought, amount_spent, remaining_balance, ))
        self.conn.commit()

    def update(self, id, date, item_bought, amount_spent, remaining_balance):
        self.cursor.execute("UPDATE Data SET date = (?), itemBought = (?), amountSpent = (?), remainingBalance = (?) WHERE id = (?)",
                            (date, item_bought, amount_spent, remaining_balance, id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM Data WHERE id = ?", (id, ))
        self.conn.commit()

    def __del__(self):
        self.conn.close()