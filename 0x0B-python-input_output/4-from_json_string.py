#!/usr/bin/python3
"""Contains function from_json_string"""
import json


def from_json_string(my_string):
    """Returns a python object from a JSON string"""
    return json.loads(my_string)
