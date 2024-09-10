#!/usr/bin/python3
"""Contains matrix_divided function"""


def matrix_divided(matrix, div):
    """Divided all elements of a matrix
    Args:
        matrix: list containing lists
        div: divisor

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats,
            each row of the matrix must be the same size & div must be a number
        ZeroDivisionError: division by zero

    Returns: a new matrix
    """
    matrErr = "matrix must be a matrix (list of lists) of integers/floats"
    if matrix == [] or matrix is None:
        raise TypeError(matrErr)
    for lst in matrix:
        if type(lst) != list:
            raise TypeError(matrErr)
        if len(lst) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for num in lst:
            if type(num) != int and type(num) != float:
                raise TypeError(matrErr)
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda n: round(n/div, 2), lr)) for lr in matrix]
