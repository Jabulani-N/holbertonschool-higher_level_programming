#!/usr/bin/python3
"""testing module using unittest
This module exclusively tests the Base class
"""


import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """tests class for class Base.
    define a test, set up whatever you need between the
    def and self.assert.

    a proper setup() function will accelerate class creation
    """

    def setUp(self):
        """Reset the __nb_objects counter.
        print test"""
        print("Base setUp")
        Base._Base__nb_objects = 0


    def tearDown(self):
        print("Base tearDown")

    # self.assertEqual(thing, what_thing_should_equal_to_pass_test)
    def test_id_assignment(self):
        newbase1 = Base()
        newbase2 = Base(89)
        newbase3 = Base()
        self.assertEqual(newbase1.id, 1)
        self.assertEqual(newbase2.id, 89)
        self.assertEqual(newbase3.id, 2)

    def test_id_type(self):
        '''test the type of id attribute to ensure an integer'''
        base = Base(10)
        self.assertIsInstance(base.id, int)


if __name__ == '__main__':
    unittest.main
