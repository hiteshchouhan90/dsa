import unittest
from src.dsa.array_easy.lc_189_rotate_array import rotate_array

class rotate_array_unit_test(unittest.TestCase):
    def test_rotate_array(self):
        self.assertEqual(rotate_array([1,2,3,4,5],2), [4,5,1,2,3])
        self.assertEqual(rotate_array([],2),[])
        self.assertEqual(rotate_array([1,2,3,4,4,44,4,5],1), [5,1,2,3,4,4,44,4])
        self.assertEqual(rotate_array([1],1), [1])
        self.assertEqual(rotate_array([1,2],1), [2,1])
