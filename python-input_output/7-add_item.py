#!/usr/bin/python3
"""moldule is script
takes indeterminate number of input agrs
add them all to a list
dump the list to file
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    data = load_from_json_file('add_item.json')
except:
    data = []
data += sys.argv[1:]

save_to_json_file(data, 'add_item.json')
