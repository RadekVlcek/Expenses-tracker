from tkinter import *
import tkinter.ttk as tk
from window import Window

class Bottom_section(Window):

    def __init__(self):
        self.window = super().window
        self.look_feel_settings = super().look_feel_settings
        self.fetch_remaining_balance()

    def initiate_frame9(self):
        self.frame9 = Frame(self.window, bg=self.look_feel_settings["dark_blue"])
        self.frame9.columnconfigure((0, 1, 2, 3), weight=1)
        self.frame9.rowconfigure(0, weight=1)

        self.f5_total_spent_label = Label(self.frame9, text="Total spent ", fg="white", bg=self.look_feel_settings["dark_blue"])
        self.f5_total_spent_value = Label(self.frame9, text="", fg="white", bg=self.look_feel_settings["dark_blue"], font=("Verdana", 24))

        self.f5_rem_balance_label = Label(self.frame9, text="Remaining balance ", fg="white", bg=self.look_feel_settings["dark_blue"])
        self.f5_rem_balance_value = Label(self.frame9, text="", fg="white", bg=self.look_feel_settings["dark_blue"], font=("Verdana", 24))

    def display_frame9(self):
        self.frame9.grid(row=2, column=0, sticky="nswe")

        self.f5_total_spent_label.grid(row=0, column=0, sticky="e")
        self.f5_total_spent_value.grid(row=0, column=1, sticky="w")

        self.f5_rem_balance_label.grid(row=0, column=2, sticky="e")
        self.f5_rem_balance_value.grid(row=0, column=3, sticky="w")

    def update_total_spent(self, new_total_spent):
        self.f5_total_spent_value.config(text=f"€{new_total_spent}")

    def pass_total_spent_this_month(self, new_total_spent):
        self.f5_total_spent_value.config(text=f"€{new_total_spent}")

    def fetch_remaining_balance(self):
        pass