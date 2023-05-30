#!/usr/bin/python3
"""module returns JSON representation of a string
requires importing json
"""
import json


def to_json_string(my_obj):
    """uses dumps to return JSON of a string
    likely  works one some other objects too
    """

    return json.dumps(my_obj)
