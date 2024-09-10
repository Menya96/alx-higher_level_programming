#!/usr/bin/python3
"""Contains function text_indentation"""


def text_indentation(text):
    """Print two new lines after `.`, `?` and `:`

    Raises:
        TypeError: text must be a string
    """
    arrSymb = [".", "?", ":"]
    if type(text) != str:
        raise TypeError("text must be a string")
    for symb in arrSymb:
        text = text.replace(symb, symb + "\n\n")
    print("\n".join(s.strip() for s in text.split("\n")), end="")
