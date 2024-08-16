import pytest
import csv


def data_provider():
    test_data = []
    with open('./test_data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            a = int(row['a'])
            b = int(row['b'])
            expected_sum = int(row['expected_sum'])
            test_data.append((a, b, expected_sum))
    return test_data


@pytest.mark.parametrize("a, b, expected_sum", data_provider())
def test_from_file(a, b, expected_sum):
    result = a + b
    assert result == expected_sum
