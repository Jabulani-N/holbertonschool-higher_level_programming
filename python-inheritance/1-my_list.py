#!/usr/bin/python3
"""module holds a class that inherits class list

it will replicate the funciton of the 'sorted' command
"""


class MyList(list):
    """inherits list and adds a method"""

    def print_sorted(self):
        """use sorted"""

        return sorted(self)
