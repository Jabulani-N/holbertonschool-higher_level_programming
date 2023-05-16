#!/usr/bin/python3#!/usr/bin/python3


def best_score(a_dictionary):
    bestgirl = None
    if isinstance(a_dictionary, dict):
        charmpoints = max(a_dictionary.values)
        bestgirl = [key for key in a_dictionary if a_dictionary[key] == charmpoints]
    return bestgirl
