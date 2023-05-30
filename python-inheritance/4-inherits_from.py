#!/usr/bin/python3
"""module holds a function to tell if object is of class"""


def inherits_from(obj, a_class):
    """if it's inherited, but not same type.

    uses type and as isinstance:
    type does not allow inherited to be True
    isinstance does
    """
    a = type(obj)

    if a_class == a:
        return False
    else:
        if isinstance(obj, a_class):
            return True
    return False  # if it's not the type, and not a child
