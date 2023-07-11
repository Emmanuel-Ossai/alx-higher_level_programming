#!/usr/bin/python3

"""
Class BaseGeometry.
"""


class BaseGeometry:
    """
    A class with public instance methods
    """

    def area(self):
        """area set"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Check to confirm that the parameter is integer.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
