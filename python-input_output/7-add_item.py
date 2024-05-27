#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""



import sys
import os
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file


filename = "add_item.json"
args = sys.argv[1:]

if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

items.extend(args)

save_to_json_file(items, filename)
