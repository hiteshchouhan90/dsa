import unittest
from src.dsa.array_easy.lc_283_move_zeros import move_zeros

class move_zeros_unit_test(unittest.TestCase):
    def test_move_zeros(self):
        self.assertEqual(move_zeros([0,1,0,3,12]), [1,3,12,0,0])
        self.assertEqual(move_zeros([0]), [0])
        self.assertEqual(move_zeros([1]), [1])
        self.assertEqual(move_zeros([]), [])