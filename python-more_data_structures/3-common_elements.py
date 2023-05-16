#!/usr/bin/python3#!/usr/bin/python3


def common_elements(set_1, set_2):
    if isinstance(set_1, list) is False or isinstance(set_2, list) is False:
        return None
    if set_1 == [] or set_2 == []:
        return []

    commoners = []
    for item1 in set_1:
        for item2 in set_2:
            if item1 == item2:
                commoners.append(item1)
    return commoners