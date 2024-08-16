import pytest


@pytest.mark.test_zero_division_error
def test_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        1 / 1

