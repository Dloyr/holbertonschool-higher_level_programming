#!/usr/bin/python3
import json

"""
return the JSON representation of an object
"""


def to_json_string(my_obj):
    """function to return the JSON representation of my_obj

        Args:
            my_obj: the object
        Returns:
            the JSON representation of my_obj
    """
    return json.dumps(my_obj)
