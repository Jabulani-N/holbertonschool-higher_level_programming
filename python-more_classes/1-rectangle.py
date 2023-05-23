#!/usr/bin/python3
"""Most basic module for class Rectangle.

"""


class Rectangle:
    """Rectangle class

    Attributes:
    width - private instance - int >= 0
    height - private instance - int >= 0

    """


    def __init__(self, width=0, height=0):
        """__init__ to be called upon creating a Rectangle instance
        sizes are intentionally optional.
        """
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.hight = height
        self.__width = width

    @property
    def width(self):
        """returns width"""
        return self.width

    @width.setter
    def width(self, value):
        """sets wieth, with same conditions as __init__"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height"""
        return self.height

    @height.setter
    def height(self, value):
        """sets height with same conditions as __init__"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
