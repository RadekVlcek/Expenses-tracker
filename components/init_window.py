from tkinter import *
import tkinter.ttk as tk
from tkinter import messagebox
from components.window import Window
from database.database import Database

class Init_window(Window, Database):
    def __init__(self, window_obj):
        self.window_obj = window_obj
        self.window = super().window
        self.look_feel_settings = super().look_feel_settings
        self.remaining_balance = 0
        self.db_file = super().db_file

    def save_init_rem_balance(self, event):
        value = self.init_rem_value_entry.get()
        
        if value.isdigit():
            if int(value) > 0:
                # Store the value in DB
                self.insert_remaining_balance_table(value)

                # Proceed to displaying main window
                from init import display_main_window
                display_main_window(self.window_obj)
            else:
                messagebox.showinfo(self.window, message="Current balance cannot be zero.")
        else:
            messagebox.showinfo(self.window, message="Please enter a valid number.")

    def initialize_init_window(self):
        self.init_rem_frame = Frame(self.window, bg=self.look_feel_settings["dark_blue"], padx=15, pady=15)
        self.init_rem_label = Label(self.init_rem_frame, text="Current bank balance:", fg="white", bg=self.look_feel_settings["dark_blue"])
        self.init_rem_value_entry = Entry(self.init_rem_frame, fg="white", width=12,  highlightbackground=self.look_feel_settings["dark_blue"], bg=self.look_feel_settings["lighter_blue"])
        self.init_rem_save_button = Button(self.init_rem_frame, text="Save", fg="black", bg=self.look_feel_settings["dark_blue"], highlightbackground=self.look_feel_settings["dark_blue"])
        self.init_rem_save_button.bind("<Button-1>", self.save_init_rem_balance)

    def insert_remaining_balance_table(self, value):
        Database.__init__(self, self.db_file)
        Database.create_remaining_balance_table(self)
        Database.insert_remaining_balance_table(self, value)

    def display_init_window(self):
        self.init_rem_frame.grid(row=0, column=0, sticky="nw")
        self.init_rem_label.grid(row=1, column=0, sticky="w")
        self.init_rem_value_entry.grid(row=1, column=1, sticky="w")
        self.init_rem_save_button.grid(row=1, column=2, sticky="w")
        #self.init_rem_frame.tkraise()