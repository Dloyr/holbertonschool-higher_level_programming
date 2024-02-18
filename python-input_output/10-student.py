#!/usr/bin/python3

"""
class that defines a students
"""


class Student:
    def __init__(self, first_name, last_name, age):
        """
        class that define a student with is first name , last name and his age

        Args:
            first_name: his first name
            last_name: his last name
            age: his age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        method for retrieves a dictionary representation of a Student isntance

        Args:
        attrs: attribute to check if his contained in the list

        Returns:
            the dictionary or the new dictionary(without unknown attributes)
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dictonary = {}

            for attribute in attrs:
                value = getattr(self, attribute, None)
                if value is not None:
                    new_dictonary[attribute] = value

            return new_dictonary
