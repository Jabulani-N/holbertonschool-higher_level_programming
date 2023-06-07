#!/usr/bin/python3
""" creates class Base"""

import json


class Base:
    """has attribute __nb_objects"""

    __nb_objects = 0

    def __init__(self, id=None):
        """__init__ method documentation
        assume any given id is an int, and DO NOT TEST for that
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON rep of list_dicitonaries
        unless it is empty/None, in wich caes return '[]'"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """recieves an object, and writes it to a file
        name the file {cls}.json
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            json.dump(list_objs, f)  # dump will do the writing
            # f is the text file object opened for writing
