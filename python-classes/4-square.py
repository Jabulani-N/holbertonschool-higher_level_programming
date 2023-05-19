#!/usr/bin/python3
""" creates class Square that defines a square by: (based on 3-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:

size must be an integer, otherwise raise a/
TypeError exception with the message size must be an integer

if size is less than 0, raise a ValueError/
 exception with the message size must be >= 0
Instantiation with optional size: def __init__(self, size=0):
Public instance method: def area(self): that returns the current square area


"""


class Square:
    """Object-class summary documentation.


    attributes will be documented in the below section
    indent them like anything else protected by a colon.

    Attributes:
        size: made private via leading underscores. defaults to 0
    """

    def __init__(self, size=0):
        """__init__ method documentation

        __init__ can optionally instead be documented in the class section
        do not include 'self' as an arg

        Args:
            size: made optional via "=0" defualt value.
                size of square instanciated
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """squares self.__size without importing math
        """
        return self.__size * self.__size

    @property
    def size(self):
        """getter: returns size of an existing Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter: alters size of an existing Square"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
