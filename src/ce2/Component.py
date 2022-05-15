'''
Generic component class
'''


class Component:

    def __init__(self, _type, label, node_0, node_1):
        self._type = _type
        self.label = label
        # drain node
        self.node_0 = int(node_0)
        # injector node
        self.node_1 = int(node_1)

    def stamp_function(self, Gm):
        return Gm
