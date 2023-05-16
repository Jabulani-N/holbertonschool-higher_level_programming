#!/usr/bin/python3#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    for item in sorted(a_dictionary):
        print(item, a_dictionary[item], sep=': ')
# sorted returns a list (not dict) of the keys in the provided dict
# sorted also sorts lists
