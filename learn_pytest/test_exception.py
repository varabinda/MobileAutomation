import pytest


def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        1 / 1
