# coding=utf-8


class Bag(object):
    """
    A class for counting hashable objects. Like collections.Counter
    """
    def __init__(self, items=None):
        self.__bag = {}
        for item in items:
            self.add(item)

    def __delitem__(self, item):
        """Delete item from bag"""
        if self.__bag.get(item):
            self.__bag[item] -= 1
            if self.__bag[item] <= 0:
                del self.__bag[item]
        else:
            raise KeyError(str(item))

    def __len__(self):
        """Return the sum of all items from bag"""
        return sum(count for count in self.__bag.values())

    def __contains__(self, item):
        """Return true if `item` is in Bag, false otherwise"""
        return item in self.__bag

    def __iter__(self):
        """Return a iterator of Bag"""
        return (item for item, count in self.__bag.items()
                        for _ in range(count))

    def add(self, item):
        """Add item to bag"""
        self.__bag[item] = self.__bag.get(item, 0) + 1

    def count(self, item):
        """Return the number of `item`"""
        return self.__bag.get(item, 0)

