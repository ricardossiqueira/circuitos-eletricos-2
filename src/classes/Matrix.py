import numpy as np


class Matrix:

    def __init__(self, size):
        self.matrix = np.zeros(size)

    def get(self):
        return self.matrix

    def add_component(self, stamp_function):
        self.matrix = stamp_function(self)
