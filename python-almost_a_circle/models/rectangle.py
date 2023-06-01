#!/usr/bin/python3
""" creates class Base"""

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
    def

    @.setter
