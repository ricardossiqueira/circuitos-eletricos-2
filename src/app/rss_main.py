from operator import attrgetter
import numpy as np

from components.rss_Gm import Gm
from components.rss_Im import Im
from functions.rss_file_handler import file_handler
from functions.rss_new_component import new_component
import components.rss_settings as rss_settings

rss_settings.init()


def main(netlist_file, sim_time, sim_delay, nr_lim, initial_values,
         target_nodes):

    # read file
    _, contents_split = file_handler(netlist_file)

    # remove comments
    no_comments = [line for line in contents_split if '*' not in line]

    # remove empty strings
    while ('' in no_comments):
        no_comments.remove('')

    # split component in a list of lists
    component_list = [line.split(' ') for line in no_comments]

    # returns list of component classes
    circuit_matrix = []
    for component in component_list:
        component.append(sim_time)
        component.append(sim_delay)
        component.append(nr_lim)
        component.append(initial_values)

        circuit_matrix.append(new_component(component))

    # return highest node in the netlist
    max_node_0 = max(circuit_matrix, key=attrgetter('node_0')).node_0
    max_node_1 = max(circuit_matrix, key=attrgetter('node_1')).node_1
    max_node_2 = max(circuit_matrix, key=attrgetter('node_2')).node_2
    max_node_3 = max(circuit_matrix, key=attrgetter('node_3')).node_3
    matrix_size = max(max_node_0, max_node_1, max_node_2, max_node_3) + 1

    # init matrices
    G_matrix = Gm([matrix_size, matrix_size])
    I_matrix = Im([matrix_size, 1])

    # add component to matrix using component's own stamp method
    for component in circuit_matrix:
        I_matrix.add_component(component.Istamp_function)
        G_matrix.add_component(component.Gstamp_function)

    e = [
        np.linalg.solve(G_matrix.drop_ground(),
                        I_matrix.get()[i][1:])
        for i in range(int(sim_time / sim_delay) + 1)
    ]

    res = []
    for j in target_nodes:
        aux = []
        for i in range(len(e)):
            aux.append(e[i][j - 1][0])
        res.append(aux)

    # for i in range(len(e)):
    #     aux = []
    #     for j in range(len(target_nodes)):
    #         aux.append(e[i][j][0])
    #     res.append(aux)

    # # voltage vector
    # e = np.linalg.solve(G_matrix.drop_ground(), I_matrix.drop_ground())

    return res
