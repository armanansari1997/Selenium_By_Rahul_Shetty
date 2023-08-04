import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_greet1():
    greet = "Hello"
    assert greet == "Hi", "Test failed because string do not match"
