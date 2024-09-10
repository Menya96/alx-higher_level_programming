#!/usr/bin/python3
"""Contains function inherits_from"""


def inherits_from(obj, a_class):
    """Checks if obj is a subclass of a_class

    Args:
        obj: object argument
        a_class: class argument

    Return: True if a subclass & False if not
    """
    if issubclass(type(obj), a_class) and a_class != type(obj):
        return True
    else:
        return False
