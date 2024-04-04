from tkinter import *
import tkinter.ttk as tk
from components.window import Window
from database.database import Database
from components.graph import Graph
from PIL import ImageTk, Image

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

    def fetch_frame5_data0(self):
        Database.__init__(self, self.db_file)
        daily_total_spent_db = Database.fetch_monthitem_total_daily_spent(self, self.selected_day, self.selected_month)

        # Check if daily_total_spent for the day is empty:
        if not daily_total_spent_db:
            return ""
        else:
            return f"Total spent today: €{daily_total_spent_db[0][0]}"

    def fetch_frame5_data1(self):
        Database.__init__(self, self.db_file)
        remaining_balance_today_db = Database.fetch_monthitem_remaining_balance(self, self.selected_day, self.selected_month)

        # Check if daily_total_spent for the day is empty:
        if not remaining_balance_today_db:
            return ""
        else:
            return f"Remaining balance today: €{remaining_balance_today_db[0][0]}"

    def display_frame4_data(self):
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

    def display_frame5_data(self):
        data0 = self.fetch_frame5_data0()
        data1 = self.fetch_frame5_data1()
        self.total_spent_today_label.config(text=f"{data0}")
        self.rem_balance_today_label.config(text=f"{data1}")

    # Initiate everything inside Frame 7
    def initiate_frame7(self):
        self.frame7 = Frame(self.window, bg=self.look_feel_settings["dark_blue"])
        self.frame7.columnconfigure((0, 1, 2), weight=1)
        self.frame7.rowconfigure((0, 1, 2), weight=3)

    # Initiate everything inside Frame 6
    def initiate_frame6(self):
        self.frame6 = Canvas(self.frame7)

    # Initiate everything inside Frame 5
    def initiate_frame5(self):
        self.frame5 = Frame(self.frame7, bd=0, bg=self.look_feel_settings["dark_blue"])
        self.total_spent_today_label = Label(self.frame5, bg=self.look_feel_settings["dark_blue"], fg="white", font=("Verdana", 15))
        self.rem_balance_today_label = Label(self.frame5, bg=self.look_feel_settings["dark_blue"], fg="white", font=("Verdana", 15))

    # Initiate everything inside Frame 4
    def initiate_frame4(self):
        self.frame4 = Frame(self.frame7, bd=0, bg=self.look_feel_settings["dark_blue"], height=30, width=20)
        self.frame4.grid_propagate(1)
        self.item_bought_label = Label(self.frame4, text="Item name", fg="white", bg=self.look_feel_settings["dark_blue"])
        self.amount_spent_label = Label(self.frame4, text="Item price (€)", fg="white", bg=self.look_feel_settings["dark_blue"])
        self.remark_label = Label(self.frame4, text="Remark", fg="white", bg=self.look_feel_settings["dark_blue"])

    # Display Frame 7
    def display_frame7(self):
        self.frame7.grid(column=1, row=1, sticky="nswe", rowspan=2)

    # Display everything inside Frame 6
    def display_frame6(self):
        graph_data = self.fetch_db_graph_data()

        if not graph_data:
            print('No graph data.')
        else:
            # Generate graph image
            self.handle_graph(graph_data)

            # Display graph image inside frame6
            self.frame6.grid(column=0, row=2)

            # Draw the graph
            from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
            canvas = FigureCanvasTkAgg(self.graph.fig, master=self.frame6)
            canvas.draw()
            canvas.get_tk_widget().grid(column=0, row=0)

    # Display everything inside Frame 5
    def display_frame5(self):
        self.frame5.grid(column=0, row=1, sticky="")
        self.total_spent_today_label.grid(column=0, row=0)
        self.rem_balance_today_label.grid(column=0, row=1)
    
    # Display everything inside Frame 4
    def display_frame4(self):
        self.frame4.grid(column=0, row=0, sticky="n", columnspan=3)
        #self.frame4.grid_propagate(False)
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

    def fetch_db_graph_data(self):
        Database.__init__(self, self.db_file)
        selected_month = Window.selected_month
        unordered_data = Database.fetch_monthitem_for_graph(self, selected_month)
        
        return unordered_data

    def handle_graph(self, graph_data):
        selected_month = Window.selected_month
        days_count_to_plot = Window.months[selected_month]

        # Create instance of Graph class
        self.graph = Graph(days_count_to_plot)

        # Pass graph data
        self.graph.collect_data(graph_data)

        # Display graph 
        self.graph.display_graph()

        #self.graph.close_graph()