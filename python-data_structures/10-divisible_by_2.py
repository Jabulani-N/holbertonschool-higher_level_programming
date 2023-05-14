#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == [] or isinstance(my_list, list) is False:
        return None
    noob = my_list.copy()
    pos = 0
    for content in my_list:
        if content % 2 == 0:
            noob[pos] = True
        else:
            noob[pos] = False
        pos += 1
    return noob
