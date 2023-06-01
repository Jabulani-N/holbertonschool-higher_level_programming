#!/usr/bin/python3
""" creates class Base"""


class Base:
    """has attribute __nb_objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method documentation
        assume any given id is an int, and DO NOT TEST for that
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
