import pytest


def data_provider():
    return [
        (1, 2, 3),
        (4, 5, 9),
        (10, -5, 5)
    ]


@pytest.mark.parametrize("a, b, expected_sum", data_provider())
def test_parametrized_addition(a, b, expected_sum):
    result = a + b
    assert result == expected_sum
