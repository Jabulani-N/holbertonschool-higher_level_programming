#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # copied form task 0, but subtracting index from length to print backward
    if type(my_list) != type([1,2]):  # type(me) returns the type of me
        return None # example array makes code prtable regardless of pyversion
    for index in reversed(my_list):  # reversed works on any sequence
        # creates variable "index" to loop through reverse of "my_list"
        print("{:d}".format(index))
        # "{:d}" is what str.format means in the question
