#!/usr/bin/python3
"""Contains function read_file"""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints it to STDOUT"""
    with open(filename, "r", encoding="utf-8") as myFile:
        for eachLine in myFile.readlines():
            print(eachLine, end="")
