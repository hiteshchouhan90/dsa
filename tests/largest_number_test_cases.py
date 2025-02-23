import unittest
from src.dsa.array_easy.largest_element import largest_element
class TestLargestElementFunction(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(largest_element([]), 0)

    def test_single_element_array(self):
        self.assertEqual(largest_element([5]), 5)

    def test_multiple_element_array_positive(self):
        self.assertEqual(largest_element([1, 8, 7, 56, 90]), 90)

    def test_multiple_element_array_negative(self):
        self.assertEqual(largest_element([-10, -5, -2, -8]), -2)

    def test_multiple_element_array_mixed(self):
        self.assertEqual(largest_element([-10, 5, -2, 8, 0]), 8)

if __name__ == '__main__':
    unittest.main()