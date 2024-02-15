#!/usr/bin/python3
"""defines if the object is instance of a class"""


def is_kind_of_class(obj, a_class):
    """Return true if object is instance of a_class or False or not

    Args:
        obj: object to check
        a_class: the class

    Returns:
        True or False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
