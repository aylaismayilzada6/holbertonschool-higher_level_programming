#!/usr/bin/python3
"""
Script that adds all command-line arguments to a Python list
and saves them to a JSON file.

If the file does not exist, it is created.
If the file exists, its content is loaded and updated.
"""

import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing list if file exists, otherwise initialize empty list
if path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add command-line arguments (excluding script name)
my_list.extend(sys.argv[1:])

# Save updated list back to JSON file
save_to_json_file(my_list, filename)
