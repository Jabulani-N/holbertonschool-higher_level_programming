#!/usr/bin/python3
"""moldule 3-say_my_name

this module prints a sentance based on input argument stinrg

requires a string input, or an error will be thrown
"""

def say_my_name(first_name, last_name=""):
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is", first_name, last_name)