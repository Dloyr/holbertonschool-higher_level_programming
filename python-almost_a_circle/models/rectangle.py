#!/usr/bin/python3

from models.base import Base

"""
class for make a rectangle
"""


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor for the rectangle

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: value of width
            y: value of height
            id: the number of instances in class Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for width

        Returns:
            private attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for width

        Args:
            value (int): value of width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be > 0
        """
        if type(value) is not int:
            raise TypeError(f"width must be an integer")
        if value < 1:
            raise ValueError(f"width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
        Getter method for height

        Returns:
            the private attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for height

        Args:
            value (int): value of height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be > 0
        """
        if type(value) is not int:
            raise TypeError(f"height must be an integer")
        if value < 1:
            raise ValueError(f"height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
        Getter method for x

        Returns:
            the private attribute x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for x

        Args:
            value (int): value of x

        Raises:
            TypeError: x must be an integer
            ValueError: x must be >= 0
        """
        if type(value) is not int:
            raise TypeError(f"x must be an integer")
        if value < 0:
            raise ValueError(f"x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
        Getter method for y

        Returns:
            the private attribute y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for y

        Args:
            value (int): value of y

        Raises:
            TypeError: y must be an integer
            ValueError: y must be >= 0
        """
        if type(value) is not int:
            raise TypeError(f"y must be an integer")
        if value < 0:
            raise ValueError(f"y must be >= 0")

        self.__y = value

    def area(self):
        """method for calculate the are of the rectangle"""
        return self.height * self.width or self.x * self.y

    def display(self):
        """method for prints the rectangle"""
        for line in range(self.height):
            print("#" * self.width)

    def __str__(self) -> str:
        """method for print the string representation of a rectangle"""
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}"
        )
