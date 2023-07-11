#!/usr/bin/python3

"""
This is a function that adds a new attribute to an object if it’s possible:
"""


def add_new_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if possible.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)


if __name__ == "__main__":
    """
    Module defining the add_new_attribute function.
    """
    obj = object()
    add_new_attribute(obj, "new_attribute", 42)
    print(obj.new_attribute)  # Output: 42
