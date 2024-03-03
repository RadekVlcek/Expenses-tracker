from tkinter import *
import tkinter.ttk as tk
from window import Window

class Month(Window):
    def __init__(self, month, days_count):
        self.window = super().window
        self.look_feel_settings = super().look_feel_settings
        self.days_count = days_count

    def display_month(self):
        self.frame3 = Frame(self.window, bd=1, bg=self.look_feel_settings["light_blue"], relief="solid")
        self.frame3.grid(column=0, row=1, sticky="nswe")
        self.frame3.columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.frame3.rowconfigure((0, 1, 2, 3, 4), weight=1)