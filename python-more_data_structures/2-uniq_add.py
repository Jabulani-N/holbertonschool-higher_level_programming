#!/usr/bin/python3#!/usr/bin/python3


def uniq_add(my_list=[]):
    if my_list == [] or isinstance(my_list, list) is False:
        return 0
    used = []
    total = 0
    repeat = False
    for listitem in my_list:
        for useditem in used:
            if listitem == useditem:
                repeat = True
        if repeat is False:
            used.append(listitem)
            total += listitem
        repeat = False
    return total
