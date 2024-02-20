#!/usr/bin/python3
"""Module for Base class"""


class Base:
    """Base of all future structures"""
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Contstructor of the class Base

        Args:
            id (int): id of instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
