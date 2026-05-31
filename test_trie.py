import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from trie import Trie, build_trie_from_patterns


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

    def test_insert_and_search_exact_match(self):
        self.trie.insert("apple")
        self.assertTrue(self.trie.search("apple"))

    def test_search_non_existent_word(self):
        self.trie.insert("apple")
        self.assertFalse(self.trie.search("app"))
        self.assertFalse(self.trie.search("orange"))

    def test_starts_with_prefix(self):
        self.trie.insert("apricot")
        self.assertTrue(self.trie.starts_with("apr"))
        self.assertTrue(self.trie.starts_with("apricot"))
        self.assertFalse(self.trie.starts_with("cat"))

    def test_empty_string(self):
        self.trie.insert("")
        self.assertTrue(self.trie.search(""))
        self.assertTrue(self.trie.starts_with(""))


class TestBuildTrieFromPatterns(unittest.TestCase):

    def test_build_trie_creates_valid_structure(self):
        patterns = ["code", "coder", "testing", "python"]
        trie = build_trie_from_patterns(patterns)

        for word in patterns:
            self.assertTrue(trie.search(word))

        self.assertTrue(trie.starts_with("cod"))
        self.assertTrue(trie.starts_with("py"))

        self.assertFalse(trie.search("test"))
        self.assertFalse(trie.starts_with("java"))


if __name__ == "__main__":
    unittest.main()