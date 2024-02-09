#!/usr/bin/python3

""" defines a Squares"""


class Square:
    """ defines a square with is size """

    def __init__(self, size=0):
        """ define instance of a square with size

        Args:
            size (int): Size of the square
        """
        self.size = size

    @property  # declare a properties
    def size(self):
        """size getter"""
        return self.__size

    @size.setter  # modify the properties
    def size(self, value):
        """size setter.

        Args:
            value: size value
        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
        """
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ instance method for obtain the area of the square """
        return self.size * self.size
