from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from datetime import datetime
import database

db = database.Database("data.db")

def validate_data():
    date = date_input.get()
    item_bought = item_bought_input.get()
    amount_spent = amount_spent_input.get()

    if date != "" and item_bought != "" and amount_spent != "":
        if amount_spent.isdigit():
            if not item_bought.isdigit():
                submit_data(date, item_bought, int(amount_spent))
            else:
                messagebox.showinfo(RootWindow, message="Item bought must be a text.")
        else:
            messagebox.showinfo(RootWindow, message="Amount spent must be a number.")
    else:
        messagebox.showerror(RootWindow, message="Text fields cannot be empty")

initial_rem_balance = 2000
def get_remaining_balance(all_records_list, amount_spent):
    global initial_rem_balance

    # If DB is empty, initial rem. balance is 2000
    if all_records_list == []:
        return initial_rem_balance - amount_spent
    else:
        pass

def submit_data(date, item_bought, amount_spent):
    all_records_list = fetch_data()
    rem_balance = get_remaining_balance(all_records_list, amount_spent)
    db.insert(date, item_bought, amount_spent, rem_balance)
    print(all_records_list)

    # Refresh data in GUI
    display_data()
    
def fetch_data():
    fetched_data = db.fetch()
    all_records_list = []
    
    for col in fetched_data:
        all_records_list.append(col)
    
    return all_records_list

def display_data():
    all_records_list = fetch_data()
    clear_entries()

    if all_records_list != []:
        # Clear ListBox and insert into GUI
        recordsListBox.delete(0, END)
        for record in all_records_list:
            recordsListBox.insert(END, record)

        # Remaining balance
        rem_balance = all_records_list[-1][-1]
        remaining_balance_label_value.config(text=rem_balance)
    
    else:
        recordsListBox.delete(0, END)

def select_item(event):
    all_records_list = fetch_data()

    try:
        recordsListBox.curselection()[0]
    except IndexError:
        print("Tuple empty, nothing selected.")
        return
    else:
        selected_item_id = recordsListBox.curselection()[0]
        global actual_db_id
        actual_db_id = all_records_list[selected_item_id][0]

        # Fill selected data into entries
        selected_data = recordsListBox.get(selected_item_id)
        date_input.delete(0, END)
        date_input.insert(END, selected_data[1])
        item_bought_input.delete(0, END)
        item_bought_input.insert(END, selected_data[2])
        amount_spent_input.delete(0, END)
        amount_spent_input.insert(END, selected_data[3])

def update_data(event):
    all_records_list = fetch_data()
    ## add additional syntax check + if not empty!
    try:
        actual_db_id
    except NameError:
        messagebox.showerror(title="Error", message="Nothing is selected")
    else:
        new_date = date_input.get()
        new_item_bought = item_bought_input.get()
        new_amount_spent = amount_spent_input.get()
        new_remaining_balance = get_remaining_balance(all_records_list, int(new_amount_spent))
        db.update(actual_db_id, new_date, new_item_bought, new_amount_spent, new_remaining_balance)
        
        # Refresh data in GUI
        display_data()

def delete_data_check():
    try:
        actual_db_id
    except NameError:
        messagebox.showerror(title="Error", message="Nothing is selected")
    else:
        call_delete_data = lambda event: delete_data(event, actual_db_id)
        messagebox.askquestion(title="You sure?", message="Sure you wanna delete it?", type="yesno", command=call_delete_data)

def delete_data(event, actual_db_id):
    if event == "yes":
        db.delete(actual_db_id)

        # Refresh data in GUI
        display_data()
    else:
        return

def clear_entries():
    date_input.delete(0, END)
    item_bought_input.delete(0, END)
    amount_spent_input.delete(0, END)

def get_calendar_data(event):
    curr_date = datetime.now()
    final_text = f'{curr_date.day}.{curr_date.month}.{curr_date.year}'
    date_input.delete(0, END)
    date_input.insert(0, final_text)

RootWindow = Tk()

# Frame1
frame1 = Frame(RootWindow)
frame1.grid()

# Date
date_label = Label(frame1, text="Date")
date_label.grid(column=0, row=0)

date_input = Entry(frame1)
date_input.grid(column=0, row=1)
date_input.bind("<Button-1>", get_curr_date)

# Item bought
item_bought_label = Label(frame1, text="Item(s) bought")
item_bought_label.grid(column=1, row=0)

item_bought_input = Entry(frame1)
item_bought_input.grid(column=1, row=1)

# Amount spent
amount_spent_label = Label(frame1, text="Amount spent (€)")
amount_spent_label.grid(column=2, row=0)

amount_spent_input = Entry(frame1)
amount_spent_input.grid(column=2, row=1)

# Submit button
submit_button = Button(frame1, text="Submit", command=validate_data)
submit_button.grid(column=4, row=1)

# Update button
update_button = Button(frame1, text="Update")
update_button.bind("<Button-1>", update_data)
update_button.grid(column=5, row=1)

# Delete button
delete_button = Button(frame1, text="Delete", command=delete_data_check)
delete_button.grid(column=6, row=1)

# Frame 2
frame2 = Frame(RootWindow)
frame2.grid()

# List box with records
recordsListBox = Listbox(frame2, width=75, height=20, border=0)
recordsListBox.grid(row=2)
recordsListBox.bind("<<ListboxSelect>>", select_item)

remaining_balance_label = Label(frame2, text="Remaining balance: ")
remaining_balance_label.grid(column=0, row=5)
remaining_balance_label_value = Label(frame2, text="")
remaining_balance_label_value.grid(column=1, row=5)

# Initially display data in GUI
display_data()

RootWindow.title("Expenses tracker")
RootWindow.geometry("1000x750")

RootWindow.mainloop()