import pytest


def test_first_program():
    print("Hello")


@pytest.mark.xfail
def test_greet():
    print("Good Afternoon")