# tests/sorting_methods_test.py

import unittest
from dsa.sorting_methods.bubble_sort import bubble_sort
from dsa.sorting_methods.selection_sort import selection_sort
from dsa.sorting_methods.insertion_sort import insertion_sort
from dsa.sorting_methods.merge_sort import merge_sort
from dsa.sorting_methods.rec_bubble_sort import rec_bubble_sort
from dsa.sorting_methods.rec_insertion_sort import rec_insertion_sort

class TestSortingMethods(unittest.TestCase):

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort([7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(bubble_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([]), [])

    def test_selection_sort(self):
        self.assertEqual(selection_sort([7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(selection_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(selection_sort([1]), [1])
        self.assertEqual(selection_sort([]), [])

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(insertion_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(insertion_sort([1]), [1])
        self.assertEqual(insertion_sort([]), [])

    def test_merge_sort(self):
        self.assertEqual(merge_sort([7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(merge_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(merge_sort([1]), [1])
        self.assertEqual(merge_sort([]), [])

    def test_rec_bubble_sort(self):
        self.assertEqual(rec_bubble_sort([7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(rec_bubble_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(rec_bubble_sort([1]), [1])
        self.assertEqual(rec_bubble_sort([]), [])

    def test_rec_insertion_sort(self):
        self.assertEqual(rec_insertion_sort([7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(rec_insertion_sort([3, 1, 2]), [1, 2, 3])
        self.assertEqual(rec_insertion_sort([1]), [1])
        self.assertEqual(rec_insertion_sort([]), [])

if __name__ == '__main__':
    unittest.main()