#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if isinstance(my_list, list) is False:
        return None
    if idx >= len(my_list) or idx < 0:
        return my_list
    for i in range(idx, len(my_list)):
        if i + 1 < len(my_list):
            my_list[i] = my_list[i + 1]
        else:
            my_list.remove(my_list[i])
    return (my_list)
