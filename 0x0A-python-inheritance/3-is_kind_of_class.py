#!/usr/bin/python3

"""
Uses the is_kind_of_class function to check the class
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if it is an instance of a class
    that inherited from,the specified class.
    """

    if isinstance(obj, a_class):
        return True
    return False
