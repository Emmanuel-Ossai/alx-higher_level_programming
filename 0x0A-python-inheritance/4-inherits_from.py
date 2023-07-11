#!/usr/bin/python3

"""
Uses the inherits_from function to check for instance of a class
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
