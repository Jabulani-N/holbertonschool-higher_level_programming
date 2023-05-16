#!/usr/bin/python3#!/usr/bin/python3


def only_diff_elements(set_1, set_2):

    commoners = {item for item in set_1 not in item in set_2}
    commoners += {item2 for item2 in set_2 not in item2 in set_1}
 # done in doubles in case one is larger
    return commoners
