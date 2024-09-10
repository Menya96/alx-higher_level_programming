#!/usr/bin/python3
"""Contains function is_same_class"""


def is_same_class(obj, a_class):
    """Checks if the obj is an instance of a_class

    Args:
        obj: python object
        a_class: python class

    Returns: True or False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
