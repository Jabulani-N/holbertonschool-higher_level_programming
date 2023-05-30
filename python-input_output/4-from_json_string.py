#!/usr/bin/python3
"""module returns Pyton object representation of a JSON string/file object
requires importing json
"""
import json


def from_json_string(my_str):
    """uses load to return JSON of a string"""
    return json.loads(my_str)
