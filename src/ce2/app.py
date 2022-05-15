from operator import attrgetter
import numpy as np

from ce2.classes.Gm import Gm
from ce2.classes.Im import Im
from ce2.classes.Resistor import Resistor
from ce2.classes.Current import Current
from ce2.functions.file_handler import file_handler

# read file
file, contents_split = file_handler('netlist0.txt')

# remove comments
no_comments = [line for line in contents_split if '*' not in line]

# remove empty strings
while ('' in no_comments):
    no_comments.remove('')

# split component in a list of lists
circuit_matrix = [line.split(' ') for line in no_comments]


# parse each component to it's own class
def new_component(arr):
    if 'R' in arr[0]:
        return Resistor(arr)
    elif 'I' in arr[0]:
        return Current(arr)


# returns list of component classes
circuit_matrix = [new_component(component) for component in circuit_matrix]

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

e = np.linalg.solve(G_matrix.drop_ground(), I_matrix.drop_ground())

print(e)
