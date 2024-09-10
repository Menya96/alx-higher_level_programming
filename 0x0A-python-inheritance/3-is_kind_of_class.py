#!/usr/bin/python3
"""Contains function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Checks if obj is an instance of or inherits from a_class

    Args:
        obj: object argument
        a_class: class argument

    Return: True if instance & False if not
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
