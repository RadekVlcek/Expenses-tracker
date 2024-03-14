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
        
        self.db_file = super().db_file

    def fetch_frame4_data(self):
        Database.__init__(self, self.db_file)
        data = Database.fetch_dayitem_data(self, self.selected_day, self.selected_month)
        return data

    def display_data_in_frame4(self):
        data = self.fetch_frame4_data()

        if data is not None:
            for index, item in enumerate(data):
                item_name = item[3]
                item_price = item[4]
                item_remark = item[5]

                Label(self.frame4, text=item_name, fg="white", bg=self.look_feel_settings["dark_blue"]).grid(column=0, row=index+1, sticky="we")
                Label(self.frame4, text=item_price, fg="white", bg=self.look_feel_settings["dark_blue"]).grid(column=1, row=index+1, sticky="we")
                Label(self.frame4, text=item_remark, fg="white", bg=self.look_feel_settings["dark_blue"]).grid(column=2, row=index+1, sticky="we")
        else:
            Label(self.frame4, text="No spendings logged", fg="white", bg=self.look_feel_settings["dark_blue"]).grid(column=1, row=2)

    # Initiate everything inside Frame 7
    def initiate_frame7(self):
        self.frame7 = Frame(self.window, bd=0, background=self.look_feel_settings["dark_blue"])
        self.frame7.columnconfigure((0, 1, 2), weight=1)
        self.frame7.rowconfigure((0, 1, 2), weight=3)

    # Initiate everything inside Frame 6
    def initiate_frame6(self):
        self.frame6 = Frame(self.frame7, bd=0, background=self.look_feel_settings["dark_blue"])
        self.graph_label = Label(self.frame6, text="Graph:")

    # Initiate everything inside Frame 5
    def initiate_frame5(self):
        self.frame5 = Frame(self.frame7, bd=0, background=self.look_feel_settings["dark_blue"])
        self.total_spent_today_label = Label(self.frame5, text="Total spent today: ")
        self.rem_balance_today_label = Label(self.frame5, text="Remaining balance today: ")

    # Initiate everything inside Frame 4
    def initiate_frame4(self):
        self.frame4 = Frame(self.frame7, bd=0, background=self.look_feel_settings["dark_blue"])
        self.item_bought_label = Label(self.frame4, text="Item name", fg="white", bg=self.look_feel_settings["dark_blue"])
        self.amount_spent_label = Label(self.frame4, text="Item price (€)", fg="white", bg=self.look_feel_settings["dark_blue"])
        self.remark_label = Label(self.frame4, text="Remark", fg="white", bg=self.look_feel_settings["dark_blue"])

    # Display Frame 7
    def display_frame7(self):
        self.frame7.grid(column=1, row=1, sticky="nswe", rowspan=2)

    # Display everything inside Frame 6
    def display_frame6(self):
        self.frame6.grid(column=0, row=2, sticky="n", columnspan=3)
        self.graph_label.grid(column=0, row=0)

    # Display everything inside Frame 5
    def display_frame5(self):
        self.frame5.grid(column=0, row=1, sticky="n", columnspan=3)
        self.total_spent_today_label.grid(column=0, row=0)
        self.rem_balance_today_label.grid(column=0, row=1)
    
    # Display everything inside Frame 4
    def display_frame4(self):
        self.frame4.grid(column=0, row=0, sticky="n", columnspan=3)
        self.item_bought_label.grid(column=0, row=0, padx=15, sticky="n")
        self.amount_spent_label.grid(column=1, row=0, padx=15, sticky="n")
        self.remark_label.grid(column=2, row=0, padx=15, sticky="n")

    # Initiate and display all frames together
    def init_and_display_all(self):
        self.initiate_frame7()
        self.initiate_frame4()
        self.initiate_frame5()
        self.initiate_frame6()
    
        self.display_frame7()
        self.display_frame4()
        self.display_frame5()
        self.display_frame6()
