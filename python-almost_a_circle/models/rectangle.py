#!/usr/bin/python3
""" creates class Base
import your previous integer validator,
use it on the setters
it'll save space from validating every setter manually
"""

from models.base import Base


class Rectangle (Base):
    """inehrits from base"""

    def integer_validator(self, name, value):
        """validate value. assume name will be string
        based on python-inheritance project task 7
        assume name is always stirng
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be > 0")
        return True  # so we have a success output

    def __init__(self, width, height, x=0, y=0, id=None):
        """all starter attributes will be private
        all will use getters and setters
        """
        super().__init__(id)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.integer_validator("x", x)
        self.integer_validator("y", y)
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
        if self.integer_validator("width", imp):
            self.__width = imp

    @property
    def height(self):
        """gets above property"""
        return self.__height

    @height.setter
    def height(self, imp):
        """sets above property"""
        if self.integer_validator("height", imp):
            self.__height = imp

    @property
    def x(self):
        """gets above property"""
        return self.__x

    @x.setter
    def x(self, imp):
        """sets above property"""
        if self.integer_validator("x", imp):
            self.__x = imp

    @property
    def y(self):
        """gets above property"""
        return self.__y

    @y.setter
    def y(self, imp):
        """sets above property"""
        if self.integer_validator("y", imp):
            self.__y = imp
