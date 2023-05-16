#!/usr/bin/python3#!/usr/bin/python3


def common_elements(set_1, set_2):

    commoners =  {item for item in set_1 if item in set_2}
    return commoners