#!/usr/bin/python3#!/usr/bin/python3


def best_score(a_dictionary):
    bestgirl = 'None'
    if isinstance(a_dictionary, dict) and len(a_dictionary) > 0:
        charmpoints = max(a_dictionary.values())
        for key in a_dictionary:
            if a_dictionary[key] == charmpoints:
                bestgirl = key
    return bestgirl
