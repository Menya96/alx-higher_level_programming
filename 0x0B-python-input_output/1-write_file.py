#!/usr/bin/python3
"""Conatains function write_file"""


def write_file(filename="", text=""):
    """Writes to a file in UTF8 and returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as myFile:
        return myFile.write(text)
