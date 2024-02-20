#!/usr/bin/python3
"""Module for a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class for make a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor of the class Square

        Args:
            size (int): the size of the square
            x (int): the width of the square
            y (int): the height of the square
            id (int): id of instances of Square
        """
        super().__init__(size, size, x, y, id)
        # call parameters of Rectangle with width and height = size

    @property
    def size(self):
        """
        Getter method for size

        Returns:
            self.width and self.height
        """
        return self.width and self.height

    @size.setter
    def size(self, value):
        """
        Setter method for size

        Args:
            value (int): value of size
        """
        self.width = value
        self.height = value
