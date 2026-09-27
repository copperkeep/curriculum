import unittest

class Cart:
    def __init__(self):
        self.items = {}

    def add(self, name, qty=1):
        self.items[name] = self.items.get(name, 0) + qty

    def count(self):
        return sum(self.items.values())

class TestCart(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.add("apple", 2)

    def test_add_same(self):
        self.cart.add("apple")
        self.assertEqual(self.cart.count(), 3)

    def test_add_new(self):
        self.cart.add("pear")
        self.assertEqual(self.cart.count(), 3)
        self.assertEqual(len(self.cart.items), 2)
