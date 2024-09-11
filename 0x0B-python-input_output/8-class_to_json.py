#!/usr/bin/python3
"""Contains function class_to_json"""


def class_to_json(obj):
    """Returns a dictionary description of a class object"""
    objDict = obj.__dict__
    return objDict
