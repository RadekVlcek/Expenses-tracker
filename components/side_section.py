from tkinter import *
import tkinter.ttk as tk
from window import Window
from database.database import Database

class Side_section(Window, Database):

    def __init__(self, selected_day, selected_month, selected_year):
        self.window = super().window
        self.look_feel_settings = super().look_feel_settings

        self.selected_day = selected_day
        self.selected_month = selected_month
        self.selected_year = selected_year

        Database.__init__(self, "database/data/data.db")

    def fetch_data(self):
        data = Database.fetch_dayitem_data(self)
        return data

    def display_data(self):
        data = self.fetch_data()

        if data is not None:
            for index, item in enumerate(data):
                item_name = item[3]
                item_price = item[4]
                item_remark = item[5]

                Label(self.frame4, text=item_name, fg="white", bg=self.look_feel_settings["dark_blue"]).grid(column=0, row=index+1)
                Label(self.frame4, text=item_price, fg="white", bg=self.look_feel_settings["dark_blue"]).grid(column=1, row=index+1)
                Label(self.frame4, text=item_remark, fg="white", bg=self.look_feel_settings["dark_blue"]).grid(column=2, row=index+1)

    def display_frame7(self):
        # Entire side parent frame
        frame7 = Frame(self.window, bd=0)
        frame7.grid(column=1, row=1, sticky="nswe", rowspan=2)
        frame7.columnconfigure((0, 1, 2), weight=1)
        frame7.rowconfigure((0, 1, 2), weight=3)

        # Stats 1 section
        self.frame4 = Frame(frame7, bd=0, background=self.look_feel_settings["dark_blue"])
        self.frame4.grid(column=0, row=0, sticky="nswe", columnspan=3)

        #self.canvas = Canvas(self.frame4, background=self.look_feel_settings["dark_blue"])
        #self.canvas.grid(column=0, row=0, sticky="nswe")

        item_bought_label = Label(self.frame4, text="Item bought", fg="white", bg=self.look_feel_settings["dark_blue"])
        item_bought_label.grid(column=0, row=0, padx=15, sticky="n")

        amount_spent_label = Label(self.frame4, text="Amount spent", fg="white", bg=self.look_feel_settings["dark_blue"])
        amount_spent_label.grid(column=1, row=0, padx=15, sticky="n")

        remark_label = Label(self.frame4, text="Remark", fg="white", bg=self.look_feel_settings["dark_blue"])
        remark_label.grid(column=2, row=0, padx=15, sticky="n")

        # Stats 2 sections
        frame5 = Frame(frame7, bd=0, background="yellow")
        frame5.grid(column=0, row=1, sticky="nswe", columnspan=3)

        total_spent_today_label = Label(frame5, text="Total spent today: ")
        total_spent_today_label.grid(column=0, row=0)

        rem_balance_today_label = Label(frame5, text="Remaining balance today: ")
        rem_balance_today_label.grid(column=0, row=1)

        # Graph section
        frame6 = Frame(frame7, bd=0, background="blue")
        frame6.grid(column=0, row=2, sticky="nswe", columnspan=3)

        graph_label = Label(frame6, text="Graph:")
        graph_label.grid(column=0, row=0)
