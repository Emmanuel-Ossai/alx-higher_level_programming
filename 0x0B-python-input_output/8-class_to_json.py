#!/usr/bin/python3

"""
Contains a function that returns the dictionary description
with simple data structure
"""


def class_to_json(obj):
    """
    Return the dictionary description of an object with a simple data
    structure for JSON serialization.

    """
    if not isinstance(obj, type):
        # Checks if obj is not a Class instance, raise a TypeError
        raise TypeError("obj must be an instance of a Class")

    # Checks and get the attributes of the object
    attributes = obj.__dict__

    # Create an empty dictionary to store the serialized attributes
    serialized = {}

    # Iterate over each attribute
    for attr, value in attributes.items():
        # Check the type of the attribute and serialize accordingly
        if isinstance(value, (list, dict, str, int, bool)):
            serialized[attr] = value

    return serialized
