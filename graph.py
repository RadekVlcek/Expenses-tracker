import matplotlib.pyplot as plt
import numpy as np

class Graph:

    def __init__(self, days_count):
        self.x_axis = []
        self.y_axis = []
        self.days_count = days_count

    def collect_data(self):
        self.x_axis = range(1, self.days_count)
        self.y_axis = np.random.uniform(size=self.days_count - 1)

    def generate_graph_image(self):
        plt.stem(self.x_axis, self.y_axis)
        plt.ylim(0, 1.2)
        plt.savefig("assets/graph.png", bbox_inches='tight')