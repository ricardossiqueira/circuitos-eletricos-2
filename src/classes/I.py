from classes.Matrix import Matrix


class I(Matrix):

    def __init__(self, size):
        super().__init__(size)

    def drop_ground(self):
        return self.matrix[1:]
