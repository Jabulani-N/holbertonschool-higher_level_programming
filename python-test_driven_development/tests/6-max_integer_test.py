#!/usr/bin/python3
"""testing module using unittest
"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class testingTask6(unittest.TestCase):
    """tests a number of potential inputs to the provided file"""

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_len1_list(self):
        self.assertEqual(max_integer([3]), 3)

    def test_len3_list(self):
        self.assertEqual(max_integer([3, 65, 4]), 65)

    def test_with_negatives(self):
        self.assertEqual(max_integer([-3, -65, -4]), -3)

    def test_ending_max(self):
        self.assertEqual(max_integer([-3, -9999, -1]), -1)

    def test_middle_max(self):
        self.assertEqual(max_integer([-3, 9999, -1]), 9999)

    def test_two_max(self):
        self.assertEqual(max_integer([-3, 1, 1]), 1)


if __name__ == '__main__':
    unittest.main
