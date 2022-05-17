import numpy as np
import pytest
from app.main import main
from trab1ricardosiqueira import main as trab1_main


@pytest.mark.parametrize("test_input, expected, test_result", [
    ('tests/assets/netlist0.txt',
     np.ndarray(shape=(2, 1), buffer=np.array([[10.], [8.]]),
                dtype=float), None),
])
def test_netlist_returns_right_result(test_input, expected, test_result):
    assert np.testing.assert_array_equal(main(test_input),
                                         expected) is test_result


@pytest.mark.parametrize("test_input, expected", [
    ('tests/assets/netlist0.txt',
     np.ndarray(shape=(2, 1), buffer=np.array([[10.], [7.]]), dtype=float)),
])
def test_invalid_result(test_input, expected):
    with pytest.raises(AssertionError):
        np.testing.assert_array_equal(main(test_input), expected)


@pytest.mark.parametrize("test_input", [
    ('tests/assets/netlist-1.txt'),
])
def test_invalid_netlist(test_input):
    with pytest.raises(OSError):
        main(test_input)


@pytest.mark.parametrize("test_input, expected, test_result", [
    ('tests/assets/netlist0.txt',
     np.ndarray(shape=(2, 1), buffer=np.array([[10.], [8.]]),
                dtype=float), None),
])
def test_trab1ricardosiqueira_is_healthy(test_input, expected, test_result):
    assert np.testing.assert_array_equal(trab1_main(test_input),
                                         expected) is test_result
