#!/usr/bin/python3
"""Contains function pascal_triangle"""


def pascal_triangle(n):
    """List of lists of integers representing Pascal's triangle

    Args:
        n: integer

    Returns: a list of lists of integers
    """
    if n <= 0:
        return []
    tri = [[1]]
    while len(tri) is not n:
        nt = tri[-1]
        ntLen = len(nt)
        tLst = [1]
        for num in range(ntLen - 1):
            tLst.append(nt[num] + nt[num + 1])
        tLst.append(1)
        tri.append(tLst)
    return tri
