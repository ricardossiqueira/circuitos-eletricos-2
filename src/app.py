from operator import attrgetter
import numpy as np

from classes.G import G
from classes.I import I
from classes.Resistor import Resistor
from classes.Current import Current
from functions.file_handler import file_handler

# read file
file, contents_split = file_handler('netlist0.txt')

# remove comments
no_comments = [line for line in contents_split if not '*' in line]

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
G = G([matrix_size, matrix_size])
I = I([matrix_size, 1])

# add component to matrix using component's own stamp method
for component in circuit_matrix:
    if component._type == 'resistor':
        G.add_component(component.stamp_function)
    elif component._type == 'current':
        I.add_component(component.stamp_function)

e = np.linalg.solve(G.drop_ground(), I.drop_ground())

print(e)
