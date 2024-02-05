
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from datetime import datetime
from database import Database

class Gui(Database):

    def __init__(self, db_file, title, screen):
        self.RootWindow = Tk()
        self.RootWindow.title(title)
        self.RootWindow.geometry(screen)
        super().__init__(db_file)

        self.all_records_list = []
        self.actual_db_id = 0   # maybe set it to None?
        self.initial_rem_balance = 2000

    def run_window(self):
        self.RootWindow.mainloop()

    def validate_data(self):
        date = self.date_input.get()
        item_bought = self.item_bought_input.get()
        amount_spent = self.amount_spent_input.get()

        if date != "" and item_bought != "" and amount_spent != "":
            if amount_spent.isdigit():
                if not item_bought.isdigit():
                    self.submit_data(date, item_bought, int(amount_spent))
                else:
                    messagebox.showinfo(self.RootWindow, message="Item bought must be a text.")
            else:
                messagebox.showinfo(self.RootWindow, message="Amount spent must be a number.")
        else:
            messagebox.showerror(self.RootWindow, message="Text fields cannot be empty")

    def get_remaining_balance(self, amount_spent):
        # If DB is empty, initial rem. balance is 2000
        if self.all_records_list == []:
            return self.initial_rem_balance - amount_spent
        else:
            for record in self.all_records_list:
                print("record: ", record[4])
                self.initial_rem_balance = self.initial_rem_balance - record[4]

    def submit_data(self, date, item_bought, amount_spent):
        self.all_records_list = self.fetch_data()
        rem_balance = self.get_remaining_balance(amount_spent)
        super().insert(date, item_bought, amount_spent, rem_balance)

        # Refresh data in GUI
        self.display_data()

    def fetch_data(self):
        fetched_data = super().fetch()

        self.all_records_list = []
        for col in fetched_data:
            self.all_records_list.append(col)
    
        return self.all_records_list

    def display_data(self):
        self.all_records_list = self.fetch_data()
        self.clear_entries()

        if self.all_records_list != []:
            # Clear ListBox and insert into GUI
            self.recordsListBox.delete(0, END)
            for record in self.all_records_list:
                self.recordsListBox.insert(END, record)

            # Remaining balance
            rem_balance = self.all_records_list[-1][-1]
            self.remaining_balance_label_value.config(text=rem_balance)
        
        else:
            self.recordsListBox.delete(0, END)

    def select_item(self, event):
        self.all_records_list = self.fetch_data()

        try:
            self.recordsListBox.curselection()[0]
        except IndexError:
            print("Tuple empty, nothing selected.")
            return
        else:
            selected_item_id = self.recordsListBox.curselection()[0]
            self.actual_db_id = self.all_records_list[selected_item_id][0]

            # Fill selected data into entries
            selected_data = self.recordsListBox.get(selected_item_id)
            self.date_input.delete(0, END)
            self.date_input.insert(END, selected_data[1])
            self.item_bought_input.delete(0, END)
            self.item_bought_input.insert(END, selected_data[2])
            self.amount_spent_input.delete(0, END)
            self.amount_spent_input.insert(END, selected_data[3])

    def update_data(self, event):
        #
        self.all_records_list = self.fetch_data()
        ## add additional syntax check + if not empty!
        try:
            self.actual_db_id
        except NameError:
            messagebox.showerror(title="Error", message="Nothing is selected")
        else:
            new_date = self.date_input.get()
            new_item_bought = self.item_bought_input.get()
            new_amount_spent = self.amount_spent_input.get()
            new_remaining_balance = self.get_remaining_balance(self.all_records_list, int(new_amount_spent))
            super().update(self.actual_db_id, new_date, new_item_bought, new_amount_spent, new_remaining_balance)
            
            # Refresh data in GUI
            self.display_data()

    def delete_data_check(self):
        try:
            self.actual_db_id
        except NameError:
            messagebox.showerror(title="Error", message="Nothing is selected")
        else:
            call_delete_data = lambda event: self.delete_data(event, self.actual_db_id)
            messagebox.askquestion(title="You sure?", message="Sure you wanna delete it?", type="yesno", command=call_delete_data)

    def delete_data(self, event, actual_db_id):
        self.actual_db_id = actual_db_id

        if event == "yes":
            super().delete(self.actual_db_id)

            # Refresh data in GUI
            self.display_data()
        else:
            return

    def clear_entries(self):
        self.date_input.delete(0, END)
        self.item_bought_input.delete(0, END)
        self.amount_spent_input.delete(0, END)

    def get_curr_date(self, event):
        curr_date = datetime.now()
        final_text = f'{curr_date.day}.{curr_date.month}.{curr_date.year}'
        self.date_input.delete(0, END)
        self.date_input.insert(0, final_text)

    # GUI methods
    def build_frames(self):
        self.frame1 = Frame(self.RootWindow)
        self.frame1.grid()
        self.frame2 = Frame(self.RootWindow)
        self.frame2.grid()

    def build_date(self):
        self.date_label = Label(self.frame1, text="Date")
        self.date_label.grid(column=0, row=0)

        self.date_input = Entry(self.frame1)
        self.date_input.grid(column=0, row=1)

        self.date_input.bind("<Button-1>", self.get_curr_date)

    def build_item_bought(self):
        self.item_bought_label = Label(self.frame1, text="Item(s) bought")
        self.item_bought_label.grid(column=1, row=0)

        self.item_bought_input = Entry(self.frame1)
        self.item_bought_input.grid(column=1, row=1)

    def build_amount_spent(self):
        self.amount_spent_label = Label(self.frame1, text="Amount spent (€)")
        self.amount_spent_label.grid(column=2, row=0)

        self.amount_spent_input = Entry(self.frame1)
        self.amount_spent_input.grid(column=2, row=1)

    def build_submit_button(self):
        self.submit_button = Button(self.frame1, text="Submit", command=self.validate_data)
        self.submit_button.grid(column=4, row=1)

    def build_update_button(self):
        self.update_button = Button(self.frame1, text="Update")
        self.update_button.bind("<Button-1>", self.update_data)
        self.update_button.grid(column=5, row=1)

    def build_delete_button(self):
        self.delete_button = Button(self.frame1, text="Delete", command=self.delete_data_check)
        self.delete_button.grid(column=6, row=1)

    def build_listbox(self):
        self.recordsListBox = Listbox(self.frame2, width=75, height=20, border=0)
        self.recordsListBox.grid(row=2)
        self.recordsListBox.bind("<<ListboxSelect>>", self.select_item)

    def build_remain_balance(self):
        self.remaining_balance_label = Label(self.frame2, text="Remaining balance: ")
        self.remaining_balance_label.grid(column=0, row=5)
        self.remaining_balance_label_value = Label(self.frame2, text="")
        self.remaining_balance_label_value.grid(column=1, row=5)