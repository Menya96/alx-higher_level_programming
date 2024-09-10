#!/usr/bin/python3
"""Contains function lookup"""


def lookup(obj):
    """Return obj's list of attributes & methods

    Args:
        obj: python object

    Returns: a list of obj's attributes & methods
    """
    return dir(obj)
