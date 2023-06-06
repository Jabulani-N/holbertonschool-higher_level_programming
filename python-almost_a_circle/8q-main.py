#!/usr/bin/python3
""" 8-main clone for testing
ability to only run kwargs if there were no positional args """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(10, 10, 10, 10)
    print(r1)

    r1.update(y=1, width=2, x=3, id=89)
    print(r1)

    print("the one with both args and kwargs is next")
    r1.update(3, 5, height=1)
    print(r1)
