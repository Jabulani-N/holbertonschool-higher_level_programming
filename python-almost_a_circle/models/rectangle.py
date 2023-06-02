#!/usr/bin/python3
""" creates class Base
import your previous integer validator,
use it on the setters
it'll save space from validating every setter manually
"""

Base = __import__('base').Base

class Rectrnagle(Base):
    """inehrits from base"""


    def __init__(self, width, height, x=0, y=0, id=None):
        """all starter attributes will be private
        all will use getters and setters
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x  = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, imp):
        self.__width = imp


    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, imp):
        self.__height = imp

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, imp):
        self.__x = imp

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, imp):
        self.__y = imp
