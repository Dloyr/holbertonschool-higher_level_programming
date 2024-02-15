#!/usr/bin/python3

"""
write an object to a text file with a JSON representation
"""
from json import dumps


def save_to_json_file(my_obj, filename):
    """ write texte file in objects with a JSON representation

        Args:
            my_obj: the object
            filename: the name of the file
    """
    json_object = dumps(my_obj)
    with open(filename, "w") as file:
        return file.write(json_object)
