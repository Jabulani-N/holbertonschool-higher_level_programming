#!/usr/bin/python3
""" creates class Square.

"""


class Square:
    """Object-class summary documentation.


    attributes will be documented in the below section
    indent them like anything else protected by a colon.

    Attributes:
        size: private via leading underscores. defaults to 0
    """


    def __init__(self, size):
        """__init__ method documentation

        __init__ can optionally instead be documented in the class section
        do not include 'self' as an arg

        Args:
            size: size of square instanciated
        """
        self.__size = size
