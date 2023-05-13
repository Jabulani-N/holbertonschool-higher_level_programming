#!/usr/bin/python3
def def print_reversed_list_integer(my_list=[]):
    # copied form task 0, but subtracting index from length to print backward
    for index in my_list:  # creates variable "index" to loop through "my_list"
        # loops through my_list. everything indented gets looped
        print("{:d}".format(len(my_list) - index))
        # "{:d}" is what str.format means in the question
# no indent = no loop
