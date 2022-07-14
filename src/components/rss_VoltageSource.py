from components.rss_Component import Component
import numpy as np


class VoltageSource(Component):
    '''
        node_0 = drain
        node_1 = inject
        mode = font operating mode
        v = voltage value
    '''

    def __init__(self, arr):
        self.mode = arr[3]
        self.v = int(arr[4])
        super().__init__(_type='voltage',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2])

    def Istamp_function(self, Im):
        self.ix = Im.get().shape[0]

        expanded_Im = np.zeros((self.ix + 1, 1))
        expanded_Im[:-1, :] = Im.get()

        expanded_Im[self.ix] -= self.v

        return expanded_Im

    def Gstamp_function(self, Gm):
        self.ix = Gm.get().shape[0]
        expanded_Gm = np.zeros((self.ix + 1, self.ix + 1))
        expanded_Gm[:-1, :-1] = Gm.get()

        expanded_Gm[self.ix, self.node_0] -= 1
        expanded_Gm[self.ix, self.node_1] += 1

        expanded_Gm[self.node_0, self.ix] += 1
        expanded_Gm[self.node_1, self.ix] -= 1

        return expanded_Gm


class VoltageSourceControlledByCurrent(Component):
    '''
        node_0 = drain
        node_1 = inject
        control_0 = positive control
        control_1 = negative control
        gain = transcondutancy gain
    '''

    def __init__(self, arr):
        super().__init__(_type='transconductor',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2],
                         node_2=arr[3],
                         node_3=arr[4])
        self.control_0 = self.node_2
        self.control_1 = self.node_3
        self.gain = float(arr[5])

    def Istamp_function(self, Im):
        self.ix = Im.get().shape[0]
        # self.iy += self.ix

        expanded_Im = np.zeros((self.ix + 2, 1))
        expanded_Im[:-2, :] = Im.get()

        return expanded_Im

    def Gstamp_function(self, Gm):
        self.ix = Gm.get().shape[0]
        self.iy = self.ix + 1

        expanded_Gm = np.zeros((self.ix + 2, self.ix + 2))
        expanded_Gm[:-2, :-2] = Gm.get()

        expanded_Gm[self.ix, self.control_0] -= 1
        expanded_Gm[self.ix, self.control_1] += 1

        expanded_Gm[self.iy, self.node_0] -= 1
        expanded_Gm[self.iy, self.node_1] += 1

        expanded_Gm[self.iy, self.ix] += self.gain

        expanded_Gm[self.control_0, self.ix] += 1
        expanded_Gm[self.control_1, self.ix] -= 1

        expanded_Gm[self.node_0, self.iy] += 1
        expanded_Gm[self.node_1, self.iy] -= 1

        return expanded_Gm


class VoltageSourceControlledByVoltage(Component):
    '''
        node_0 = drain
        node_1 = inject
        control_0 = positive control
        control_1 = negative control
        gain = voltage gain
    '''

    def __init__(self, arr):
        super().__init__(_type='transconductor',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2],
                         node_2=arr[3],
                         node_3=arr[4])
        self.control_0 = self.node_2
        self.control_1 = self.node_3
        self.gain = float(arr[5])

    def Istamp_function(self, Im):
        self.ix = Im.get().shape[0]

        expanded_Im = np.zeros((self.ix + 1, 1))
        expanded_Im[:-1, :] = Im.get()

        return expanded_Im

    def Gstamp_function(self, Gm):
        self.ix = Gm.get().shape[0]
        expanded_Gm = np.zeros((self.ix + 1, self.ix + 1))
        expanded_Gm[:-1, :-1] = Gm.get()

        expanded_Gm[self.ix, self.node_0] -= 1
        expanded_Gm[self.ix, self.node_1] += 1

        expanded_Gm[self.ix, self.control_0] += self.gain
        expanded_Gm[self.ix, self.control_1] -= self.gain

        expanded_Gm[self.node_0, self.ix] += 1
        expanded_Gm[self.node_1, self.ix] -= 1

        return expanded_Gm
