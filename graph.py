import matplotlib.pyplot as plt
import numpy as np

class Graph:

    def __init__(self, days_count):
        self.x_axis = []
        self.y_axis = []
        self.days_count = days_count

    def collect_data(self, graph_data):
        data_to_plot = []

        # Extract data from graph_data and create new list data_to_plot
        add_zero = False
        value = 0
        for day_index in range(self.days_count):
            for d in graph_data:
                if day_index+1 == d[0]:
                    value = d[1]
                    break
                else:
                    value = None

            data_to_plot.append(value)
            value = 0

        print(self.days_count)
        print(data_to_plot, " -> ", len(data_to_plot))

        self.x_axis = range(0, self.days_count)
        self.y_axis = data_to_plot

    def display_graph(self):
        plt.figure(figsize=(3.4, 2.5))
        plt.stem(self.x_axis, self.y_axis, linefmt='#193c67', markerfmt='#193c67', basefmt="#193c67")  # Adjust line and marker formats
        plt.tight_layout(pad=0.4)  # Adjust layout
        self.fig = plt.gcf()

    def close_graph(self):
        plt.close(self.fig)