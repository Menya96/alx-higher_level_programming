#!/usr/bin/python3
"""Contains function say_my_name"""


def say_my_name(first_name, last_name=""):
    """Prints string with full name

    Args:
        first_name: first name
        last_name: last name

    Raises:
        TypeError: first_name & last_name must be strings
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
