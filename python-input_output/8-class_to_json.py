#!/usr/bin/python3

"""
dictionary description with simple data for JSON serialization
"""


def class_to_json(obj):
    """
    function for return a dictionary description of obj in JSON file

    Args:
        obj: object to return

    Returns:
        dictionary descritption
    """
    return obj.__dict__
