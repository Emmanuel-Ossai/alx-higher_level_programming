#!/usr/bin/python3

"""
The class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This shows a square."""

    def __init__(self, size):
        """Starting a new square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
