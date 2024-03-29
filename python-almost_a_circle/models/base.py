#!/usr/bin/python3
"""Module for Base class"""
import json
from os import path


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
        Class method for save the list of objects of a class in a JSON file

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

    @staticmethod
    def from_json_string(json_string):
        """
        Static method for convert a JSON string to a list of dictionaries

        Args:
            json_string (str): the string to convert

        Returns:
            the list of dictionaries
        """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Classmethod for return the instance with all attributes already set

        Args:
            cls (class): the class we use his instance
            dictionary (dict): the dictionary of all attributes of the class

        Return:
            the instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            new_rectangle = cls(5, 2)
        else:
            new_rectangle = cls(10)
        new_rectangle.update(**dictionary)

        return new_rectangle

    @classmethod
    def load_from_file(cls):
        """
        Class method for return a list of instances from a JSON file

        Args:
            cls (class): all class, parent and child

        Returns:
            the list of instances
        """
        filename = cls.__name__ + ".json"

        if not path.isfile(filename):
            return []

        with open(filename, "r", encoding='utf-8') as file:
            json_string = file.read()

        dictionary_list = cls.from_json_string(json_string)

        return [cls.create(**dictionary) for dictionary in dictionary_list]
