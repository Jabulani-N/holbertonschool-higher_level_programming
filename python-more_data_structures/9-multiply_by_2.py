#!/usr/bin/python3#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dupe = a_dictionary.copy()
    for key in dupe:
        dupe[key] *= 2
    return dupe
