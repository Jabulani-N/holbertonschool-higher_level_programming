#!/usr/bin/python3


def add_integer(a, b=98):
    """tests for type to be int or float,

    then if they are and are divisible by 1, return their sum
    """

    if isinstance(a, int) is False and \
       isinstance(a, float) is False or \
       a == None:
        raise TypeError ("a must be an integer")
    if isinstance(b, int) is False and \
       isinstance(b, float) is False or \
       b == None:
        raise TypeError ("b must be an integer")
    if a % 1 != 0:
        raise TypeError ("a must be an integer")
    if b % 1 != 0:
        raise TypeError ("a must be an integer")
    return a + b
