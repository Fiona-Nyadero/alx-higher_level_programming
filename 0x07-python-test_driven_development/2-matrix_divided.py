#!/usr/bin/python3
"""Module (Function) matrix_divided"""


def matrix_divided(matrix, div):
    """Returns a new matrix"""

    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for rw in matrix:
        if len(rw) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for cl in rw:
            if type(cl) is not int and type(cl) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    len_rws = []
    for rw in matrix:
        len_rws.append(len(rw))
    if not all(cl == len_rws[0] for cl in len_rws):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    the_matrix = [[round(cl / div, 2) for cl in rw] for rw in matrix]

    return the_matrix
