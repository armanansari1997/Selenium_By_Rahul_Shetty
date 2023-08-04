import pytest


# here yield is a keyword if we write anything after that line then it will execute at last

# @pytest.fixture
# def setup():
#     print("I will be executed first")
#     yield
#     print("I will be executed at last")


# def test_fixture_demo(setup):
#     print("I will execute steps in fixture demo method")

@pytest.mark.usefixtures("setup")
class TestExample:
    def test_fixture_demo1(self):
        print("I will execute steps in fixture demo method1")

    def test_fixture_demo2(self):
        print("I will execute steps in fixture demo method2")

    def test_fixture_demo3(self):
        print("I will execute steps in fixture demo method3")

    def test_fixture_demo4(self):
        print("I will execute steps in fixture demo method4")
