from tkinter import *
import tkinter.ttk as tk
from window import Window

class Bottom_section(Window):

    def __init__(self):
        self.window = super().window
        self.look_feel_settings = super().look_feel_settings

    def display_frame9(self):
        frame9 = Frame(self.window, bg=self.look_feel_settings["dark_blue"])
        frame9.grid(row=2, column=0, sticky="nswe")

        frame9.columnconfigure((0, 1, 2, 3, 4, 5), weight=2)
        frame9.rowconfigure(0, weight=1)

        f5_rem_balance_label = Label(frame9, text="Remaining balance", fg="white", bg=self.look_feel_settings["dark_blue"])
        f5_rem_balance_label.grid(row=0, column=0, sticky="e")
        f5_rem_balance_value = Label(frame9, text="TEST", fg="white", bg=self.look_feel_settings["dark_blue"]) # to be configured
        f5_rem_balance_value.grid(row=0, column=1, sticky="w")

        f5_total_spent_label = Label(frame9, text="Total spent", fg="white", bg=self.look_feel_settings["dark_blue"])
        f5_total_spent_label.grid(row=0, column=2, sticky="e")
        f5_total_spent_value = Label(frame9, text="TEST", fg="white", bg=self.look_feel_settings["dark_blue"]) # to be configured
        f5_total_spent_value.grid(row=0, column=3, sticky="w")

        f5_smtg_else_label = Label(frame9, text="Something else", fg="white", bg=self.look_feel_settings["dark_blue"])
        f5_smtg_else_label.grid(row=0, column=4, sticky="e")
        f5_smtg_else_value = Label(frame9, text="TEST", fg="white", bg=self.look_feel_settings["dark_blue"]) # to be configured
        f5_smtg_else_value.grid(row=0, column=5, sticky="w")