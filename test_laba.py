import unittest
from laba2 import min_eating_speed

class TestGorillaJackie(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(min_eating_speed([3, 6, 7, 11], 8), 4)

    def test_example_2(self):
        self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 5), 30)

    def test_example_3(self):
        self.assertEqual(min_eating_speed([30, 11, 23, 4, 20], 6), 23)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)