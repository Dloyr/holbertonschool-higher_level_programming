#!/usr/bin/python3
"""
    divide each items of matrix per a value
"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix: the variable to the matrix
        div: the value for the division of the matrix

    Raise:
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Return:
        a new matrix with the result of the divisions
    """
    new_matrix = []
    er_message = "matrix must be a matrix (list of lists) of integers/floats"

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if (
        not all(isinstance(row, list) and
                all(isinstance(element, (int, float)) for element in row)
                for row in matrix)
    ):
        raise TypeError(er_message)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)

    return new_matrix
