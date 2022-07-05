from cmath import rect, pi
from src.components.rss_Component import Component


class DCCurrentSource(Component):
    '''
        node_0 = drain             \\
        node_1 = inject            \\
        mode = font operating mode \\
        i = current value
    '''

    def __init__(self, arr):
        self.mode = arr[3]
        self.i = int(arr[4])
        super().__init__(_type='current',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2])

    def get(self):
        return self.label, self.node_0, self.node_1, self.mode, self.i

    def stamp_function(self, Im):
        Im = Im.get()
        Im[self.node_0] -= self.i
        Im[self.node_1] += self.i
        return Im


class CurrentSourceControlledByVoltage(Component):
    '''
        node_0 = drain                \\
        node_1 = inject               \\
        control_0 = positive control  \\
        control_1 = negative control  \\
        value = transcondutancy value
    '''

    def __init__(self, arr):
        self.control_0 = int(arr[3])
        self.control_1 = int(arr[4])
        self.value = int(arr[5])
        super().__init__(_type='transconductor',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2])

    def get(self):
        return self.label, self.node_0, self.node_1, self.control_0, self.control_1, self.value

    def stamp_function(self, Gm):
        Gm = Gm.get()
        Gm[self.node_0, self.control_0] += self.value
        Gm[self.node_1, self.control_0] -= self.value
        Gm[self.node_0, self.control_1] -= self.value
        Gm[self.node_1, self.control_1] += self.value

        return Gm


class SinusoidalCurrentSource(Component):
    '''
        node_0 = drain             \\
        node_1 = inject            \\
        mode = font operating mode \\
        DC = DC value              \\
        A = amplitude value        \\
        f = frequency value        \\
        phi = phase value
    '''

    def __init__(self, arr):
        self.mode = arr[3]
        self.DC = int(arr[4])
        self.A = int(arr[5])
        self.f = float(arr[6])
        self.phi = int(arr[7])
        super().__init__(_type='current',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2])

        # phase in radians
        self.phasor = self.i = rect(self.A, self.phi * pi / 180)
        self.omega = 2 * pi * self.f

    def get(self):
        return self.label, self.node_0, self.node_1, self.mode, self.DC, self.A, self.f, self.phi

    def get_phasor(self):
        return self.phasor

    def get_omega(self):
        return self.omega

    def stamp_function(self, Im):
        Im = Im.get()
        Im[self.node_0] -= self.i
        Im[self.node_1] += self.i
        return Im
