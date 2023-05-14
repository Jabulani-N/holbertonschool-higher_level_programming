#!/usr/bin/python3#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == [] or isinstance(my_list, list) is False:
        return None
    maxi = my_list[0]
    for content in my_list:
        if content > maxi:
            maxi = content
    return maxi
