from tkinter import *
import tkinter.ttk as tk
from window import Window
from database.database import Database

class Month(Window, Database):
    def __init__(self, month, days_count):
        self.window = super().window
        self.look_feel_settings = super().look_feel_settings
        self.days_count = days_count

    def display_month(self):
        self.frame3 = Frame(self.window, bd=1, bg=self.look_feel_settings["light_blue"], relief="solid")
        self.frame3.grid(column=0, row=1, sticky="nswe")
        self.frame3.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.frame3.rowconfigure((0, 1, 2, 3, 4), weight=1)

    def init_month_db(self, curr_month, selected_month):
        if curr_month == selected_month:
            print(f"Creating DB table for {selected_month}.")
            Database.__init__(self, "database/data/data.db")
            Database.create_month_table(self)

    def handle_month_input(self, item_price):
        self.month_id = Window.selected_month
        self.day_id = Window.selected_day
        self.year_id = Window.selected_year

        day_entry_exists = Database.check_if_day_exists(self, self.month_id, self.day_id)

        if day_entry_exists:
            self.update_monthitem()
        else:
            self.insert_monthitem_to_db(item_price)

    def insert_monthitem_to_db(self, item_price):
        total_spent_today = item_price
        remaining_balance = None

        Database.__init__(self, "database/data/data.db")
        Database.insert_monthitem(self, self.month_id, self.day_id, self.year_id, total_spent_today, remaining_balance)

    def update_monthitem(self):
        new_total_spent_today = self.calculate_daily_spent()

        Database.__init__(self, "database/data/data.db")
        Database.update_monthitem(self, self.month_id, self.day_id, new_total_spent_today)

    def fetch_dayitem_total_spent(self):
        Database.__init__(self, "database/data/data.db")
        daily_total_spent = Database.fetch_dayitem_total_spent(self, self.month_id)

        return daily_total_spent

    def calculate_daily_spent(self):
        daily_total_spent = self.fetch_dayitem_total_spent()

        result = 0 
        for index, item in enumerate(daily_total_spent):
            result += item[0]
            
        return result