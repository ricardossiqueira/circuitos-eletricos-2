from components.rss_Component import Component
import numpy as np


class CurrentSource(Component):
    '''
        DC mode params:\\
            node_0 = drain\\
            node_1 = inject\\
            mode = font operating mode\\
            i = current value\n
        SIN mode params:\\
            node_0 = drain\\
            node_1 = inject\\
            mode = font operating mode\\
            i = current value\\
            amplitude = amplitude of the sin wave\\
            frequency = frequency of the sin wave (in Hz)\\
            phase = phase of the sin wave (in degrees)\n
        PULSE mode params:\\
            node_0 = drain\\
            node_1 = inject\\
            mode = font operating mode\\
            i = current value\\
            v1 = first voltage level\\
            v2 = second voltage level\\
            delay = time on the voltage level v1\\
            trise = rise time in seconds\\
            tfall = fall time in seconds\\
            tv2 = time on the voltage level v2\\
            tperiod = period of the pulse in seconds
    '''

    def __init__(self, arr):
        self.mode = arr[3]
        self.i = int(arr[4])
        super().__init__(_type='current',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2])

        if self.mode == 'SIN':
            self.amplitude = arr[5]
            self.fequency = arr[6]
            self.phase = arr[7]

        if self.mode == 'PULSE':
            self.v1 = arr[5]
            self.v2 = arr[6]
            self.delay = arr[7]
            self.trise = arr[8]
            self.tfall = arr[9]
            self.tv2 = arr[10]
            self.tperiod = arr[11]

    def Istamp_function(self, Im):
        Im = Im.get()
        Im[self.node_0] -= self.i
        Im[self.node_1] += self.i
        return Im


class CurrentSourceControlledByVoltage(Component):
    '''
        node_0 = drain\\
        node_1 = inject\\
        control_0 = positive control\\
        control_1 = negative control\\
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
        node_0 = drain\\
        node_1 = inject\\
        control_0 = positive control\\
        control_1 = negative control\\
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
