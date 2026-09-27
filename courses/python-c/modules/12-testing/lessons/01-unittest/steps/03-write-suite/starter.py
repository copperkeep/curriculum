import unittest

def slug(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return "-".join(text.lower().split())

# Write class TestSlug(unittest.TestCase) with at least three test methods:
# a normal case, an edge case, and one using assertRaises.
