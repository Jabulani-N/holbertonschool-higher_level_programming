#!/usr/bin/python3
"""module returns a class's dict in the form of a simple data structure
the data structure used here is list
requires no import
"""


def class_to_json(obj):
    """returns list of obj's dict"""
    return list(obj.__dict__)
