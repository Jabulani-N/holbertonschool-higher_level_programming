#!/usr/bin/python3
"""testing module using unittest
This module exclusively tests the Rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """tests class for class Rectangle.
    define a test, set up whatever you need between the
    def and self.assert.

    a proper setup() function will accelerate class creation
    """
    # self.assert(thing, what_thing_should_equal_to_pass_test)
    def test_width_height_assignment(self):
        """tests creating a rectangle with
        width and height of different values
        """
        pass

    def test_x_y_assignment(self):
        """tests creating a rectangle with x and y valeus
        tests the getter for both
        """
        pass


if __name__ == '__main__':
    unittest.main
