import unittest

class Cart:
    def __init__(self):
        self.items = {}

    def add(self, name, qty=1):
        self.items[name] = self.items.get(name, 0) + qty

    def count(self):
        return sum(self.items.values())

# Write TestCart with a setUp that makes a Cart holding 2 apples, and two tests:
# one that adding 1 apple gives a count of 3, and one that adding a pear
# gives a count of 3 with 2 distinct items.
