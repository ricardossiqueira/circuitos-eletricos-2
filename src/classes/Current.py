from classes.Component import Component


class Current(Component):

    def __init__(self, arr):
        self.mode = arr[3]
        self.i = int(arr[4])
        super().__init__(_type='current',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2])

    def get(self):
        return self.label, self.node_0, self.node_1, self.mode, self.i

    def stamp_function(self, I):
        I = I.get()
        I[self.node_0] -= self.i
        I[self.node_1] += self.i
        return I
