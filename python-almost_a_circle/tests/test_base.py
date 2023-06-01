#!/usr/bin/python3
"""testing module using unittest
This module exclusively tests the Base class

find a way to directly import the base class
it's like "from something import Base"
then you can do the "Base(89) the checker wants
"""


import unittest

from models.base import Base


class testingTask1(unittest.TestCase):
    """tests class for task 1
    define a test, set up whatever you need between the
    def and self.assert.

    a proper setup() function will accelerate class creation
    """


    # self.assert(thing, what_thing_should_equal_to_pass_test)
    def test_empty_input(self):
        newbase = Base(89)
        self.assertEqual(newbase.id, 89)


if __name__ == '__main__':
    unittest.main
