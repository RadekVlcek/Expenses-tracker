from tkinter import *
import tkinter.ttk as tk
from datetime import date

class Window:
    # Initialize Tk main window
    window = Tk()
    look_feel_settings = {
        "dark_blue": "#0a1829",
        "light_blue": "#0f243e",
        "lighter_blue": "#143052",
        "day_today": "#1a3a5e"
    }

    # Date today
    today = date.today()
    curr_today = today.strftime("%d")[1]
    curr_month = today.strftime("%B")
    curr_year = today.strftime("%Y")

    # Initially selected day, month and year
    selected_day = curr_today
    selected_month = curr_month
    selected_year = curr_year

    def __init__(self):
        # Window startup size
        window_height = self.window.winfo_screenwidth()
        window_width = self.window.winfo_screenheight()

        self.window.geometry("1440x900")
        self.window.minsize(1440, 900)
        self.window.title("Expenses Tracker")
        self.window.configure(bg="#0a1829")

        # Configure main window columns
        self.window.columnconfigure(0, weight=7)
        self.window.columnconfigure(1, weight=5)

        # Configure main window rows
        self.window.rowconfigure(0, weight=0)
        self.window.rowconfigure(1, weight=1)
        self.window.rowconfigure(2, weight=1)

        self.months = {
            "January": 31,
            "February": 29,
            "March": 31,
            "April": 30,
            "May": 31,
            "June": 30,
            "July": 31,
            "August": 31,
            "September": 30,
            "October": 31,
            "November": 30,
            "December": 31
        }

    def display_window(self):
        self.window.mainloop()