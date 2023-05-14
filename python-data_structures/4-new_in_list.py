#!/usr/bin/python3#!/usr/bin/python3


# largely copied from task2
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list) is False:
        return None
    dupe_list = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return dupe_list
    else:
        dupe_list[idx] = element
        return dupe_list
