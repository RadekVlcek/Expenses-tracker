from tkinter import *
import tkinter.ttk as tk
from window import Window
from functools import partial

class Day(Window):
    def __init__(self, month_obj, row, col, pass_top_right_section):
        self.frame3 = month_obj.frame3
        self.row = row
        self.col = col
        self.look_feel_settings = month_obj.look_feel_settings
        self.pass_top_right_section = pass_top_right_section

    def display_day(self):
        self.f3_day_frame = Frame(self.frame3, bd=1, relief="solid")
        self.f3_day_frame.grid(row=self.row, column=self.col)

    def get_day_color(self, day_index):
        pass

    def populate_day_props(self, day_index):
        self.f3_day_frame.config(bg=self.look_feel_settings["lighter_blue"])
        # Bind each day to handle_day_click function
        self.f3_day_frame.bind("<Button-1>", partial(self.handle_day_click, day_index))

        self.f3_day_frame.columnconfigure((0, 1), weight=1, minsize=60)
        self.f3_day_frame.rowconfigure((0, 1), weight=1, minsize=60)

        # Day number label - top left corner
        day_label = Label(self.f3_day_frame, text=day_index, font=("Verdana", 20, "italic"), fg="white", bg=self.look_feel_settings["lighter_blue"], padx=4, pady=2)
        day_label.grid(row=0, column=0, sticky="nw")

        # Total spent per day label - middle
        spent_per_day_label = Label(self.f3_day_frame, text="Spent today", fg="white", bg=self.look_feel_settings["lighter_blue"])
        spent_per_day_label.grid(row=1, column=0, columnspan=2)

    # Trigger clicked day button
    def handle_day_click(self, day_index, event):
        print(day_index)
        Window.selected_day = day_index
        Window.selected_year = 2024
        self.pass_top_right_section().config(text=f"{Window.selected_day} {Window.selected_month} {Window.selected_year}")