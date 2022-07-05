import numpy as np
import pytest
from src.app.rss_main import main
from trab2ricardosiqueira import main as trab2_main

netlists_test = []

trabalho_1 = [
    ('tests/assets/netlist0.txt',
     np.ndarray(shape=(2, 1), buffer=np.array([[10.], [8.]]),
                dtype=float), None),
    ('tests/assets/netlist1.txt',
     np.ndarray(shape=(2, 1),
                buffer=np.array([[3.38461538], [6.15384615]]),
                dtype=float), None),
    ('tests/assets/netlist2.txt',
     np.ndarray(shape=(4, 1),
                buffer=np.array([[-48.94117647058809], [-78.82352941176447],
                                 [-120.94117647058788], [-9.88235294117644]]),
                dtype=float), None),
    ('tests/assets/netlist3.txt',
     np.ndarray(shape=(7, 1),
                buffer=np.array([[459.9999999999993], [419.99999999999943],
                                 [819.9999999999989], [119.99999999999973],
                                 [-919.9999999999991], [-1093.3333333333321],
                                 [-1613.3333333333314]]),
                dtype=float), None),
]

trabalho_2 = [
    ('tests/assets/netlist4.txt',
     np.ndarray(shape=(3, 1),
                buffer=np.array([[3.295 + 0.202j], [3.257 + 0.51j],
                                 [3.282 + 0.41j]]),
                dtype=np.complex128), None),
    ('tests/assets/netlist5.txt',
     np.ndarray(shape=(3, 1),
                buffer=np.array([[1.473 + 2.955j], [1.187 + 3.075j],
                                 [1.286 + 3.047j]]),
                dtype=np.complex128), None),
    ('tests/assets/netlist6.txt',
     np.ndarray(shape=(2, 1),
                buffer=np.array([[99.476 + 6.62j], [0.578 - 4.943j]]),
                dtype=np.complex128), None),
    ('tests/assets/netlist7.txt',
     np.ndarray(shape=(2, 1),
                buffer=np.array([[-1.111 + 0.932j], [0.0188 - 0.016j]]),
                dtype=np.complex128), None),
]

netlists_test.extend(trabalho_1)
netlists_test.extend(trabalho_2)


@pytest.mark.parametrize("test_input, expected, test_result", netlists_test)
def test_trab1ricardosiqueira_is_healthy(test_input, expected, test_result):
    assert np.testing.assert_array_almost_equal(
        trab2_main(test_input), expected, decimal=3) is test_result


@pytest.mark.parametrize("test_input, expected, test_result", netlists_test)
def test_netlist_returns_right_result(test_input, expected, test_result):
    assert np.testing.assert_array_almost_equal(
        main(test_input), expected, decimal=3) is test_result


@pytest.mark.parametrize("test_input, expected", [
    ('tests/assets/netlist0.txt',
     np.ndarray(shape=(2, 1), buffer=np.array([[10.], [7.]]), dtype=float)),
])
def test_invalid_result(test_input, expected):
    with pytest.raises(AssertionError):
        np.testing.assert_array_almost_equal(main(test_input), expected)


@pytest.mark.parametrize("test_input", [
    ('tests/assets/netlist-1.txt'),
])
def test_invalid_netlist(test_input):
    with pytest.raises(OSError):
        main(test_input)
