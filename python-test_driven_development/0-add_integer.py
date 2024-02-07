#!/usr/bin/python3
"""
    Adds 2 integers
    Args:
        a (int or float) : First value and b (int or float) : Second value
"""


def add_integer(a, b=98):
    """
    Return: a + b
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
