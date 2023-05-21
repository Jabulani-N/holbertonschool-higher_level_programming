#!/usr/bin/python3
"""module that prints a square of hashes

size based on size.

only accepts integers
"""


def print_square(size):
    """prints a square of #s based on size

    largely copied from the test python classes directory
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return None
    else:
        for row in range(size):
            for column in range(size):
                print("#", end='')
            print("")
