#!/usr/bin/python3
def print_list_integer(my_list=[]):
    #  I believe the above is the prototype of the function
    str = "{content}" #  brackets mean formattable variable
    for index in my_list: #  creates variable "index" to loop through "my_list"
        #loops through my_list. everything indented gets looped
        print(str.format(content = index))
        #  str.format(variable = anything_I_want)
#  no indent = no loop