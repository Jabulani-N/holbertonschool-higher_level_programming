#!/usr/bin/python3
"""testing module using unittest
"""


import unittest

max_integer = __import__('6-max_integer').max_integer

class testingTask6(unittest.TestCase):
    """tests a number of potential inputs to the provided file"""


    def test_empty_list(self):
        self.assertEqual(max_integer([]), 0)



if __name__ == '__main__':
    unittest.main