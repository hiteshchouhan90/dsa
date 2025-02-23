import unittest
from src.dsa.array_easy.second_largest import second_largest

class TestSecondLargestFunction(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(second_largest([]), -1)

    def test_array_with_one_element(self):
        self.assertEqual(second_largest([5]), -1)

    def test_array_with_two_distinct_elements(self):
        self.assertEqual(second_largest([5, 10]), 5)

    def test_array_with_two_identical_elements(self):
        self.assertEqual(second_largest([5, 5]), -1)

    def test_array_with_multiple_distinct_elements(self):
        self.assertEqual(second_largest([12, 35, 1, 10, 34, 1]), 34)

    def test_array_with_multiple_identical_elements(self):
        self.assertEqual(second_largest([10, 10, 10, 5, 5]), 5)

if __name__ == '__main__':
    unittest.main()