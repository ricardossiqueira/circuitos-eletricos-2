import numpy as np
import pytest
from src.app.rss_main import main
from trab3ricardosiqueira import main as trab3_main

netlists_test = []

trabalho_1 = [
    ('tests/assets/trabalho1/netlist0.txt',
     np.ndarray(shape=(2, 1), buffer=np.array([[10.], [8.]]),
                dtype=float), None),
    ('tests/assets/trabalho1/netlist1.txt',
     np.ndarray(shape=(2, 1),
                buffer=np.array([[3.38461538], [6.15384615]]),
                dtype=float), None),
    ('tests/assets/trabalho1/netlist2.txt',
     np.ndarray(shape=(4, 1),
                buffer=np.array([[-48.94117647058809], [-78.82352941176447],
                                 [-120.94117647058788], [-9.88235294117644]]),
                dtype=float), None),
    ('tests/assets/trabalho1/netlist3.txt',
     np.ndarray(shape=(7, 1),
                buffer=np.array([[459.9999999999993], [419.99999999999943],
                                 [819.9999999999989], [119.99999999999973],
                                 [-919.9999999999991], [-1093.3333333333321],
                                 [-1613.3333333333314]]),
                dtype=float), None),
]

trabalho_3 = [
    ('tests/assets/trabalho3/netlist0.txt',
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
    ('tests/assets/trabalho3/netlist1.txt',
     np.ndarray(shape=(5, 1),
                buffer=np.array([
                    [10.0],
                    [10.0],
                    [10.0],
                    [0.0],
                    [-10.0],
                ]),
                dtype=float), None),
    ('tests/assets/trabalho3/netlist2.txt',
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
    ('tests/assets/trabalho3/netlist3.txt',
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
    assert np.testing.assert_array_almost_equal(
        trab3_main(test_input), expected, decimal=3) is test_result


@pytest.mark.parametrize("test_input, expected, test_result", netlists_test)
def test_netlist_returns_right_result(test_input, expected, test_result):
    assert np.testing.assert_array_almost_equal(
        main(test_input), expected, decimal=3) is test_result


@pytest.mark.parametrize("test_input, expected", [
    ('tests/assets/trabalho1/netlist0.txt',
     np.ndarray(shape=(2, 1), buffer=np.array([[10.], [7.]]), dtype=float)),
])
def test_invalid_result(test_input, expected):
    with pytest.raises(AssertionError):
        np.testing.assert_array_almost_equal(main(test_input), expected)


@pytest.mark.parametrize("test_input", [
    ('tests/assets/trabalho1/INVALID_NETLIST.txt'),
])
def test_invalid_netlist(test_input):
    with pytest.raises(OSError):
        main(test_input)
