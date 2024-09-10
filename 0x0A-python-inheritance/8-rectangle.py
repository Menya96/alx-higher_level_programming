#!/usr/bin/python3
"""Contains classes BaseGeometry and Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
