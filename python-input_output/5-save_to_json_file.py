#!/usr/bin/python3
"""module file-makes JSON representation of a string
requires importing json
"""
import json


def save_to_json_file(my_obj, filename):
    """uses dump to write a JSON-filled file from a string
    likely  works one some other objects too

    uses operations from file-writing
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)  # dump will do the writing
        # f is the text file object opened for writing
