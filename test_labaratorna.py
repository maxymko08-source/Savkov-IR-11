import unittest
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

try:
    from labaratorna import process_matrix_file
except ImportError:
    print("\n[ПОМИЛКА] Не вдалося знайти файл labaratorna.py")
    print(f"Я шукаю тут: {current_dir}")
    print(f"Файли, які я бачу: {os.listdir(current_dir)}")
    sys.exit(1)

class TestIslandBFS(unittest.TestCase):
    def setUp(self):
        self.test_filename = "matrix_input.txt"
        matrix_content = "1 1 0\n1 1 0\n0 0 1"
        with open(self.test_filename, 'w') as f:
            f.write(matrix_content)

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_logic(self):
        result = process_matrix_file(self.test_filename)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)