import pytest


def test_set_comparison():
    set1 = set("1308")
    set2 = set("8035")
    assert set1 == set2


def test_compare_dictionaries():
    dict1 = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }

    dict2 = {
        "name": "Alice",
        "age": 30,
        "city": "Los Angeles"
    }

    assert dict1 == dict2, "The dictionaries should not be equal due to different 'city' values."


def test_eq_long_text():
    a = "1" * 100 + "a" + "2" * 100
    b = "1" * 100 + "b" + "2" * 100
    assert a == b


def test_eq_multiline_text():
    assert "foo\nspam\nbar" == "foo\neggs\nbar"
