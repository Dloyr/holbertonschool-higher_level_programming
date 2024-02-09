#!/usr/bin/python3

""" defines a Squares"""


class Square:
    """ defines a square with is size """

    def __init__(self, size):
        """ define instance of a square with size

        Args:
            size (int): Size of the square
        """
        self.__size = size
