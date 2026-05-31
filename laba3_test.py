import unittest
import os
from labara3 import process_tree_file

class TestButterflyTree(unittest.TestCase):

    def setUp(self):
        self.test_filename = "temp_tree_test.txt"
        with open(self.test_filename, 'w') as f:
            post_order_data = "# # 62 # # 91 76 # # 18 # # 44 29 50"
            f.write(post_order_data)

    def tearDown(self):
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_tree_drawing(self):
        root = process_tree_file(self.test_filename)
        
        self.assertIsNotNone(root)
        
        self.assertEqual(root.value, 50)
        self.assertEqual(root.left.value, 76)
        self.assertEqual(root.right.value, 29)
        
        self.assertEqual(root.left.left.value, 62)
        self.assertEqual(root.left.right.value, 91)
        
        self.assertEqual(root.right.left.value, 18)
        self.assertEqual(root.right.right.value, 44)

if __name__ == '__main__':
    unittest.main(verbosity=2)