#!/usr/bin/python3

"""
Class for defines a base for making square and rectangle
"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Contstructor of the class Base

        Args:
            id (int): the number of instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
