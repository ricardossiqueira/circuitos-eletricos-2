'''
Generic component class
'''


class Component:
    '''
        node_0 = drain          \\
        node_1 = inject         \\
        _type = component type  \\
        label = component label
    '''

    def __init__(self, _type, label, node_0, node_1):
        self._type = _type
        self.label = label
        self.node_0 = int(node_0)
        self.node_1 = int(node_1)

    def stamp_function(self, Gm):
        return Gm
