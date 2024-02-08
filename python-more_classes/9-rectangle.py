#!/usr/bin/python3

"""defines a rectangle"""


class Rectangle:
    """rectangle is empty"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ defines instance of a rectangle with is width and height

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        """property for retrieve the attribute height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter for modify the value of height"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >=0")

        self.__height = value

    def area(self):
        """instance method for get the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """instance method for get the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0

        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """instance method for the representation of strings of rectangle"""
        rectangle_string = ""

        if self.__width == 0 or self.__height == 0:
            return ""

        for index_a in range(self.__height):
            for index_b in range(self.__width):
                rectangle_string += str(self.print_symbol)
            rectangle_string += "\n"

        return rectangle_string[:-1]

    def __repr__(self):
        """instance method for the printable representation of an object"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        """instance method for delete the instantate object"""
        print("Bye rectangle ...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method for compare two rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.perimeter() > rect_2.perimeter():
            return rect_1
        elif rect_1.perimeter() < rect_2.perimeter():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """class method for return a square instance"""
        return cls(size, size)
