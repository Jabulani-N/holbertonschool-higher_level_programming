#!/usr/bin/python3
"""testing module using unittest
This module exclusively tests the Base class

find a way to directly import the base class
it's like "from something import Base"
then you can do the "Base(89) the checker wants

consider looking at at least two other test files
to see how they are structured
"""


import unittest

from models.base import Base


class TestBase(unittest.TestCase):
    """tests class for class Base.
    define a test, set up whatever you need between the
    def and self.assert.

    a proper setup() function will accelerate class creation
    """
    # self.assert(thing, what_thing_should_equal_to_pass_test)
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
