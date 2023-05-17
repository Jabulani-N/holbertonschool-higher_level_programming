#!/usr/bin/python3

class dog:

    def __init__(self, starting_name, starting_breed, starting_birthyear):
        self.name = starting_name
        self.breed = starting_breed
        self.birthyear = starting_birthyear

    def get_name(self):
        return self.name

    def set_name(self,input_name):
        self.name = input_name

    def get_breed(self):
        return self.breed

    def get_age(self):
        from datetime import datetime
#  datetime is used for the get_age fun.
        return (datetime.now().year - self.birthyear)

    def bark():
        print("borrk")
