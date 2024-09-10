#!/usr/bin/python3
"""Contains function print_square"""


def print_square(size):
    """Print a square with the hash character

    Args:
        size: length of one side of a square

    Raises:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for r in range(size):
        for c in range(size):
            print("#", end="")
        print("")
