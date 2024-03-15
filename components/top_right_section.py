from tkinter import *
import tkinter.ttk as tk
from window import Window

class Top_right_section(Window):

    def __init__(self):
        self.window = super().window
        self.look_feel_settings = super().look_feel_settings

    def display_frame8(self):
        selected_day = super().curr_today
        selected_month = super().curr_month
        selected_year = super().curr_year

        frame8 = Frame(self.window, bg=self.look_feel_settings["dark_blue"])
        frame8.grid(row=0, column=1)
        frame8.columnconfigure(1, weight=1)
        frame8.rowconfigure(0, weight=1)
        self.current_date_selected = Label(frame8, text=f"{selected_day}. {selected_month} {selected_year}", font=("Verdana", 21), fg="white", bg=self.look_feel_settings["dark_blue"])
        self.current_date_selected.grid(column=0, row=0)

    def pass_top_right_section(self):
        return self.current_date_selected