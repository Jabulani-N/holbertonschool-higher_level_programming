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

    def __init__(self, size=0, position=(0, 0)):
        """creates a Square

        Args:
            size: made optional via "=0" defualt value.
                size of square instanciated
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if isinstance(position, tuple) is False or \
           len(position) != 2 or \
           isinstance(position[0], int) is False or \
           isinstance(position[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0 or \
           position[0] is None or position[1] is None:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__struckpose = position

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
        """prints a square of #s based on self.__size

        considers position
        """

        if self.__size == 0:
            print("")
        else:
            for heading in range(self.__struckpose[1]):
                print()
            for row in range(self.__size):
                for indentation in range(self.__struckpose[0]):
                    print(" ", end='')
                for column in range(self.__size):
                    print("#", end='')
                print("")

    @property
    def position(self):
        return self.__struckpose

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is False or \
           len(value) != 2 or \
           isinstance(value[0], int) is False or \
           isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0 or \
           value[0] is None or value[1] is None:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__struckpose = value
        self.__struckpose = value
