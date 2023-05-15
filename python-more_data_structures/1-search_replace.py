#!/usr/bin/python3#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if isinstance(my_list, list) is False:
        return None
    if my_list == []:
        return my_list
    noob = []
    for item in my_list:
        if item == search:
            noob.append(replace)
        else:
            noob.append(item)
    return noob
