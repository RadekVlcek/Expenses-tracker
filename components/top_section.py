from tkinter import *
import tkinter.ttk as tk
from tkinter import messagebox
from datetime import date
from functools import partial
from database.database import Database
from components.side_section import Side_section
from day import Day
from month import Month
from window import Window

class Top_section(Day, Month, Window):
    def __init__(self):
        self.window = super().window
        self.look_feel_settings = super().look_feel_settings

    def raise_selected_month(self, event):
        selected_month = self.selected_month_str.get()
        self.update_selected_month(selected_month)
        selected_frame3 = self.months_frames_ready[selected_month].frame3
        selected_frame3.tkraise()

        # Pass currently selected month to Window class
        Window.selected_day = 1
        self.pass_top_right_section().config(text=f"{Window.selected_day} {Window.selected_month} {Window.selected_year}")

        print(f"Selected (month chosen): {Window.selected_day}. {Window.selected_month}. {Window.selected_year}")

        # Trigger displaying data for the day clicked
        self.update_side_section_data()

    def update_selected_month(self, new_month):
        Window.selected_month = new_month

    # Save data to database
    def save_data(self):
        item_name = self.f2_item_bought_input.get()
        item_price = self.f2_amount_spent_input.get()
        item_remark = self.f2_remark_input.get()
        day_id = Window.selected_day
        month_id = Window.selected_month

        if self.validate_data(item_name, item_price, item_remark):
            # Update DayItem database
            Day.insert_dayitem_to_db(self, day_id, month_id, item_name, item_price, item_remark)

            # Update MonthItem database
            Month.handle_month_input(self, item_price)

            # Trigger displaying updated data in Side_section
            self.update_side_section_data()

            # Trigger displaying updated data for each Day element

    def update_side_section_data(self):
        side_section = Side_section(Window.selected_day, Window.selected_month, Window.selected_year)
        side_section.init_and_display_all()
        side_section.display_data_in_frame4()

    def validate_data(self, item_name, item_price, item_remark):
        if item_name != "" and item_price != "" and item_remark != "":
            if item_price.isdigit():
                if not item_name.isdigit():
                    if not item_remark.isdigit():
                        return True
                    else:
                        messagebox.showinfo(self.window, message="Remark must be a text.")
                else:
                    messagebox.showinfo(self.window, message="Item bought must be a text.")
            else:
                messagebox.showinfo(self.window, message="Amount spent must be a number.")
        else:
            messagebox.showerror(self.window, message="Text fields cannot be empty")
    
    def clear_entries(self):
        self.f2_item_bought_input.delete(0, END)
        self.f2_amount_spent_input.delete(0, END)
        self.f2_remark_input.delete(0, END)
        
    def display_frame2(self, months, months_frames_ready, pass_top_right_section):
        # Passed to object level to be used by raise_selected_month function
        self.months_frames_ready = months_frames_ready

        self.pass_top_right_section = pass_top_right_section

        self.selected_month_str = StringVar(self.window, Window.curr_month)

        # Frame 2 - for Frame 1, Item bought, Amount spent and Remark
        frame2 = Frame(self.window, bg=self.look_feel_settings["dark_blue"])
        frame2.grid(row=0, column=0, pady=(15, 10), sticky="nswe")
        frame2.columnconfigure((1, 2, 3, 4, 5, 6, 7, 8), weight=1)
        frame2.rowconfigure(0, weight=1)

        # Frame 1 (month) section
        frame1 = Frame(frame2)
        frame1.grid(row=0, column=0, padx=(25, 50), sticky="w")
        f1_months_dropdown = OptionMenu(frame1, self.selected_month_str, *months, command=self.raise_selected_month)
        f1_months_dropdown.grid(row=0, column=0, padx=(0, 5))

        # Year section
        year_text = StringVar(frame1, "2024")
        year_dropdown = OptionMenu(frame1, year_text, "2024")
        year_dropdown.grid(row=0, column=1)

        # Item bought section
        f2_item_bought_label = Label(frame2, text="Item bought", fg="white", bg=self.look_feel_settings["dark_blue"])
        f2_item_bought_label.grid(row=0, column=1, sticky="e")
        self.f2_item_bought_input = Entry(frame2, fg="white",  highlightbackground=self.look_feel_settings["dark_blue"], bg=self.look_feel_settings["lighter_blue"])
        self.f2_item_bought_input.grid(row=0, column=2, sticky="w")

        # Amount spent section
        f2_amount_spent_label = Label(frame2, text="Amount spent", fg="white", bg=self.look_feel_settings["dark_blue"])
        f2_amount_spent_label.grid(row=0, column=3, sticky="e")
        self.f2_amount_spent_input = Entry(frame2, fg="white",  highlightbackground=self.look_feel_settings["dark_blue"], bg=self.look_feel_settings["lighter_blue"], width=10)
        self.f2_amount_spent_input.grid(row=0, column=4, sticky="w")

        # Remark section
        f2_remark_label = Label(frame2, text="Remark", fg="white", bg=self.look_feel_settings["dark_blue"])
        f2_remark_label.grid(row=0, column=5, sticky="e")
        self.f2_remark_input = Entry(frame2, fg="white",  highlightbackground=self.look_feel_settings["dark_blue"], bg=self.look_feel_settings["lighter_blue"])
        self.f2_remark_input.grid(row=0, column=6, sticky="w")

        # Save button
        f2_save_btn = Button(frame2, text="Save", bg=self.look_feel_settings["dark_blue"], command=self.save_data)
        f2_save_btn.grid(row=0, column=7)
