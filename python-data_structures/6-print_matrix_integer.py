#!/usr/bin/python3

# print a list in a list (double entry table) of integers
def print_matrix_integer(matrix=[[]]):
    for index_row in matrix:
        for index_line in index_row:
            print(index_line, end=" ")
        print()
