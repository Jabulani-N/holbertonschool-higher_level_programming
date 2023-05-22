#!/usr/bin/python3
"""module that formats a string

craetes 2 new lines after every : ., ? and :.

only accepts string
raises error on non-string
"""


def text_indentation(text):
    """translates in a newline after each '. ', so it's '.\n' instead
    same with ? and :
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    hold_string = text
    dots = str.maketrans(". ",".\n\n")
    quests = str.maketrans("? ","?\n\n")
    cols = str.maketrans(": ",":\n\n")
    hold_string = hold_string.translate(dots)
    hold_string = hold_string.translate(quests)
    hold_string = hold_string.translate(cols)
    # translates all except the last character in the document
    # won't work on last char because it won't have trailing spce
    # also does not translate line-ending delims
    print(hold_string)
