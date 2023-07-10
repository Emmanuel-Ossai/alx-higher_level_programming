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

    Examples:
        >>> obj = SomeClass()
        >>> attributes = lookup(obj)
        >>> print(attributes)
        ['attribute1', 'method1', 'method2']

    """
    attributes = []
    for attr in dir(obj):
        if not attr.startswith('__'):
            attributes.append(attr)
    return attributes
