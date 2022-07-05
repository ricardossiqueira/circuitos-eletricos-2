from src.components.rss_Component import Component


class SinusoidalTransformer(Component):
    '''
        node_0 = a                         \\
        node_1 = b                         \\
        node_2 = c                         \\
        node_3 = d                         \\
        L_1 = primary winding inductance   \\
        L_2 = secondary winding inductance \\
        M = mutual inductance              \\
        omega = angular frequency
    '''

    def __init__(self, arr):
        self.L_1 = float(arr[5])
        self.L_2 = float(arr[6])
        self.M = float(arr[7])
        self.omega = arr[8]
        super().__init__(_type='sinusoidal_transformer',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2],
                         node_2=arr[3],
                         node_3=arr[4])

        self.gamma_11 = self.L_2 / (self.L_1 * self.L_2 - self.M**2)
        self.gamma_22 = self.L_1 / (self.L_1 * self.L_2 - self.M**2)
        self.gamma_12 = self.gamma_21 = -self.M / (self.L_1 * self.L_2 -
                                                   self.M**2)

    def get(self):
        return self.label, self.node_0, self.node_1, self.node_2, self.node_3, self.L_1, self.L_2, self.M, self.omega

    def stamp_function(self, Gm):
        Gm = Gm.get()
        Gm[self.node_0, self.node_0] += self.gamma_11 / (1j * self.omega)
        Gm[self.node_0, self.node_1] -= self.gamma_11 / (1j * self.omega)
        Gm[self.node_1, self.node_0] -= self.gamma_11 / (1j * self.omega)
        Gm[self.node_1, self.node_1] += self.gamma_11 / (1j * self.omega)

        Gm[self.node_0, self.node_2] += self.gamma_12 / (1j * self.omega)
        Gm[self.node_0, self.node_3] -= self.gamma_12 / (1j * self.omega)
        Gm[self.node_1, self.node_2] -= self.gamma_12 / (1j * self.omega)
        Gm[self.node_1, self.node_3] += self.gamma_12 / (1j * self.omega)

        Gm[self.node_2, self.node_0] += self.gamma_21 / (1j * self.omega)
        Gm[self.node_2, self.node_1] -= self.gamma_21 / (1j * self.omega)
        Gm[self.node_3, self.node_0] -= self.gamma_21 / (1j * self.omega)
        Gm[self.node_3, self.node_1] += self.gamma_21 / (1j * self.omega)

        Gm[self.node_2, self.node_2] += self.gamma_22 / (1j * self.omega)
        Gm[self.node_2, self.node_3] -= self.gamma_22 / (1j * self.omega)
        Gm[self.node_3, self.node_2] -= self.gamma_22 / (1j * self.omega)
        Gm[self.node_3, self.node_3] += self.gamma_22 / (1j * self.omega)

        return Gm
