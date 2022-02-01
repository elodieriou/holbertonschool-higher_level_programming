#!/usr/bin/python3
"""
The module define a script that adds all arguments to a Python list,
and save them to a file.
"""
import sys
import os
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
my_list = []
if os.path.exists('add_item.json') is False:
    save_to_json_file(my_list, filename)
my_list = load_from_json_file(filename)
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
save_to_json_file(my_list, filename)
