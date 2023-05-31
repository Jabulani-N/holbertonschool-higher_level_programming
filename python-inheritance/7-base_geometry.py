#!/usr/bin/python3
"""module does nothing"""


class BaseGeometry():
    """does nothing"""

    def area(self):
        """throws an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate value. assume name will be string"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
