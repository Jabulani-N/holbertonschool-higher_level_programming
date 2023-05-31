#!/usr/bin/python3
"""imports rectangle
rectangle imports base_gemoetry
rectangle elaborates
rectangle leaves
elaborates
leaves
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    """elaboration of rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        # so it complains correcctly if size is bad
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """happens when you say print(instance)
        overwrites the parent's version
        """
        selfstring = "[Square] " + str(self.__width) \
                     + "/" + str(self.__height)
        return selfstring