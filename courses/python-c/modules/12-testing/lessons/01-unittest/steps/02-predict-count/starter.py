import unittest

class T(unittest.TestCase):
    def test_a(self): pass
    def helper(self): pass
    def test_b(self): pass

print(unittest.defaultTestLoader.loadTestsFromTestCase(T).countTestCases())
