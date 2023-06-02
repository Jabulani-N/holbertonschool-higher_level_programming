#!/usr/bin/python3
""" creates class Base
import your previous integer validator,
use it on the setters
it'll save space from validating every setter manually
"""

from models.base import Base


class Rectangle (Base):
    """inehrits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """all starter attributes will be private
        all will use getters and setters
        """
        super().__init__(id)
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
        self.__width = imp

    @property
    def height(self):
        """gets above property"""
        return self.__height

    @height.setter
    def height(self, imp):
        """sets above property"""
        self.__height = imp

    @property
    def x(self):
        """gets above property"""
        return self.__x

    @x.setter
    def x(self, imp):
        """sets above property"""
        self.__x = imp

    @property
    def y(self):
        """gets above property"""
        return self.__y

    @y.setter
    def y(self, imp):
        """sets above property"""
        self.__y = imp
