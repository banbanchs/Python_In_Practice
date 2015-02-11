import pytest
from .bag import Bag


@pytest.fixture
def bag():
    b = Bag([1, 2, 3, 4, 5, 6, 2, 3, 1, 5, 2, 3, 1, 2, 1, 3, 2, 1])
    # {1: 5, 2: 5, 3: 4, 5: 2, 4: 1, 6: 1}
    return b


def test_bag_add_item(bag):
    num_one = bag.count(1)
    assert num_one, 5
    bag.add(1)
    assert bag.count(1), 6


def test_bag_del_item(bag):
    num_one = bag.count(3)
    assert num_one, 4
    del bag[3]
    assert bag.count(3), 3


def test_item_in_bag(bag):
    assert 3 in bag
    assert 7 not in bag


def test_bag_iter(bag):
    num = 0
    for i in bag:
        num += 1
    assert num == len(bag)
