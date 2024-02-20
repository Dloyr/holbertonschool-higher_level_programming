#!/usr/bin/python3

"""class for make a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor of the class Square

        Args:
            size (int): the size of the square
            x (int): the width of the square
            y (int): the height of the square
            id (int): the numbers of instance of Square
        """
        super().__init__(size, size, x, y, id)
        # call parameters of Rectangle with width and height = size
