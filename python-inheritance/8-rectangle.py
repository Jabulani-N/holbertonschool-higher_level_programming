#!/usr/bin/python3
"""imports base_geometry
elaborates
leaves
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle (BaseGeometry):
    """elaboration of base geometry"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
