#!/usr/bin/python3
"""module holds a function to tell if object is of class"""


def is_same_class(obj, a_class):
    """uses type, as isinstance allows inherited to be True"""
    a = type(obj)
    b = type(a_class)
    return b == a
