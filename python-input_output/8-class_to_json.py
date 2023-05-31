#!/usr/bin/python3
"""module returns a class's dict in the form of a simple data structure
the data structure used here is list
requires no import
"""


def class_to_json(obj):
    """returns list of obj's dict"""
    dict_desc = {}

    attributes = obj.__dict__

    for attr, value in attributes.items():
        if type(value) in [list, dict, str, int, bool]:
            dict_desc[attr] = value
    return dict_desc
