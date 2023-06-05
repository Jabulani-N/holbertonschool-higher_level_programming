#!/usr/bin/python3
""" creates class Base
import your previous integer validator,
use it on the setters
it'll save space from validating every setter manually
"""

from models.base import Base


class Rectangle (Base):
    """inehrits from base"""

    def integer_validator0(self, name, value):
        """validate value. assume name will be string
        based on python-inheritance project task 7
        assume name is always stirng
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value < 0:
            raise ValueError(name + " must be >= 0")

    def integer_validator1(self, name, value):
        """validate value. assume name will be string
        based on python-inheritance project task 7
        assume name is always stirng
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be > 0")

    def __init__(self, width, height, x=0, y=0, id=None):
        """all starter attributes will be private
        all will use getters and setters
        """
        super().__init__(id)
        self.integer_validator1("width", width)
        self.integer_validator1("height", height)
        self.integer_validator0("x", x)
        self.integer_validator0("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """gets above property"""
        return self.__width

    @width.setter
    def width(self, imp):
        """sets above property"""
        if self.integer_validator1("width", imp):
            self.__width = imp

    @property
    def height(self):
        """gets above property"""
        return self.__height

    @height.setter
    def height(self, imp):
        """sets above property"""
        if self.integer_validator1("height", imp):
            self.__height = imp

    @property
    def x(self):
        """gets above property"""
        return self.__x

    @x.setter
    def x(self, imp):
        """sets above property"""
        if self.integer_validator0("x", imp):
            self.__x = imp

    @property
    def y(self):
        """gets above property"""
        return self.__y

    @y.setter
    def y(self, imp):
        """sets above property"""
        if self.integer_validator0("y", imp):
            self.__y = imp

    def area(self):
        """calculates and returns area"""
        return self.__width * self.__height

    def display(self):
        """prints a rectangle
        based on instance attributes
        """
        str_rectangle = ""
        for heading in range(self.__y):
            str_rectangle += "\n"
        for row in range(self.__height):
            for indent in range(self.__x):
                str_rectangle += " "
            for column in range(self.__width):
                str_rectangle += "#"
            str_rectangle += '\n'
        print(str_rectangle, end="")

    def __str__(self):
        return "[Rectangle] (" + str(self.id) + ") " +\
               str(self.__x) + "/" + str(self.__y) + " - " +\
               str(self.__width) + "/" + str(self.__height)

    def update(self, *args):
        """updates all the rectangle instance's attributes.
        as many attributes as given.
        runs the respective validator on each.

        elif is used beacause the closes python has to a switch is
        a dictionary. you'd use the 'switch' as the key,
        and the 'do this' as the definition.
        returning runnable code out of that? more work than worth

        the order is id, width, height, x, y
        """
        argnum = 0
        for arg_itself in args:
            if arg_itself is None:  # it's done all args, or got none
                return  # also prevents icrimenting argnum
            elif argnum is 0:
                # validate and assign for id
                if isinstance(arg_itself, int):
                    self.id = arg_itself
            elif argnum is 1:
                # validate and assign for width
                if self.integer_validator1("width", arg_itself):
                    self.__width = arg_itself
            elif argnum is 2:  # height
                pass
            elif argnum is 3:  # x
                pass
            elif argnum is 4:  # y
                pass
            argnum += 1  # keep up with arg_itself in args incrimenting
