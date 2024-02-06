from tkinter import *
from tkinter import ttk


app = Tk()
app.geometry("500x750")

btn = ttk.Button(app, text="test btn")
btn.grid()

app.mainloop()