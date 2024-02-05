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
        if (not isinstance(self.__size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property  # declare a properties
    def size(self):
        """ class method for take the size of the square """
        return self.__size

    @size.setter  # modify the properties
    def size(self, value):
        """ class method for modify value of size """
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ class method for obtain the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ class method for print the square """
        for row in range(self.__size):
            print("#" * self.__size)
