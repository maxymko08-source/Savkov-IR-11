import unittest

from lab1 import find_kth_largest

class TestQuickselect(unittest.TestCase):
    
    def test_find_k_largest(self):
        self.assertEqual(find_kth_largest([5, 14, 8, 21, 18, 34], 4), (14, 1))


if __name__ == '__main__':    
    test_mas = [5, 14, 8, 21, 18, 34]
    test_k = 4
    val, idx = find_kth_largest(test_mas, test_k)
    print(f"Вхідний масив: {test_mas} Задане k: {test_k} Знайдений {test_k}-й найбільший елемент: {val} Позиція {test_k}-го найбільшого елемента в масиві: {idx}")
    
    unittest.main()
