#!/usr/bin/python3#!/usr/bin/python3
def no_c(my_string):
    hold_string = my_string.translate({ord('C'): None})
    hold_string = hold_string.translate({ord('c'): None})
    return hold_string
