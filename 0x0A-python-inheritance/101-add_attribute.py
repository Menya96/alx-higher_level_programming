#!/usr/bin/python3
"""Contains function add_attribute"""


def add_attribute(obj, clsAttribute, atrributeValue):
    """Adds a new attribute to an object if possible

    Raises:
        TypeError: can't add new attribute
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, clsAttribute, atrributeValue)
