from src.dsa.array_easy.lc_1752 import check_sorted_array
import unittest

class TestSortedArray(unittest.TestCase):
    def test_check_sorted_array(self):
        self.assertTrue(check_sorted_array([1,2,3,4,5]))
        self.assertFalse(check_sorted_array([3,4,2,1]))
        self.assertFalse(check_sorted_array([1,3,2,4,5]))

if __name__ == '__main__':
    unittest.main()