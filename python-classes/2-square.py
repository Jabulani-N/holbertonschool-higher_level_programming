#!/usr/bin/python3
""" creates class Square.

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
