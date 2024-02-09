#!/usr/bin/python3

"""defines a rectangle"""


class Rectangle:
    """class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """ defines instance of a rectangle with is width and height

        Args:
            width : width of the rectangle.
            height : height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter.

        Args:
            value: width value.
        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter.

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter.

        Args:
            value: height value.
        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value
