#!/usr/bin/python3
"""Contains class MyInt"""


class MyInt(int):
    """Class MyInt inherits from class int"""
    def __eq__(self, other):
        """Custom inverted equal to dunder operation"""
        return self.real != other

    def __ne__(self, other):
        """Custom inverted not equal to dunder operation"""
        return self.real == other
