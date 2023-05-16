#!/usr/bin/python3#!/usr/bin/python3


def common_elements(set_1, set_2):
    if isinstance(set_1, dict) is False or isinstance(set_2, dict) is False:
        return None
    if set_1 == {} or set_2 == {}:
        return {}

    commoners =  {item for item in set_1 if item in set_2}
    return commoners