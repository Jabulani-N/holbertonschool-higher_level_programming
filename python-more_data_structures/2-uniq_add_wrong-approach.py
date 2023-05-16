#!/usr/bin/python3#!/usr/bin/python3


def uniq_add(my_list=[]):
    if my_list == [] or isinstance(my_list, list) is False:
        return 0
    used = []
    twice = []
    total = 0
    repeat = False
    for listitem in my_list:
        for useditem in used:
            if listitem == useditem:
                twice.append(listitem)
                repeat = True
        if repeat is False:
            used.append(listitem)
        repeat = False
# we now have a list of used values and repeat values
# now we just total all used values that are not repeats
# we could use the original list if we wanted.
    for useditem in used:
        for twiceitem in twice:
            if useditem == twiceitem:
                repeat = True
        if repeat is False:
            total += useditem
        repeat = False
    return total
