import unittest
from src.dsa.binary_search_array.search_rotated_array import search_rotated_array

class TestSearchRotatedArray(unittest.TestCase):
    def test_search_rotated_array(self):
        self.assertEqual(search_rotated_array([4, 5, 6, 7, 0, 1, 2], 0), 4)
        self.assertEqual(search_rotated_array([4, 5, 6, 7, 0, 1, 2], 3), -1)
        self.assertEqual(search_rotated_array([1], 0), -1)

        self.assertEqual(search_rotated_array([1, 3], 3), 1)
        self.assertEqual(search_rotated_array([1, 3], 1), 0)