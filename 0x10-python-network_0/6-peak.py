#!/usr/bin/python3
"""Find a peak module"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted ints"""
    li = list_of_integers
    p = 0
    ln = len(list_of_integers)
    d = int(((ln - p) // 2) + p)
    if ln == 1:
        return li
    if ln == 2:
        return max(li)
    if li[d] >= li[d - 1] and li[d] >= li[d + 1]:
        return li[d]
    if d > 0 and li[d] < li[d + 1]:
        return find_peak(li[d:])
    if d > 0 and li[d] < li[d - 1]:
        return find_peak(li[:d])
