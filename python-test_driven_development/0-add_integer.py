#!/usr/bin/python3
"""module 0-add_integer

adds the input ints. also accepts integer floats"""


def add_integer(a, b=98):
    """tests for type to be int or float,

    then if they are and are divisible by 1, return their sum

    if they are float, cast to int.
    int(x) == floor of x in iteger format
    """

    if isinstance(a, int) is False and \
       isinstance(a, float) is False or \
       a is None:
        raise TypeError ("a must be an integer")
    if isinstance(b, int) is False and \
       isinstance(b, float) is False or \
       b is None:
        raise TypeError ("b must be an integer")
    if a % 1 != 0:
        a = int(a)
    if b % 1 != 0:
        b = int(b)
    return a + b
