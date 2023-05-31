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
        super.__init__(size, size)
        self.__size = size
