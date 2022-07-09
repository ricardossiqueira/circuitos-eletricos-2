from src.components.rss_Component import Component


class Resistor(Component):
    '''
        node_0 = drain
        node_1 = inject
        R = resistance value
    '''

    def __init__(self, arr):
        self.R = float(arr[3])
        super().__init__(_type='resistor',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2])

    def get(self):
        return self.label, self.node_0, self.node_1, self.R

    def Gstamp_function(self, Gm):
        Gm = Gm.get()
        Gm[self.node_0, self.node_0] += 1 / self.R
        Gm[self.node_0, self.node_1] -= 1 / self.R
        Gm[self.node_1, self.node_0] -= 1 / self.R
        Gm[self.node_1, self.node_1] += 1 / self.R
        return Gm
