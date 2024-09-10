#!/usr/bin/python3
"""Contains function matrix_mul"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices

    Args:
        m_a: matrix one
        m_b: matrix two

    Raises:
        TypeError: m_a & m_b must be a list of lists
        ValueError: m_a & m_b can't be empty
    """
    if type(m_a) is not list:
        TypeError("m_a must be a list")
    elif type(m_b) is not list:
        TypeError("m_b must be a list")

    for lst in m_a:
        if type(lst) is not list:
            TypeError("m_a must be a list of lists")
        if m_a == [] or m_a == [[]]:
            raise ValueError("m_a can't be empty")
        for el in lst:
            if type(el) not in [int, float]:
                TypeError("m_a should contain only integers or floats")
        if len(lst) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for lst in m_b:
        if type(lst) is not list:
            TypeError("m_b must be a list of lists")
        if m_b == [] or m_b == [[]]:
            raise ValueError("m_b can't be empty")
        for el in lst:
            if type(el) not in [int, float]:
                TypeError("m_b should contain only integers or floats")
        if len(lst) != len(m_a[0]):
            raise TypeError("each row of m_b must be of the same size")
