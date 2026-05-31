import unittest
from red_black_priority_queue import RedBlackPriorityQueue

class TestRedBlackPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = RedBlackPriorityQueue()

    def test_empty_queue(self):
        self.assertIsNone(self.pq.peek(), "peek() порожньої черги має повертати None")
        self.assertIsNone(self.pq.extract_max(), "extract_max() порожньої черги має повертати None")

    def test_single_element(self):
        self.pq.insert("Один", 10)
        
        self.assertEqual(self.pq.peek(), ("Один", 10))
        
        self.assertEqual(self.pq.extract_max(), ("Один", 10))
        
        self.assertIsNone(self.pq.peek())

    def test_priority_ordering(self):
        self.pq.insert("Низький", 1)
        self.pq.insert("Високий", 100)
        self.pq.insert("Середній", 50)

        self.assertEqual(self.pq.extract_max(), ("Високий", 100))
        self.assertEqual(self.pq.extract_max(), ("Середній", 50))
        self.assertEqual(self.pq.extract_max(), ("Низький", 1))
        self.assertIsNone(self.pq.extract_max())

    def test_duplicate_priorities(self):
        self.pq.insert("Завдання А", 10)
        self.pq.insert("Завдання Б", 10)

        val1, pri1 = self.pq.extract_max()
        val2, pri2 = self.pq.extract_max()

        self.assertEqual(pri1, 10)
        self.assertEqual(pri2, 10)
        
        extracted_values = [val1, val2]
        self.assertIn("Завдання А", extracted_values)
        self.assertIn("Завдання Б", extracted_values)

    def test_original_scenario(self):

        self.pq.insert("Завдання А", 5)
        self.pq.insert("Завдання Б", 10)
        self.pq.insert("Завдання В", 1)
        self.pq.insert("Завдання Г", 10)
        self.pq.insert("Завдання Д", 7)

        self.assertEqual(self.pq.extract_max(), ("Завдання Г", 10))
        self.assertEqual(self.pq.extract_max(), ("Завдання Б", 10))
        self.assertEqual(self.pq.extract_max(), ("Завдання Д", 7))
        self.assertEqual(self.pq.extract_max(), ("Завдання А", 5))
        self.assertEqual(self.pq.extract_max(), ("Завдання В", 1))
        
        self.assertIsNone(self.pq.extract_max())


if __name__ == '__main__':
    unittest.main()