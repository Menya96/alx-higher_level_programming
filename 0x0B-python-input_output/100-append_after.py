#!/usr/bin/python3
"""Contains function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line text after each line containing a specific string"""
    with open(filename, "r", encoding="utf-8") as aFile:
        allLines = aFile.readlines()
        newLines = []
        for eachLine in allLines:
            newLines.append(eachLine)
            if search_string in eachLine:
                newLines.append(new_string)

    with open(filename, "w", encoding="utf-8") as myFile:
        for aLine in newLines:
            myFile.write(aLine)
