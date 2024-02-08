#!/usr/bin/python3

"""defines a rectangle"""


class Rectangle:
    """rectangle is empty"""
    def __init__(self, width=0, height=0):
        """ defines instance of a rectangle with is width and height

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """class method for take the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """class method for modify the value of width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")

        self.__width = value

    @property
    def height(self):
        """class method for take the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """class method for modify the value of height"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")

        self.__height = value
