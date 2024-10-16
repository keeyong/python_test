import pytest
import avg

def test_average():
    answer = avg.compute_average([1, 2, 3, 4, 5])
    assert answer == 3.0

def test_empty_input_average():
    answer = avg.compute_average([])
    assert answer is None

