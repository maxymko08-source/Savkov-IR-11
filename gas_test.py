import unittest
from gas_system import check_gas_supply

class TestGasSupply(unittest.TestCase):

    def test_all_connected(self):
        cities = ['Львів', 'Стрий']
        storages = ['Сховище_1']
        pipelines = [['Сховище_1', 'Львів'], ['Львів', 'Стрий']]
        
        result = check_gas_supply(cities, storages, pipelines)
        self.assertEqual(result, [])

    def test_unreachable_city(self):
        cities = ['Львів', 'Стрий']
        storages = ['Сховище_1']
        pipelines = [['Сховище_1', 'Стрий']]
        
        expected = [['Сховище_1', ['Львів']]]
        result = check_gas_supply(cities, storages, pipelines)
        self.assertEqual(result, expected)

    def test_transit_delivery(self):
        cities = ['Львів', 'Стрий']
        storages = ['Сховище_1']
        pipelines = [['Сховище_1', 'Львів'], ['Львів', 'Стрий']]
        
        result = check_gas_supply(cities, storages, pipelines)
        self.assertEqual(result, [])

    def test_multiple_storages(self):     
        cities = ['Львів']
        storages = ['Сховище_1', 'Сховище_2']
        pipelines = [['Сховище_1', 'Львів']]
        
        expected = [['Сховище_2', ['Львів']]]
        result = check_gas_supply(cities, storages, pipelines)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()