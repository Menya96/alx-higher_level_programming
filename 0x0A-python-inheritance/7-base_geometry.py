#!/usr/bin/python3
"""Contains class BaseGeometry"""


class BaseGeometry():
    """Class BaseGeometry"""

    def area(self):
        """Unimplemented area method

        Raises:
            Exception: area() is not implemented
            TypeError: name must be an integer
            ValueError: name must be greater than 0
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
