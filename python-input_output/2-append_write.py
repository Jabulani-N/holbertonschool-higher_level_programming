#!/usr/bin/python3
"""module will append text to a file"""


def append_write(filename="", text=""):
    """appends text text to file filename
    uses with operator
    filename is the input argument
    text is input argument
    """

    with open(filename, 'a', encoding="utf-8") as f:
        typed = f.write(text)
    return typed
