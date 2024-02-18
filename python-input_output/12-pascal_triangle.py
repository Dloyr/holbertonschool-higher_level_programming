#!/usr/bin/python3

def pascal_triangle(n):
    """
    function to create a pascal triangle

    Args:
        n: the size of the pascal triangle

    Returns:
        the triangle
    """
    triangle = []
    first_line = [1]

    triangle.append(first_line)

    for line in range(1, n):
        new_line = [1]

        for column in range(1, len(first_line)):
            new_line.append(first_line[column - 1] + first_line[column])

        new_line.append(1)
        first_line = new_line
        triangle.append(new_line)

    return triangle
