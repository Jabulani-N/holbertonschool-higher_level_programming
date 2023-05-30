#!/usr/bin/python3
"""module will read a file and print it"""


def read_file(filename=""):
    """reads file filename and prints it
    uses with operator
    filename is the input argument
    """

    with open('filename', encoding="utf-8") as f:
        read_data = f.read()
    print(read_data)
