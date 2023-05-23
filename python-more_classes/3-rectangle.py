#!/usr/bin/python3
"""module for class Rectangle.

new features: _str_ and _repr_ return string of Rectangle isntance
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

        self.__height = height
        self.__width = width

    @property
    def width(self):
        """returns width"""
        return self.__width

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
        return self.__height

    @height.setter
    def height(self, value):
        """sets height with same conditions as __init__"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calcs and returns rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """calcs and returns rectangle perimiter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """returns a string rectangle of #s
        width wide and height tall
        """
        str_rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return str_rectangle
        for row in range(self.__height):
            for item in range(self.__width):
                str_rectangle += "#"
            str_rectangle += "\n"
        return str_rectangle

    def __repr__(self):
        """returns a string rectangle of #s
        width wide and height tall
        """
        str_rectangle = ""
        if self.__height == 0 or self.__width == 0:
            return str_rectangle
        for row in range(self.__height):
            for item in range(self.__width):
                str_rectangle += "#"
            str_rectangle += "\n"
        return str_rectangle
