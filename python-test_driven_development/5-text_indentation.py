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
        raise TypeError ("text must be a string")
    holdstring = text
    hold_string.translate({ord('. '): '.\n\n'})
    hold_string.translate({ord('? '): '?\n\n'})
    hold_string.translate({ord(': '): ':\n\n'})
    # translates all except the last one in the document
    # also doe snot translate line-ending delims
