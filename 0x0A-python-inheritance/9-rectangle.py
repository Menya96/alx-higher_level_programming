#!/usr/bin/python3
"""Contains classes BaseGeometry and Rectangle"""


class BaseGeometry():
    """Class BaseGeometry"""

    def area(self):
        """Area method

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


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from class BaseGeometry

    Attributes:
        __width: private rectangle's width
        __height: preivate rectangle's height
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def __str__(self):
        """Custom Rectangle __str__ method"""
        return f"[Rectangle] {self.__width}/{self.__height}"

    def area(self):
        """Custom Rectangle area method"""
        return self.__width * self.__height
