import pytest
from calculator import add

@pytest.fixture
def input_data():
    return (2, 3)

def test_add(input_data):
    a, b = input_data
    assert add(a, b) == 5

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (1, 1, 2),
    (10, 15, 25)
])
def test_add_parameterized(a, b, expected):
    assert add(a, b) == expected