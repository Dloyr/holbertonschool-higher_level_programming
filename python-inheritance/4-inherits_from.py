#!/usr/bin/python3
"""find if object is an directly or indirectly instance of a inherited class"""


def inherits_from(obj, a_class):
    """return true if obj is instance of inherited a_class, else : False

    Args:
        obj: object to check
        a_class: class

    Returns:
        True or False
    """
    if isinstance(obj, a_class) and not issubclass(a_class, obj.__class__):
        return True
    else:
        return False
