#!/usr/bin/python3
"""Contains class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle: Inherits from class Base

    Attributes (extra from Base):
        width: rectangle's width
        height: rectangle's height
        x: attribute x
        y: attribute y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width attribute getter function"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter function

        Raises:
            TypeError: attribute must be an integer
            ValueError: width/height must be > 0 & x/y must be >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter function"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter function

        Raises:
            TypeError: attribute must be an integer
            ValueError: width/height must be > 0 & x/y must be >= 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X getter function"""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter function

        Raises:
            TypeError: attribute must be an integer
            ValueError: width/height must be > 0 & x/y must be >= 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y getter function"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter function

        Raises:
            TypeError: attribute must be an integer
            ValueError: width/height must be > 0 & x/y must be >= 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates and returns the rectangle's area"""
        return self.height * self.width

    def display(self):
        """Prints the rectangle using '#' and spaces"""
        for emp in range(self.y):
            print("")

        for row in range(self.height):
            for space in range(self.x):
                print(" ", end="")
            for col in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Custom rectangle __str__ method"""
        rS = "[Rectangle]"
        rid = f"({self.id})"
        return f"{rS} {rid} {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute

        Arguments:
            *args: iterable tuple of arguments passed in
            **kwargs: dictionary arguments object
        """
        if len(args) == 0 or args is None:
            for k, vl in kwargs.items():
                setattr(self, k, vl)

        for ai in range(len(args)):
            if ai == 0:
                self.id = args[0]
            elif ai == 1:
                self.width = args[1]
            elif ai == 2:
                self.height = args[2]
            elif ai == 3:
                self.x = args[3]
            elif ai == 4:
                self.y = args[4]

    def to_dictionary(self):
        """Returns a dictionary representation of a rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
