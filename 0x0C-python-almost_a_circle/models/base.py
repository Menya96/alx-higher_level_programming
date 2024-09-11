#!/usr/bin/python3
"""Contains Base class"""
import json
import csv


class Base:
    """Class Base

    Attributes:
        nb_objects: private class atrribute number of objects created
        id: object attribute 'id'
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON string of the list_dictionaries arg

        Args:
            list_dictionaries: a python list containing dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string list_objs to a file

        Args:
            cls: a class
            list_objs: a python list containing Base inheriting objects
        """
        if list_objs is None:
            listDicts = []
        else:
            listDicts = []
            for obj in list_objs:
                listDicts.append(obj.to_dictionary())
        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as myFile:
            myFile.write(Base.to_json_string(listDicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns a python list from a JSON string

        Args:
            json_string: JSON string to load the python list
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            cls: class name
            **dictionary: **kwargs (key-value arguments)
        """
        if cls.__name__ == "Rectangle":
            protoRec = cls(2, 7)
            protoRec.update(**dictionary)
            return protoRec
        elif cls.__name__ == "Square":
            protoSq = cls(2)
            protoSq.update(**dictionary)
            return protoSq

    @classmethod
    def load_from_file(cls):
        """Returns a list of instance objects

        Attributes:
            cls: a class
        """
        fileName = f"{cls.__name__}.json"
        try:
            with open(fileName, "r", encoding="utf-8") as myFile:
                theList = Base.from_json_string(myFile.read())
                return [cls.create(**dct) for dct in theList]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes in CSV

        Args:
            cls: class
            list_objs: list of instances to serialize
        """
        csvfile = f"{cls.__name__}.csv"
        with open(csvfile, "w", newline="") as mycsvFile:
            if len(list_objs) == 0 or list_objs is None:
                mycsvFile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    cellNames = ["id", "width", "height", "x", "y"]
                else:
                    cellNames = ["id", "size", "x", "y"]
                addData = csv.DictWriter(mycsvFile, fieldnames=cellNames)
                for eachObj in list_objs:
                    addData.writerow(eachObj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize in CSV

        Args:
            cls: a class
        """
        fileName = f"{cls.__name__}.csv"
        try:
            with open(fileName, "r", newline="") as acsvFile:
                if cls.__name__ == "Rectangle":
                    cellNames = ["id", "width", "height", "x", "y"]
                else:
                    cellNames = ["id", "size", "x", "y"]
                dlst = csv.DictReader(acsvFile, fieldnames=cellNames)
                dlst = [
                    dict([ky, int(vl)] for ky, vl in dt.items()) for dt in dlst
                ]
                return [cls.create(**dc) for dc in dlst]
        except IOError:
            return []
