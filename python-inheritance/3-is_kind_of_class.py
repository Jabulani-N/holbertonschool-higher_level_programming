#!/usr/bin/python3
"""module holds a function to tell if object is of class"""


def is_same_class(obj, a_class):
    """uses isnstance, as isinstance allows inherited to be True"""
    return isinstance(obj, a_class)
