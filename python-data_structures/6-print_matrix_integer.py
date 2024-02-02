#!/usr/bin/python3

# print a list in a list (double entry table) of integers
def print_matrix_integer(matrix=[[]]):
    for index_row in range(len(matrix)):
        for index_column in range(len(matrix[index_row])):
            print("{:d}".format(matrix[index_row][index_column]), end="")
            if index_column != (len(matrix[index_row]) - 1):
                print(" ", end="")

        print()
