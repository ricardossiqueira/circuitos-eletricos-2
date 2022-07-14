import numpy as np
import pytest
from app.rss_main import main
from trab4ricardosiqueira import main as trab4_main

netlists_test = []

trabalho_1 = [
    (['tests/assets/trabalho1/netlist0.txt', 0.0, 0.0, 0.0, [],
      []], np.ndarray(shape=(2, 1),
                      buffer=np.array([[10.], [8.]]),
                      dtype=float), None),
    (['tests/assets/trabalho1/netlist1.txt', 0.0, 0.0, 0.0, [], []],
     np.ndarray(shape=(2, 1),
                buffer=np.array([[3.38461538], [6.15384615]]),
                dtype=float), None),
    (['tests/assets/trabalho1/netlist2.txt', 0.0, 0.0, 0.0, [], []],
     np.ndarray(shape=(4, 1),
                buffer=np.array([[-48.94117647058809], [-78.82352941176447],
                                 [-120.94117647058788], [-9.88235294117644]]),
                dtype=float), None),
    (['tests/assets/trabalho1/netlist3.txt', 0.0, 0.0, 0.0, [], []],
     np.ndarray(shape=(7, 1),
                buffer=np.array([[459.9999999999993], [419.99999999999943],
                                 [819.9999999999989], [119.99999999999973],
                                 [-919.9999999999991], [-1093.3333333333321],
                                 [-1613.3333333333314]]),
                dtype=float), None),
]

trabalho_3 = [
    (['tests/assets/trabalho3/netlist0.txt', 0.0, 0.0, 0.0, [], []],
     np.ndarray(shape=(6, 1),
                buffer=np.array([
                    [5.0],
                    [5.0],
                    [-15.0],
                    [-32.0],
                    [24.5],
                    [24.0],
                ]),
                dtype=float), None),
    (['tests/assets/trabalho3/netlist1.txt', 0.0, 0.0, 0.0, [], []],
     np.ndarray(shape=(5, 1),
                buffer=np.array([
                    [10.0],
                    [10.0],
                    [10.0],
                    [0.0],
                    [-10.0],
                ]),
                dtype=float), None),
    (['tests/assets/trabalho3/netlist2.txt', 0.0, 0.0, 0.0, [], []],
     np.ndarray(shape=(6, 1),
                buffer=np.array([
                    [-0.861],
                    [-16.203],
                    [-20.506],
                    [10.0],
                    [-18.873],
                    [25.506],
                ]),
                dtype=float), None),
    (['tests/assets/trabalho3/netlist3.txt', 0.0, 0.0, 0.0, [], []],
     np.ndarray(shape=(18, 1),
                buffer=np.array([
                    [-200.0],
                    [0.0],
                    [0.0],
                    [0.0],
                    [0.0],
                    [0.0],
                    [-399.633],
                    [0.0],
                    [10.0],
                    [10.0],
                    [10.0],
                    [9.184],
                    [-1905.143],
                    [-0.001],
                    [0.401],
                    [0.0],
                    [0.0],
                    [0.0],
                ]),
                dtype=float), None),
]

netlists_test.extend(trabalho_1)
netlists_test.extend(trabalho_3)


@pytest.mark.parametrize("test_input, expected, test_result", netlists_test)
def test_trabFile_is_healthy(test_input, expected, test_result):
    netlist_file, sim_uptime, nr_step, nr_lim, initial_values, target_nodes = test_input
    assert np.testing.assert_array_almost_equal(trab4_main(
        netlist_file, sim_uptime, nr_step, nr_lim, initial_values,
        target_nodes),
                                                expected,
                                                decimal=3) is test_result


@pytest.mark.parametrize("test_input, expected, test_result", netlists_test)
def test_netlist_returns_right_result(test_input, expected, test_result):
    netlist_file, sim_uptime, nr_step, nr_lim, initial_values, target_nodes = test_input
    assert np.testing.assert_array_almost_equal(
        main(netlist_file, sim_uptime, nr_step, nr_lim, initial_values,
             target_nodes),
        expected,
        decimal=3) is test_result


@pytest.mark.parametrize("test_input, expected", [
    (["tests/assets/trabalho1/netlist0.txt", 0.0, 0.0, 0.0, [], []],
     np.ndarray(shape=(2, 1), buffer=np.array([[10.], [7.]]), dtype=float)),
])
def test_invalid_result(test_input, expected):
    netlist_file, sim_uptime, nr_step, nr_lim, initial_values, target_nodes = test_input
    with pytest.raises(AssertionError):
        np.testing.assert_array_almost_equal(
            main(netlist_file, sim_uptime, nr_step, nr_lim, initial_values,
                 target_nodes), expected)


@pytest.mark.parametrize("test_input", [
    (["tests/assets/trabalho1/INVALID_NETLIST.txt", 0.0, 0.0, 0.0, [], []]),
])
def test_invalid_netlist(test_input):
    netlist_file, sim_uptime, nr_step, nr_lim, initial_values, target_nodes = test_input
    with pytest.raises(OSError):
        main(netlist_file, sim_uptime, nr_step, nr_lim, initial_values,
             target_nodes)
