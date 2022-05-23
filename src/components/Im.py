from src.components.Matrix import Matrix


class Im(Matrix):

    def __init__(self, size):
        super().__init__(size)

    def drop_ground(self):
        return self.matrix[1:]
