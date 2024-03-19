from tkinter import *
import tkinter.ttk as tk
from window import Window
from database.database import Database
from components.bottom_section import Bottom_section

class Month(Window, Database):
    def __init__(self, month, days_count):
        self.window = super().window
        self.look_feel_settings = super().look_feel_settings
        self.days_count = days_count
        self.db_file = super().db_file

        self.total_spent_this_month = 0

    def display_month(self):
        self.frame3 = Frame(self.window, bd=0, bg=self.look_feel_settings["dark_blue"], relief="solid", padx=0, pady=0)
        self.frame3.grid(column=0, row=1, sticky="")
        self.frame3.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=0)
        self.frame3.rowconfigure((0, 1, 2, 3, 4), weight=0)

    def init_month_db(self, curr_month, selected_month):
        if curr_month == selected_month:
            print(f"Creating DB table for {selected_month}.")
            Database.__init__(self, self.db_file)
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
        spent_per_item = item_price
        remaining_balance = None

        Database.__init__(self, self.db_file)
        Database.insert_monthitem(self, self.month_id, self.day_id, self.year_id, spent_per_item, remaining_balance)

    def update_monthitem(self):
        new_total_spent_today = self.calculate_daily_spent()
        new_remaining_balance = None

        Database.__init__(self, self.db_file)
        Database.update_monthitem(self, self.month_id, self.day_id, new_total_spent_today, new_remaining_balance)

    def fetch_dayitem_total_spent(self):
        Database.__init__(self, self.db_file)
        daily_total_spent = Database.fetch_dayitem_total_spent(self, self.day_id, self.month_id)

        return daily_total_spent

    def calculate_daily_spent(self):
        daily_total_spent = self.fetch_dayitem_total_spent()

        result = 0 
        for index, item in enumerate(daily_total_spent):
            result += item[0]
            
        return result

    def calculate_remaining_balance(self):
        pass

    def fetch_bottom_section_monthly_spent(self, month_id):
        Database.__init__(self, self.db_file)
        data = Database.fetch_monthitem_total_monthly_spent(self, month_id)
        
        total_monthly_spent = 0
        for item in data:
            total_monthly_spent += int(item[0])

        self.total_spent_this_month = total_monthly_spent

        self.pass_total_spent_this_month()

    def return_total_spent_this_month(self):
        return self.total_spent_this_month

    def pass_total_spent_this_month(self):
        bottom_section = Bottom_section()
        bottom_section.initiate_frame9()
        bottom_section.update_total_spent(self.total_spent_this_month)
        bottom_section.display_frame9()
