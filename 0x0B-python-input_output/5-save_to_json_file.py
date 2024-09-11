#!/usr/bin/python3
"""Contains function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes a JSON representation of a Python object to a text file"""
    with open(filename, "w", encoding="utf-8") as myFile:
        json.dump(my_obj, myFile)
