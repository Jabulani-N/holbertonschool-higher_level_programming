#!/usr/bin/python3
"""module returns JSON representation of a class's dict
requires importing json
"""
import json


def class_to_json(obj):
    """uses dumps to return JSON of a string
    likely  works one some other objects too
    may be able to use string() to turn the dict into a string to dump
    """

    return json.dumps(my_obj)
