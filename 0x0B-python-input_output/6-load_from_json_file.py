#!/usr/bin/python3
"""Contains function load_from_json_file"""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file"""
    with open(filename, "r", encoding="utf-8") as myFile:
        return json.load(myFile)
