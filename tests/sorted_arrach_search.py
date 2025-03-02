import unittest
from src.dsa.array_easy.sorted_array_search import search

class TestSortedArraySearch(unittest.TestCase):
    def test_search(self):
        self.assertEqual(search([1, 2, 3, 4, 6], 6), True)
        self.assertEqual(search([1, 2, 4, 5, 6], 3), False)
        self.assertEqual(search([2, 3, 5, 6], 1), False)