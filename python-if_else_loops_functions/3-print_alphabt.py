#!/usr/bin/python3
import string
for index in range(0, 26):
    if index != 4 and index != 16:
        print("{}".format(string.ascii_lowercase[index]), end="")
