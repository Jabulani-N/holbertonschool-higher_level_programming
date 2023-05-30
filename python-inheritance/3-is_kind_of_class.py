#!/usr/bin/python3
"""module holds a function to tell if object is of class"""


def is_same_class(obj, a_class):
    """uses isinstance, which allows children to be True"""
    return isinstance(obj, a_class)
