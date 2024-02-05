#!/usr/bin/python3

# use the method size for calculate the aera of size
class Square:
    def __init__(self, size=0):
        self.__size = size
        if (not isinstance(self.__size, int)):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    @property  # declare a properties
    def size(self):  # is a method for find size
        return self.__size

    @size.setter  # modify the properties
    def size(self, value):  # is a method for modify value of size
        if (not isinstance(value, int)):
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size
