from src.components.Component import Component


class SinusoidalCapacitor(Component):
    '''
        node_0 = drain              \\
        node_1 = inject             \\
        C = capacitance value       \\
        cond = initial conditions   \\
        omega = angular frequency
    '''

    def __init__(self, arr):
        self.C = int(arr[3])
        self.cond = int(arr[4])
        self.omega = arr[5]
        super().__init__(_type='sinusoidal_capacitor',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2])

        self.impedance = self.C * 1j * self.omega

    def get(self):
        return self.label, self.node_0, self.node_1, self.C

    def stamp_function(self, Gm):
        Gm = Gm.get()
        Gm[self.node_0, self.node_0] += self.impedance
        Gm[self.node_0, self.node_1] -= self.impedance
        Gm[self.node_1, self.node_0] -= self.impedance
        Gm[self.node_1, self.node_1] += self.impedance
        return Gm
