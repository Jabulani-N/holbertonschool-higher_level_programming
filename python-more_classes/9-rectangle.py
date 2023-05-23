#!/usr/bin/python3
"""module for class Rectangle.

new features:
class method def square(cls, size=0):
returns newly created Rectangle with height == width == size
"""


class Rectangle:
    """Rectangle class

    Attributes:
    width - private instance - int >= 0
    height - private instance - int >= 0

    """
    number_of_instances = 0
    print_symbol = "#"

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
        type(self).number_of_instances += 1

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
                str_rectangle += f'{self.print_symbol}'
            str_rectangle += "\n"
        str_rectangle = str_rectangle.strip()
        return str_rectangle

    def __repr__(self):
        reproduction = f'Rectangle({self.__width}, {self.__height})'
        return reproduction

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        """returns rect_1 if rec_2 does not have a higher area
        both must be instances of Rectangle
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    def square(cls, size=0):
        return cls.__init__(size, size)
