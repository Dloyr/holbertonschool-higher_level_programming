#!/usr/bin/python3
"""Module for Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Convert a list of dicitonaries to a JSON string

        Args:
            list_dictionaries (list): the list of dicitonaries

        Return:
            the JSON string
        """

        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method for save the list of objects of a class in a JSON file

        Args:
            cls (class): the class
            list_objs (list): the list of objects of the class
        """
        if list_objs is None:
            list_objs = []

        objects_dictionary = [objects.to_dictionary() for objects in list_objs]
        json_string = Base.to_json_string(objects_dictionary)

        with open(cls.__name__ + ".json", "w", encoding='utf-8') as file:
            file.write(json_string)
