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

    @classmethod
    def save_to_file(cls, list_objs):
        """recieves an object, and writes it to a file
        name the file {cls}.json
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                # get each object's dictionary (they all inherit the method)
                # puts that diciotnary in the list_dicts
                f.write(Base.to_json_string(list_dicts))
                # writes the to_json_string results directly to file

    @staticmethod
    def from_json_string(json_string):
        """converts a json string into a dictionary"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance from a dictionary
        cls will be one of the base family
        cls.__name__ gives the type
        """
        if cls.__name__ == "Rectangle":
            holder = cls (1, 1)
        else:
            holder = cls (1)  # works for base and square
        holder.update(**dictionary)
        return holder
