import unittest

from game import game


class MyTestCase(unittest.TestCase):
    def test_something(self):
        result = game()
        self.assertEqual(True, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
