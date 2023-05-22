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
    hold_string.translate({ord('. '): '.\n\n'})
    hold_string.translate({ord('? '): '?\n\n'})
    hold_string.translate({ord(': '): ':\n\n'})
    # translates all except the last one in the document
    # also does not translate line-ending delims
    print(hold_string)
