#!/usr/bin/python3

"""
This is a python code that contains lookup function
"""


def lookup(obj):

    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object to inspect.

    Returns:
        list: A list of available attributes and methods.

    """
    return dir(obj)
