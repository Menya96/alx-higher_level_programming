#!/usr/bin/python3
"""Contains classes BaseGeometry, Rectangle and Square"""


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


class Square(Rectangle):
    """Class Square which inherits from class Rectangle

    Args:
        size: size of one side of the square
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Custom Square area method"""
        return self.__size ** 2

    def __str__(self):
        """Custom string for the Square class"""
        return f"[Square] {self.__size}/{self.__size}"
