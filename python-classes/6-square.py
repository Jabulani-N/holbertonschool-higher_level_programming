#!/usr/bin/python3
""" creates class Square.

"""


class Square:
    """Object-class summary documentation.


    attributes will be documented in the below section
    indent them like anything else protected by a colon.

    Attributes:
        size: made private via leading underscores. defaults to 0
        position: number of spaces to put befroe printing
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


    def my_print(self):
        """prints a square of #s based on self.__size"""
        if self.__size == 0:
            print("")
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end='')
                print("")
