#!/usr/bin/python3

# defines a class Square who return the square area
class Square:
    def __init__(self, size=0):
        self.__size = size
        if (size is not int(size)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
