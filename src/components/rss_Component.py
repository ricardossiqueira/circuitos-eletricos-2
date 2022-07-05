'''
Generic component class
'''


class Component:
    '''
        node_0 = drain                \\
        node_1 = inject               \\
        node_2 = c (transformer only) \\
        node_3 = d (transformer only) \\
        _type = component type        \\
        label = component label
    '''

    def __init__(self, _type, label, node_0, node_1, node_2=0, node_3=0):
        self._type = _type
        self.label = label
        self.node_0 = int(node_0)
        self.node_1 = int(node_1)
        self.node_2 = int(node_2)
        self.node_3 = int(node_3)

    def stamp_function(self, Gm, _omega):
        return Gm
