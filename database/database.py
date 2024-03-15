import sqlite3
from datetime import date

class Database:
    def __init__(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"DB: Error: {e}")
        else:
            print("DB: Database connected")

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
            print(f"DB: Error (create_day_table): {e}")
        else:
            self.conn.commit()

    def insert_dayitem(self, day_id, month_id, item_name, item_price, remark):
        try:
            self.cursor.execute("INSERT INTO DayItem VALUES (NULL, ?, ?, ?, ?, ?)", (day_id, month_id, item_name, item_price, remark, ))
        except sqlite3.Error as e:
            print(f"DB: Error (insert_dayitem): {e}")
        else:
            self.conn.commit()
            print("DB: DayItem table: Data inserted into Day table.")

    def fetch_dayitem_data(self, day_id, month_id):
        try:
            self.cursor.execute("SELECT * FROM DayItem WHERE DayID = ? AND MonthID = ?", (day_id, month_id))
        except sqlite3.Error as e:
            print(f"DB: Error (fetch_dayitem_data): {e}")
        else:
            fetched_data = self.cursor.fetchall()
            print("DB: DayItem table: All daily data fetched.")
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
            print(f"DB: Error (create_month_table): {e}")
        else:
            self.conn.commit()
            print("DB: MonthItem table: Month tablet created.")

    def insert_monthitem(self, month_id, day_id, year_id, total_spent_today, remaining_balance):
        try:
            self.cursor.execute("INSERT INTO MonthItem VALUES (?, ?, ?, ?, ?)", (month_id, day_id, year_id, total_spent_today, remaining_balance, ))
        except sqlite3.Error as e:
            print(f"DB: Error (insert_monthitem): {e}")
        else:
            self.conn.commit()
            print("DB: Monthitem table: Data inserted into Month table.")

    def update_monthitem(self, month_id, day_id, new_amount):
        try:
            self.cursor.execute("UPDATE MonthItem SET TotalSpentToday = ? WHERE MonthID = ? AND DayID = ?", (new_amount, month_id, day_id, ))
        except sqlite3.Error as e:
            print(f"DB: Error (update_monthitem): {e}")
        else:
            self.conn.commit()
            print("DB: Monthitem table: Updated total spent amount inserted: ")

    def fetch_dayitem_total_spent(self, day_id, month_id):
        try:
            self.cursor.execute("SELECT ItemPrice FROM DayItem WHERE DayID = ? AND MonthID = ?", (day_id, month_id, ))
        except sqlite3.Error as e:
            print(f"DB: Error (fetch_dayitem_total_spent): {e}")
        else:
            fetched_data = self.cursor.fetchall()
            return fetched_data

    def fetch_monthitem_total_daily_spent(self, day_id, month_id):
        try:
            self.cursor.execute("SELECT TotalSpentToday FROM MonthItem WHERE DayID = ? AND MonthID = ?", (day_id, month_id, ))
        except sqlite3.Error as e:
            print(f"DB: Error (fetch_monthitem_total_daily_spent): {e}")
        else:
            fetched_data = self.cursor.fetchall()
            return fetched_data

    def check_if_day_exists(self, month_id, day_id):
        try:
            self.cursor.execute("SELECT EXISTS (SELECT 1 FROM MonthItem WHERE MonthID = ? AND DayID = ?)", (month_id, day_id, ))
        except sqlite3.Error as e:
            print(f"DB: Error (check_if_day_exists): {e}")
        else:
            result = self.cursor.fetchone()[0]
            return bool(result)

    def fetch_monthitem_total_monthly_spent(self, month_id):
        try:
            self.cursor.execute("SELECT TotalSpentToday FROM MonthItem WHERE MonthID = ?", (month_id, ))
        except sqlite3.Error as e:
            print(f"DB: Error (fetch_monthitem_total_monthly_spent): {e}")
        else:
            fetched_data = self.cursor.fetchall()
            return fetched_data

    def fetch_monthitem_for_graph(self, month_id):
        try:
            self.cursor.execute("SELECT DayID, TotalSpentToday FROM MonthItem WHERE MonthID = ?", (month_id, ))
        except sqlite3.Error as e:
            print(f"DB: Error (fetch_monthitem_for_graph): {e}")
        else:
            fetched_data = self.cursor.fetchall()
            return fetched_data

    # Year functions
    def create_year_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS YearItem (
                    MonthID TEXT,
                    YearID INT,
                    TotalSpentThisMonth INT,
                    RemainingBalanceThisMonth INT,
                    FOREIGN KEY(MonthID) REFERENCES MonthItem(MonthID)
                )""")
        except sqlite3.Error as e:
            print(f"DB: Error (create_year_table): {e}")
        else:
            self.conn.commit()

"""
    def __del__(self):
        try:
            self.conn.close()
        except sqlite3.Error as e:
            print(e)
        else:
            print("DB: Database closed. \n")

 """