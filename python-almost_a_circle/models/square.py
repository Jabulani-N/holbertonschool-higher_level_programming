#!/usr/bin/python3
""" creates Square
import your previous integer validator,
use it on the setters
it'll save space from validating every setter manually
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """inehrits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """all starter attributes handled by super"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] (" + str(self.id) + ") " +\
               str(self.x) + "/" + str(self.y) + " - " +\
               str(self.width)

    @property
    def size(self):
        """gets above property"""
        return self.width

    @size.setter
    def size(self, imp):
        """sets above property"""
        self.width = imp
        self.height = imp
