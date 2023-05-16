#!/usr/bin/python3#!/usr/bin/python3


def only_diff_elements(set_1, set_2):

    commoners = {item for item in set_1 if item not in set_2}

    commoners = {item for item in set_2 if item not in set_1}
# done in doubles to collect uniques form both sets
    return commoners
