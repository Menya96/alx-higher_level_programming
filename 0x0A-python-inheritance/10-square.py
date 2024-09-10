#!/usr/bin/python3
"""Contains classes BaseGeometry, Rectangle and Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square which inherits from class Rectangle

    Args:
        size: size of one side of the square
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Custom Square area method"""
        return self.__size ** 2
