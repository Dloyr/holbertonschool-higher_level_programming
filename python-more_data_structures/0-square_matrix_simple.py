#!/usr/bin/python3
# print a list of each items squares of matrix
def square_matrix_simple(matrix=[]):
    matrixSqr = list(map(lambda row: list(map(lambda x: x * x, row)), matrix))
    return matrixSqr
