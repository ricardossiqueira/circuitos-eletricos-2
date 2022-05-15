from operator import attrgetter
import numpy as np

from .Gm import Gm
from .Im import Im
from .Resistor import Resistor
from .Current import Current
from .functions import file_handler


# parse each component to it's own class
def new_component(arr):
    if 'R' in arr[0]:
        return Resistor(arr)
    elif 'I' in arr[0]:
        return Current(arr)


def main(file_name):

    # read file
    _, contents_split = file_handler(file_name)

    # remove comments
    no_comments = [line for line in contents_split if '*' not in line]

    # remove empty strings
    while ('' in no_comments):
        no_comments.remove('')

    # split component in a list of lists
    circuit_matrix = [line.split(' ') for line in no_comments]

    # returns list of component classes
    circuit_matrix = [new_component(component) for component in circuit_matrix]

    # return highest node in the netlist
    max_node_0 = max(circuit_matrix, key=attrgetter('node_0')).node_0
    max_node_1 = max(circuit_matrix, key=attrgetter('node_1')).node_1
    matrix_size = max(max_node_0, max_node_1) + 1

    # init matrices
    G_matrix = Gm([matrix_size, matrix_size])
    I_matrix = Im([matrix_size, 1])

    # add component to matrix using component's own stamp method
    for component in circuit_matrix:
        if component._type == 'resistor':
            G_matrix.add_component(component.stamp_function)
        elif component._type == 'current':
            I_matrix.add_component(component.stamp_function)

    # voltage vector
    e = np.linalg.solve(G_matrix.drop_ground(), I_matrix.drop_ground())

    return e
