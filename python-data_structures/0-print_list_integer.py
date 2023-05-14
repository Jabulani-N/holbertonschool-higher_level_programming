#!/usr/bin/python3
def print_list_integer(my_list=[]):
    # I believe the above is the prototype of the function
    for index in my_list:  # creates variable "index" to loop through "my_list"
        # loops through my_list. everything indented gets looped
        print("{:d}".format(index))
# no indent = no loop
