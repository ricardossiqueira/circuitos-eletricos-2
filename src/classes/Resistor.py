from classes.Component import Component


class Resistor(Component):

    def __init__(self, arr):
        self.R = int(arr[3])
        super().__init__(_type='resistor',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2])

    def get(self):
        return self.label, self.node_0, self.node_1, self.R

    def stamp_function(self, G):
        G = G.get()
        G[self.node_0, self.node_0] += 1 / self.R
        G[self.node_0, self.node_1] -= 1 / self.R
        G[self.node_1, self.node_0] -= 1 / self.R
        G[self.node_1, self.node_1] += 1 / self.R
        return G
