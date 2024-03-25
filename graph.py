import matplotlib.pyplot as plt
import numpy as np

class Graph:

    def __init__(self, days_count):
        self.x_axis = []
        self.y_axis = []
        self.days_count = days_count

    def collect_data(self):
        self.x_axis = range(1, self.days_count)
        self.y_axis = range(1, self.days_count)

    def generate_graph_image(self):
        plt.figure(figsize=(3.4, 2.5))
        plt.stem(self.x_axis, self.y_axis)
        self.fig = plt.gcf()