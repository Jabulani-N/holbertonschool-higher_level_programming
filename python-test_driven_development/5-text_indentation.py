#!/usr/bin/python3
"""module that formats a string

craetes 2 new lines after every : ., ? and :.

only accepts string
raises error on non-string
"""


def text_indentation(text):
    """replaces in a newline after each '. ', so it's '.\n' instead
    same with ? and :
    """
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    hold_string = text
    hold_string = hold_string.replace(". ", ".")
    hold_string = hold_string.replace(".", ".\n\n")
    # this method makes it capture and replace spaces after delims
    hold_string = hold_string.replace("? ", "?")
    hold_string = hold_string.replace("?", "?\n\n")
    hold_string = hold_string.replace(": ", ":")
    hold_string = hold_string.replace(":", ":\n\n")

    print(hold_string, end="")
