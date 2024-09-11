#!/usr/bin/python3
"""Contains class Student"""


class Student():
    """Defines a student

    Attributes:
        first_name: student's first name
        last_name: student's last name
        age: student's age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a student"""
        selfDict = self.__dict__
        if attrs is not None:
            newAttrs = {}
            for atb in attrs:
                if atb in selfDict:
                    newAttrs[atb] = selfDict[atb]
            return newAttrs

        return selfDict
