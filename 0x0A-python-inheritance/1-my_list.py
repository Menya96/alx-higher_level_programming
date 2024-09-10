#!/usr/bin/python3
"""Contains class MyList"""


class MyList(list):
    """Inherits from class list"""
    def print_sorted(self):
        """Print a list in ascending order"""
        print(sorted(self))
