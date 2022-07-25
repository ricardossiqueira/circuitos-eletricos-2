from src.components.rss_Component import Component


class Diode(Component):
    '''
      node_0 = drain\\
      node_1 = inject\\
      Is = saturation current\\
      nVt = thermal voltage
    '''

    def __init__(self, arr):
        super().__init__(_type='diode',
                         label=arr[0],
                         node_0=arr[1],
                         node_1=arr[2])
        self.Is = float(arr[3])
        self.nVt = float(arr[4])
