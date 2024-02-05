#!/usr/bin/python3

""" defines a Squares"""


class Square:
    """ defines a square with is size """

    def __init__(self, size=0):
        """ define instance of a square with size

        Args:
            size (int): Size of the square
        """

        self.__size = size
        if (size is not int(size)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        """ class method for obtain the area of the square """
        return self.__size * self.__size
