from tkinter import *
import tkinter.ttk as tk
from window import Window
from database.database import Database
from components.side_section import Side_section
from functools import partial

class Day(Window, Database):
    def __init__(self, month_obj, row, col, pass_top_right_section):
        self.frame3 = month_obj.frame3
        self.row = row
        self.col = col
        self.look_feel_settings = month_obj.look_feel_settings
        self.pass_top_right_section = pass_top_right_section
        self.db_file = Window.db_file
        self.f3_day_frame_today = None

    def display_day(self):
        self.f3_day_frame = Frame(self.frame3, bd=1, relief="solid", padx=0, pady=0)
        self.f3_day_frame.grid(row=self.row, column=self.col)

    def fetch_monthitem_total_daily_spent(self, day_id, month_id):
        Database.__init__(self, self.db_file)
        daily_total_spent = Database.fetch_monthitem_total_daily_spent(self, day_id, month_id)

        # Check if daily_total_spent for the day is empty:
        if not daily_total_spent:
            return ""
        else:
            return f"€{daily_total_spent[0][0]}"

    def today_button_color(self, day, month):
        actual_day_today = int(Window.curr_today)
        actual_month_today = str(Window.curr_month)
        if day == actual_day_today and month == actual_month_today:
            self.f3_day_frame_today = self.f3_day_frame
            return "day_today", 1
        else:
            return "lighter_blue", 0

    def populate_day_props(self, day_index, month_id):
        # Configure button spacing
        self.f3_day_frame.columnconfigure((0, 1), weight=1, minsize=60)
        self.f3_day_frame.rowconfigure((0, 1), weight=1, minsize=60)

        # Configure button default color
        get_color = self.today_button_color(day_index, month_id)
        self.f3_day_frame.config(bg=self.look_feel_settings[get_color[0]], highlightbackground=self.look_feel_settings[get_color[0]], highlightthickness=get_color[1])

        # Configure button on-hover and off-hover color
        self.f3_day_frame.bind("<Enter>", self.handle_hover_enter)
        self.f3_day_frame.bind("<Leave>", self.handle_hover_leave)

        # Configure binding to handle_day_click function
        self.f3_day_frame.bind("<Button-1>", partial(self.handle_day_click, day_index))

        # Day number label - top left corner
        self.day_label = Label(self.f3_day_frame, text=day_index, font=("Verdana", 20, "italic"), fg="white", bg=self.look_feel_settings[get_color[0]], padx=4, pady=2)
        self.day_label.grid(row=0, column=0, sticky="nw")
        self.day_label.bind("<Button-1>", partial(self.handle_day_click, day_index))

        # Total spent per day label - middle
        daily_total_spent = self.fetch_monthitem_total_daily_spent(day_index, month_id)
        self.spent_per_day_label = Label(self.f3_day_frame, text=f"{daily_total_spent}", fg="white", bg=self.look_feel_settings[get_color[0]])
        self.spent_per_day_label.grid(row=1, column=0, columnspan=2)
        self.spent_per_day_label.bind("<Button-1>", partial(self.handle_day_click, day_index))
    
    def handle_hover_enter(self, event):
        if self.f3_day_frame is not self.f3_day_frame_today:
            self.f3_day_frame.config(bg=self.look_feel_settings["button_hover_enter"])
            self.day_label.config(bg=self.look_feel_settings["button_hover_enter"])
            self.spent_per_day_label.config(bg=self.look_feel_settings["button_hover_enter"])

    def handle_hover_leave(self, event):
        if self.f3_day_frame is not self.f3_day_frame_today:
            self.f3_day_frame.config(bg=self.look_feel_settings["lighter_blue"])
            self.day_label.config(bg=self.look_feel_settings["lighter_blue"])
            self.spent_per_day_label.config(bg=self.look_feel_settings["lighter_blue"])

    def handle_day_click(self, day_index, event):
        # Update top right section with selected day, month and year
        Window.selected_day = day_index
        Window.selected_year = 2024
        self.pass_top_right_section().config(text=f"{Window.selected_day} {Window.selected_month} {Window.selected_year}")

        print(f"Selected (day click): {Window.selected_day}. {Window.selected_month}, {Window.selected_year}")

        # Trigger displaying data for the day clicked
        side_section = Side_section(Window.selected_day, Window.selected_month, Window.selected_year)
        side_section.init_and_display_all()
        side_section.display_data_in_frame4()

    # Insert data into DayItem table. Called from database.py
    def insert_dayitem_to_db(self, day_id, month_id, item_name, item_price, item_remark):
        Database.__init__(self, self.db_file)
        self.create_day_table()
        self.insert_dayitem(day_id, month_id, item_name, item_price, item_remark)
        self.clear_entries()

