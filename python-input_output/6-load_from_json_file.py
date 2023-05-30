#!/usr/bin/python3
"""module file-reads JSON representation to a string
requires importing json
"""
import json


def load_from_json_file(filename):
    """uses load to read a JSON-filled file to a string

    uses operations from file-reading
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)  # dump will do the writing
        # f is the text file object opened for writing
