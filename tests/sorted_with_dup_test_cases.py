import unittest
from src.dsa.array_easy.sorted_with_duplicates import sorted_union

class SortedWithDupTestCases(unittest.TestCase):
    def test_sorted_union(self):
        arr1 = [1,2,2,3,4]
        arr2 = [5,6,6,7,7]
        self.assertEqual(sorted_union(arr1, arr2), [1,2,3,4,5,6,7])
        arr1 = [1,2,2,3,4]
        arr2 = []
        self.assertEqual(sorted_union(arr1, arr2), [1,2,3,4])
        arr1 = [1,2,2,3,4]
        arr2 = [5,6,6,7,7]
        self.assertEqual(sorted_union(arr1, arr2), [1,2,3,4,5,6,7])