#!/usr/bin/python3
"""Contains add_item python script"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json = __import__('6-load_from_json_file').load_from_json_file

    argc = len(sys.argv)
    theFile = "add_item.json"
    try:
        argsList = load_from_json(theFile)
    except FileNotFoundError:
        argsList = []
    for a in range(1, argc):
        argsList.append(sys.argv[a])
    save_to_json_file(argsList, theFile)
