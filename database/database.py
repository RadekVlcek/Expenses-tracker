import sqlite3
from datetime import date

class Database:
    def __init__(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Error: {e}")
        else:
            print("Database connected")

    # Day functions
    def create_day_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS DayItem (
                    ItemID INTEGER PRIMARY KEY,
                    DayID INT,
                    MonthID TEXT,
                    ItemName TEXT,
                    ItemPrice INT,
                    Remark TEXT,
                    FOREIGN KEY(MonthID) REFERENCES MonthItem(MonthID)
                )""")
        except sqlite3.Error as e:
            print(f"Error (create_day_table): {e}")
        else:
            self.conn.commit()

    def insert_dayitem(self, day_id, month_id, item_name, item_price, remark):
        try:
            self.cursor.execute("INSERT INTO DayItem VALUES (NULL, ?, ?, ?, ?, ?)", (day_id, month_id, item_name, item_price, remark, ))
        except sqlite3.Error as e:
            print(f"Error (insert_dayitem): {e}")
        else:
            self.conn.commit()
            print("DayItem table: Data inserted into Day table.")

    def fetch_dayitem_data(self, day_id, month_id):
        try:
            self.cursor.execute("SELECT * FROM DayItem WHERE DayID = ? AND MonthID = ?", (day_id, month_id))
        except sqlite3.Error as e:
            print(f"Error (fetch_dayitem_data): {e}")
        else:
            fetched_data = self.cursor.fetchall()
            print("DayItem table: All daily data fetched.")
            return fetched_data

    # Month functions
    def create_month_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS MonthItem (
                    MonthID TEXT,
                    DayID INT,
                    YearID INT,
                    TotalSpentToday INT, 
                    RemainingBalanceToday INT
                )""")
        except sqlite3.Error as e:
            print(f"Error (create_month_table): {e}")
        else:
            self.conn.commit()
            print("MonthItem table: Month tablet created.")

    def insert_monthitem(self, month_id, day_id, year_id, total_spent_today, remaining_balance):
        try:
            self.cursor.execute("INSERT INTO MonthItem VALUES (?, ?, ?, ?, ?)", (month_id, day_id, year_id, total_spent_today, remaining_balance, ))
        except sqlite3.Error as e:
            print(f"Error (insert_monthitem): {e}")
        else:
            self.conn.commit()
            print("Monthitem table: Data inserted into Month table.")

    def update_monthitem(self, month_id, day_id, new_amount):
        try:
            self.cursor.execute("UPDATE MonthItem SET TotalSpentToday = ? WHERE MonthID = ? AND DayID = ?", (new_amount, month_id, day_id, ))
        except sqlite3.Error as e:
            print(f"Error (update_monthitem): {e}")
        else:
            self.conn.commit()
            print("Monthitem table: Updated total spent amount inserted: ")

    def fetch_dayitem_total_spent(self, day_id, month_id):
        try:
            self.cursor.execute("SELECT ItemPrice FROM DayItem WHERE DayID = ? AND MonthID = ?", (day_id, month_id, ))
        except sqlite3.Error as e:
            print(f"Error (fetch_dayitem_total_spent): {e}")
        else:
            fetched_data = self.cursor.fetchall()
            print("Dayitem table: Daily total spent data fetched: ", fetched_data)
            return fetched_data

    def check_if_day_exists(self, month_id, day_id):
        try:
            self.cursor.execute("SELECT EXISTS (SELECT 1 FROM MonthItem WHERE MonthID = ? AND DayID = ?)", (month_id, day_id, ))
        except sqlite3.Error as e:
            print(f"Error (check_if_day_exists): {e}")
        else:
            result = self.cursor.fetchone()[0]
            return bool(result)
