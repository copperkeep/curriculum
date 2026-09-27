import unittest

def slug(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return "-".join(text.lower().split())

class TestSlug(unittest.TestCase):
    def test_spaces(self):
        self.assertEqual(slug("Hello World"), "hello-world")

    def test_empty(self):
        self.assertEqual(slug(""), "")

    def test_rejects_none(self):
        with self.assertRaises(TypeError):
            slug(None)
