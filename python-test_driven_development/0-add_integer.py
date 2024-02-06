#!/usr/bin/python3
"""
    Adds 2 integers
"""


def add_integer(a, b=98):
    """
    Args:
        a (int or float) : First value
        b (int or float) : Second value

    Raises:
        TypeError: If a or b is not in type in or float

    Return:
        a + b
    """
    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return a + b
