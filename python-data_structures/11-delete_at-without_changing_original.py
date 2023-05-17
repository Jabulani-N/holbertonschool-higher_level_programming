#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if isinstance(my_list, list) is False:
        return None
    if idx >= len(my_list) or idx < 0:
        return my_list
    noob = []
    pos = 0
    for content in my_list:
        if pos != idx:
            noob.append(content)
        pos += 1
    my_list = noob.copy()
    return (noob)
