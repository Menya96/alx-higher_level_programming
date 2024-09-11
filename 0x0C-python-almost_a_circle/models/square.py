#!/usr/bin/python3
"""Contains class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square: inherits from class Rectangle

    Attributes overriden:
        size: the width & height are of the same size 'size'
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size

    def __str__(self):
        """Custom square string"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """Extended size getter from width getter"""
        return super().width

    @size.setter
    def size(self, sizeVl):
        """Extended size setter from width setter"""
        super().width
        self.width = sizeVl
        self.height = sizeVl

    def update(self, *args, **kwargs):
        """Square class extended update method"""
        if len(args) == 0 or args is None:
            for ky, vlue in kwargs.items():
                setattr(self, ky, vlue)

        for aI in range(len(args)):
            if aI == 0:
                self.id = args[0]
            elif aI == 1:
                self.size = args[1]
            elif aI == 2:
                self.x = args[2]
            elif aI == 3:
                self.y = args[3]

    def to_dictionary(self):
        """Returns a dictionary representation of a square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
