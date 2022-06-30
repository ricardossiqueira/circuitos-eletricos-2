from components.Component import Component


# TODO: CHECK INDUCTOR CLASS
# TODO: IMPLEMENT INDUCTOR INITIAL CONDITIONS
class SinusoidalInductor(Component):
    '''
        node_0 = drain            \\
        node_1 = inject           \\
        L = inductance value      \\
        cond = initial conditions \\
        omega = angular frequency
    '''

    def __init__(self, arr):
        self.L = int(arr[3])
        self.cond = int(arr[4])
        self.omega = int(arr[5])
        super().__init__(_type='sinusoidal_inductor',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2])

        self.impedance = 1 / (self.L * 1j * self.omega)

    def get(self):
        return self.label, self.node_0, self.node_1, self.L

    def stamp_function(self, Gm):
        Gm = Gm.get()
        Gm[self.node_0, self.node_0] += self.impedance
        Gm[self.node_0, self.node_1] -= self.impedance
        Gm[self.node_1, self.node_0] -= self.impedance
        Gm[self.node_1, self.node_1] += self.impedance
        return Gm
