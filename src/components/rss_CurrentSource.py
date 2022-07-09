from src.components.rss_Component import Component
import numpy as np


class CurrentSource(Component):
    '''
        node_0 = drain
        node_1 = inject
        mode = font operating mode
        i = current value
    '''

    def __init__(self, arr):
        self.mode = arr[3]
        self.i = int(arr[4])
        super().__init__(_type='current',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2])

    def Istamp_function(self, Im):
        Im = Im.get()
        Im[self.node_0] -= self.i
        Im[self.node_1] += self.i
        return Im


class CurrentSourceControlledByVoltage(Component):
    '''
        node_0 = drain
        node_1 = inject
        control_0 = positive control
        control_1 = negative control
        value = transcondutancy value
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

    def Gstamp_function(self, Gm):
        Gm = Gm.get()
        Gm[self.node_0, self.control_0] += self.gain
        Gm[self.node_1, self.control_0] -= self.gain
        Gm[self.node_0, self.control_1] -= self.gain
        Gm[self.node_1, self.control_1] += self.gain

        return Gm


class CurrentSourceControlledByCurrent(Component):
    '''
        node_0 = drain
        node_1 = inject
        control_0 = positive control
        control_1 = negative control
        gain = current gain
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

        expanded_Gm[self.ix, self.control_0] -= 1
        expanded_Gm[self.ix, self.control_1] += 1

        expanded_Gm[self.node_0, self.ix] += self.gain
        expanded_Gm[self.node_1, self.ix] -= self.gain

        expanded_Gm[self.control_0, self.ix] += 1
        expanded_Gm[self.control_1, self.ix] -= 1

        return expanded_Gm
