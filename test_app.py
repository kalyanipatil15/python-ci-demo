import unittest
from correct import add
from buggy import multiply

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

if __name__ == "__main__":
    unittest.main()
