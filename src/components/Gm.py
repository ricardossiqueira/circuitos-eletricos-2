from src.components.Matrix import Matrix


class Gm(Matrix):

    def __init__(self, size):
        super().__init__(size)

    def drop_ground(self):
        return self.matrix[1:, 1:]
