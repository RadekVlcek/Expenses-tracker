import sqlite3
from datetime import date

class Database:
    def __init__(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(e)
        else:
            print("Database connected")

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
            print(e)
        else:
            self.conn.commit()

    def insert_dayitem(self, day_id, month_id, item_name, item_price, remark):
        try:
            self.cursor.execute("INSERT INTO DayItem VALUES (NULL, ?, ?, ?, ?, ?) ", (day_id, month_id, item_name, item_price, remark))
        except sqlite3.Error as e:
            print(e)
        else:
            self.conn.commit()
            print("Data inserted")

    def fetch_dayitem_data(self):
        try:
            self.cursor.execute("SELECT * FROM DayItem")
        except sqlite3.Error as e:
            print(e)
        else:
            fetched_data = self.cursor.fetchall()
            return fetched_data

    def create_month_table(self):
        try:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS MonthItem (
                    MonthID TEXT PRIMARY KEY,
                    DayID INT,
                    YearID INT,
                    TotalSpentToday INT, 
                    RemainingBalanceToday INT
                )""")
        except sqlite3.Error as e:
            print(e)
        else:
            self.conn.commit()