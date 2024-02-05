#!/usr/bin/python3

""" defines a Squares"""


class Square:
    """ defines a square with is size """

    def __init__(self, size=0, position=(0, 0)):
        """ define instance of a square with size

        Args:
            size (int): Size of the square
            position (tuple): position in the square
        """

        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__position = position

    @property  # declare a properties
    def size(self):
        """ class method for take the size of the square """
        return self.__size

    @size.setter  # modify the properties
    def size(self, value):
        """ class method for modify value of size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ class method to take the position in the square """
        return self.__position

    @size.setter
    def position(self, value):
        """ class method for modify the value of position """
        self.__position = value
        if self.__position[:2] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """ class method for obtain the area of the square """
        return self.__size * self.__size

    def my_print(self):
        """ class method for print the square """
        if self.__size == 0:
            print("")

        for index in range(self.__position[1]):
            print()
        for row in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
