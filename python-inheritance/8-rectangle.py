#!/usr/bin/python3
"""defines a class BaseGeometry"""


class BaseGeometry:
    """class is empty"""
    pass

    def area(self):
        """instance method for calculate the area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """instance method for verify if integer is valid"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """inherited class for make a rectangle"""
    def __init__(self, width, height):
        """ define instance of a rectange with his width and height

        Args:
            width: private attribute width
            height: private attribute height
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
