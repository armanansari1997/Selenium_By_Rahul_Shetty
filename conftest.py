import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executed at last")


@pytest.fixture()
def data_load():
    print("User Profile Data is being created")
    return ["Arman","Ansari","armanansari.com"]