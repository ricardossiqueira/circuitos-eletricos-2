import numpy as np
import pytest
from app.main import main
from trab1ricardosiqueira import main as trab1_main

netlists_test = [
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
]


@pytest.mark.parametrize("test_input, expected, test_result", netlists_test)
def test_trab1ricardosiqueira_is_healthy(test_input, expected, test_result):
    assert np.testing.assert_array_almost_equal(trab1_main(test_input),
                                                expected) is test_result


@pytest.mark.parametrize("test_input, expected, test_result", netlists_test)
def test_netlist_returns_right_result(test_input, expected, test_result):
    assert np.testing.assert_array_almost_equal(main(test_input),
                                                expected) is test_result


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
