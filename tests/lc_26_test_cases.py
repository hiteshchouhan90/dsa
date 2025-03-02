import unittest
from src.dsa.array_easy.lc_26 import remove_duplicates

class test_remove_duplicates(unittest.TestCase):
    def test_remove_duplicates(self):
        nums = [0,0,1,2,3,4,4,4,5,6,6,7,10]
        self.assertEqual(remove_duplicates(nums=nums), (9, [0,1,2,3,4,5,6,7,10, 6,6,7,10]))           
        nums = [1,1,1,1]
        self.assertEqual(remove_duplicates(nums=nums), (1, [1,1,1,1]))
        nums = [1]
        self.assertEqual(remove_duplicates(nums=nums), (1, [1]))
        nums = []
        self.assertEqual(remove_duplicates(nums=nums), (0, []))