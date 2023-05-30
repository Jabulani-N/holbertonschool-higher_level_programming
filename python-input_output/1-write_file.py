#!/usr/bin/python3
"""module will write text to a file"""


def write_file(filename="", text=""):
    """writes text text to file filename
    uses with operator
    filename is the input argument
    text is input argument
    """

    with open(filename, 'rw', encoding="utf-8") as f:
        typed = f.write(text)
    return typed
