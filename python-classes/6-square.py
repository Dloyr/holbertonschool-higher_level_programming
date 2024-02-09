#!/usr/bin/python3

""" defines a Squares"""


class Square:
    """ defines a square with is size """

    def __init__(self, size=0, position=(0, 0)):
        """ define instance of a square with size

        Args:
            size (int): Size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter.

        Args:
            value: position value
        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ instance method for obtain the area of the square """
        return self.size * self.size

    def my_print(self):
        """ instance method for print the square """
        if self.size == 0:
            print()
        else:
            for index in range(self.position[1]):
                print()
            for row in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
