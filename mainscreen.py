from tkinter import *
import tkinter as tk
from functools import partial

window = tk.Tk()
window.geometry("1000x750")

# Trigger clicked day button
def identify_day(event, day):
    day_object_id = event
    day_number = event.cget("text")
    print(day_object_id, day_number)

def select_month(event):
    selected_month = selected_month_str.get()
    months_frames[selected_month].tkraise()



## Generate days
months = {
    "January": 31,
    "February": 28,
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

months_frames = {}
all_days_buttons = []

# every month
for index, month in enumerate(months):
    day = IntVar(window)
    day = 1
    frame = Frame(window)
    frame.grid(column=1, row=1)

    # every day
    for row in range(5):
        for col in range(7):
            day_label = Label(frame, justify="right", text=day, width=5, height=5, border=5, font=('Helvetica 18 bold italic'))
            day_label.grid(row=row, column=col)
            all_days_buttons.append(day_label)

            if day >= months[month]:
                break
            else:
                day += 1

    months_frames[month] = frame

# Bind each day to identify_day function
for day in all_days_buttons:
    day.bind("<Button-1>", partial(identify_day, day))

months_dropdown_frame = Frame(window)
months_dropdown_frame.grid(row=0, column=0)
selected_month_str = StringVar(window, "Select month")
months_dropdown = OptionMenu(months_dropdown_frame, selected_month_str, *months.keys(), command=select_month)
months_dropdown.grid()

window.mainloop()