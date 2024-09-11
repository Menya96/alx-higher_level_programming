#!/usr/bin/python3
"""Contains function append_write"""


def append_write(filename="", text=""):
    """Appends string to end of a file & returns number of chars added"""
    with open(filename, "a", encoding="utf-8") as myfile:
        return myfile.write(text)
