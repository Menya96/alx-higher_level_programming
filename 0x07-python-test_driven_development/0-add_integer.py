#!/usr/bin/python3
"""Contains function add_integer"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
        a: integer 1
        b: integer 2

    Raises:
        TypeError: a / b must be an integer

    Returns: sum of a and b
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
