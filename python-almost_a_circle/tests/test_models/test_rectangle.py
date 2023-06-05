#!/usr/bin/python3
"""testing module using unittest
This module exclusively tests the Rectangle class
"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """tests class for class Rectangle.
    define a test, set up whatever you need between the
    def and self.assert.

    a proper setup() function will accelerate class creation
    """
    # self.assertEqual(thing, what_thing_should_equal_to_pass_test)
    def setUp(self):
        """Reset the __nb_objects counter.
        print test"""
        print("Rectangle setUp")
        Base._Base__nb_objects = 0


    def tearDown(self):
        print("Rectangle tearDown")


    def test_width_height_assignment(self):
        """tests creating a rectangle with width and height
        of different values
        """
        with self.assertRaises(ValueError):
            Rectangle(0, 0)
        with self.assertRaises(ValueError):
            Rectangle(-1, -50)
        with self.assertRaises(TypeError):
            Rectangle('lol', 10)
        with self.assertRaises(TypeError):
            Rectangle(11111, 'rofl')
        rect_valid = Rectangle(2, 3)
        self.assertEqual(2, 2)
        # print("rect_valid's width is" + str(rect_valid.width()))
        self.assertEqual(2, rect_valid.width)
        self.assertEqual(rect_valid.height, 3)

    def test_x_y_assignment(self):
        """tests creating a rectangle with x and y valeus
        tests the getter for both
        """
        with self.assertRaises(ValueError):
            Rectangle(10, 10, -1, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 10, 2, -1)
        with self.assertRaises(TypeError):
            Rectangle(2, 10, "lol", 2)
        with self.assertRaises(TypeError):
            Rectangle(11111, 2222, 3, 'rofl')
        rect_valid = Rectangle(2, 3, 1, 2)
        self.assertEqual(rect_valid.display(),"\n\n\n   ##\n   ##")

    def update(self, *args):
        """updates all the rectangle instance's attributes.
        as many attributes as given.
        runs the respective validator on each.

        elif is used beacause the closes python has to a switch is
        a dictionary. you'd use the 'switch' as the key,
        and the 'do this' as the definition.
        returning runnable code out of that? more work than worth
        """
        argnum = 0
        for arg_itself in args:
            pass


if __name__ == '__main__':
    unittest.main
