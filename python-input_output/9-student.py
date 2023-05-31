#!/usr/bin/python3
"""module does nothing"""


class Student():
    """arimas"""

    def __init__(self, first_name, last_name, age):
        """comes into existance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """does the same as task8, but to self"""
        dict_desc = {}
        attributes = self.__dict__
        for attr, value in attributes.items():
            if type(value) in [list, dict, str, int, bool]:
                dict_desc[attr] = value
        return dict_desc
