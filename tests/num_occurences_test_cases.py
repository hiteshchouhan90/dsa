import unittest
from src.dsa.binary_search_array.num_occurences import num_occurences

class TestNumOccurences(unittest.TestCase):
    def test_num_occurences(self):
        self.assertEqual(num_occurences([1, 2, 2, 2, 2, 3, 4, 4, 8], 4), 2)
        self.assertEqual(num_occurences([1, 2, 2, 2, 2, 3, 4, 4, 8], 8), 1)
        self.assertEqual(num_occurences([1, 2, 2, 2, 2, 3, 4, 4, 8], 1), 1)
        self.assertEqual(num_occurences([1, 2, 2, 2, 2, 3, 4, 4, 8], 5), 0)