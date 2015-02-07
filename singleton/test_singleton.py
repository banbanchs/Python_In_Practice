import pytest
from .singleton import App


@pytest.fixture
def first():
    app = App()
    return app

@pytest.fixture
def second():
    app = App()
    return app

def test_id(first, second):
    assert id(first) == id(second)

def test_change_value(first, second):
    first.a = 3
    assert first.a == second.a == 3
