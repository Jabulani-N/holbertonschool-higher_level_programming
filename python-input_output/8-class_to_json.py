#!/usr/bin/python3
"""module returns a class's dict in the form of a simple data structure
the data structure used here is list
requires no import
"""


def class_to_json(obj):
    """returns list of obj's dict"""
    return obj.__dict__

# the below got ful marks. I tried the above, but it did not work.
# I later learned that it was indeed the approach. likely syntax error.
# dict_desc = {}

    # attributes = obj.__dict__

    # for attr, value in attributes.items():
        # if type(value) in [list, dict, str, int, bool]:
            # dict_desc[attr] = value
    # return dict_desc
