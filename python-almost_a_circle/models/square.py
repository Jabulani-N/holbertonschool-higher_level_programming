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

    def update(self, *args, **kwargs):
        """updates the square
        can be made more efficient by offloading
        all args that are not size-related to super's update

        for the sake coder-hours, this will include reundant code instead.
        """
        argnum = 0
        skipQwargs = False

        if args is not None:
            for arg_itself in args:
                if isinstance(arg_itself, dict) is False:
                    skipQwargs = True
                    # so that kwargs version only runs if exclusively kwargs
                if arg_itself is None:  # it's done all args, or got none
                    return  # also prevents icrimenting argnum
                elif argnum == 0:
                    # validate and assign for id
                    if isinstance(arg_itself, int):
                        self.id = arg_itself
                elif argnum == 1:
                    # validate and assign for width
                    self.integer_validator1("size", arg_itself)
                    self.size = arg_itself
                elif argnum == 2:  # x
                    self.integer_validator0("x", arg_itself)
                    self.__x = arg_itself
                elif argnum == 3:  # y
                    self.integer_validator0("y", arg_itself)
                    self.__y = arg_itself
                argnum += 1  # keep up with arg_itself in args incrimenting

        if skipQwargs is False:
            # kwargs stuff goes here. only fires if args is empty
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == "id":
                        if isinstance(value, int):
                            self.id = value
                    elif key == "size":
                        self.size = value
                    elif key == "x":
                        self.integer_validator0("x", value)
                        self.__x = value
                    elif key == "y":
                        self.integer_validator0("y", value)
                        self.__y = value
