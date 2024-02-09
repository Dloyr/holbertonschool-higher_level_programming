#!/usr/bin/python3

"""defines a rectangle"""


class Rectangle:
    """rectangle is empty"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return self.width * 2 + self.height * 2

    def __str__(self):
        rectangle_string = ""
        if self.width == 0 or self.height == 0:
            return ""

        for index_a in range(self.height):
            for index_b in range(self.width):
                rectangle_string += "#"
            rectangle_string += "\n"

        return rectangle_string[:-1]

    def __repr__(self):
        """instance method for the printable representation of an object"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """class method for delete the instantate object"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
