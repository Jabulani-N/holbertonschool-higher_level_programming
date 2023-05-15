#!/usr/bin/python3#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # approach: translate search to be replaced with replace
    # potential issues: if search = 2, may replace 22 with replacereplace
    if isinstance(my_list, list) is False:
        return None
    if my_list == []:
        return my_list
    noob = my_list.translate({ord(search): replace})
    return noob
