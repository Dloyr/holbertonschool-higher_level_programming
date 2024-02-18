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

    def to_json(self):
        """
        method for retrieves a dictionary representation of a Student isntance
        """
        return self.__dict__
