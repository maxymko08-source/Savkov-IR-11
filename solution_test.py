import unittest
from solution import get_max_flow

class TestFlowerDelivery(unittest.TestCase):
    
    def test_basic_flow(self):
        farms = ["F1"]
        shops = ["S1"]
        roads = [("F1", "S1", 10)]
        self.assertEqual(get_max_flow(farms, shops, roads), 10)

    def test_bottleneck(self):
        farms = ["F1"]
        shops = ["S1"]
        roads = [
            ("F1", "X1", 20),
            ("X1", "S1", 5)
        ]
        self.assertEqual(get_max_flow(farms, shops, roads), 5)

    def test_multiple_sources_sinks(self):
        farms = ["F1", "F2"]
        shops = ["S1", "S2"]
        roads = [
            ("F1", "X1", 10),
            ("F2", "X1", 10),
            ("X1", "S1", 5),
            ("X1", "S2", 7)
        ]
        self.assertEqual(get_max_flow(farms, shops, roads), 12)

    def test_no_path(self):
        farms = ["F1"]
        shops = ["S1"]
        roads = [("F1", "X1", 10), ("X2", "S1", 10)]
        self.assertEqual(get_max_flow(farms, shops, roads), 0)

if __name__ == '__main__':
    unittest.main()