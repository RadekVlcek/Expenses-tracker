from tkinter import *
import tkinter.ttk as tk
from window import Window
from database.database import Database
from components.side_section import Side_section
from functools import partial

class Day(Window, Database):

    test = None

    def __init__(self, month_obj, pass_top_right_section):
        self.frame3 = month_obj.frame3
        self.look_feel_settings = month_obj.look_feel_settings
        self.pass_top_right_section = pass_top_right_section
        self.db_file = Window.db_file
        self.selected_day_frame_label = None

    def display_day(self, row, col):
        self.f3_day_frame = Frame(self.frame3, bd=1, relief="solid")
        self.f3_day_frame.grid(row=row, column=col, padx=7, pady=7)

    def fetch_monthitem_total_daily_spent(self, day_id, month_id):
        Database.__init__(self, self.db_file)
        daily_total_spent_db = Database.fetch_monthitem_total_daily_spent(self, day_id, month_id)

        # Check if daily_total_spent for the day is empty:
        if not daily_total_spent_db:
            return ""
        else:
            return f"€{daily_total_spent_db[0][0]}"

    def update_total_spent_for_day(self, updated_amount):
        self.spent_per_day_label.config(text=updated_amount)

    def today_button_props(self, day, month):
        actual_day_today = int(Window.curr_today)
        actual_month_today = str(Window.curr_month)

        if day == actual_day_today and month == actual_month_today:
            return 1
        else:
            return 0

    def populate_day_props(self, day_index, month_id):
        # Configure button spacing
        self.f3_day_frame.columnconfigure((0, 1), weight=1, minsize=60)
        self.f3_day_frame.rowconfigure((0, 1), weight=1, minsize=60)

        # Configure button default color
        today_button_props = self.today_button_props(day_index, month_id)
        self.f3_day_frame.config(bg=self.look_feel_settings["lighter_blue"], highlightthickness=today_button_props)

        # Configure button on-hover and off-hover color
        self.f3_day_frame.bind("<Enter>", self.handle_hover_enter)
        self.f3_day_frame.bind("<Leave>", self.handle_hover_leave)

        # Configure binding to handle_day_click function
        self.f3_day_frame.bind("<Button-1>", partial(self.handle_day_click, day_index, self.f3_day_frame))

        # Day number label - top left corner
        self.day_label = Label(self.f3_day_frame, text=day_index, font=("Verdana", 24), fg="white", bg=self.look_feel_settings["lighter_blue"], padx=4, pady=2)
        self.day_label.grid(row=0, column=0, sticky="nw")
        self.day_label.bind("<Button-1>", partial(self.handle_day_click, day_index, self.f3_day_frame))

        # Total spent per day label - middle
        self.daily_total_spent = self.fetch_monthitem_total_daily_spent(day_index, month_id)
        self.spent_per_day_label = Label(self.f3_day_frame, text=f"{self.daily_total_spent}", fg="white", bg=self.look_feel_settings["lighter_blue"])
        self.spent_per_day_label.grid(row=1, column=0, columnspan=2)
        self.spent_per_day_label.bind("<Button-1>", partial(self.handle_day_click, day_index, self.f3_day_frame))
    
    def handle_hover_enter(self, event):
        self.f3_day_frame.config(bg=self.look_feel_settings["button_hover_enter"])
        self.day_label.config(bg=self.look_feel_settings["button_hover_enter"])
        self.spent_per_day_label.config(bg=self.look_feel_settings["button_hover_enter"])

    def handle_hover_leave(self, event):
        self.f3_day_frame.config(bg=self.look_feel_settings["lighter_blue"])
        self.day_label.config(bg=self.look_feel_settings["lighter_blue"])
        self.spent_per_day_label.config(bg=self.look_feel_settings["lighter_blue"])

    def handle_day_click(self, day_index, event, f3_day_frame):
        # Update top right section with selected day, month and year
        Window.selected_day = day_index
        Window.selected_year = 2024
        self.pass_top_right_section().config(text=f"{Window.selected_day}. {Window.selected_month}, {Window.selected_year}")

        # Initiate Side_section object and reload the section
        side_section = Side_section(Window.selected_day, Window.selected_month, Window.selected_year)
        side_section.init_and_display_all()

        # Trigger displaying data in frame4 for day clicked
        side_section.display_frame4_data()

        # Trigger displaying data in frame5 for day clicked
        side_section.display_frame5_data()

        # Pass currently selected Day element to Window class
        self.pass_selected_day_amount_label()

    # Insert data into DayItem table. Called from database.py
    def insert_dayitem_to_db(self, day_id, month_id, item_name, item_price, item_remark):
        Database.__init__(self, self.db_file)
        self.create_day_table()
        self.insert_dayitem(day_id, month_id, item_name, item_price, item_remark)
        self.clear_entries()

    # Pass selected_day_amount_label to Window object
    def pass_selected_day_amount_label(self):
        Window.selected_day_amount_label = self.spent_per_day_label

    # Pass selected_day_amount_label to Main for further processing for initial startup
    def return_current_day_amount_label(self, day, month):
        actual_day_today = int(Window.curr_today)
        actual_month_today = str(Window.curr_month)
        if day == actual_day_today and month == actual_month_today:
            return self.spent_per_day_label
        else:
            return None

    def return_first_day_amount_label(self):
        return self.spent_per_day_label