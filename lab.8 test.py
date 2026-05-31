import unittest
from laba8 import find_max_chain_with_bucket_sort

class TestWchainBucket(unittest.TestCase):

    def test_example_1(self):
        words = ["crates", "car", "cats", "crate", "rate", "at", "ate", "tea", "rat", "a"]
        self.assertEqual(find_max_chain_with_bucket_sort(words), 6)

    def test_example_2(self):
        words = ["b", "bcad", "bca", "bad", "bd"]
        self.assertEqual(find_max_chain_with_bucket_sort(words), 4)

    def test_example_3(self):
        words = ["word", "anotherword", "yetanotherword"]
        self.assertEqual(find_max_chain_with_bucket_sort(words), 1)

    def test_empty_list(self):
        words = []
        self.assertEqual(find_max_chain_with_bucket_sort(words), 0)

    def test_max_length_word(self):
        long_word = "a" * 50
        words = [long_word]
        self.assertEqual(find_max_chain_with_bucket_sort(words), 1)

if __name__ == "__main__":
    unittest.main()