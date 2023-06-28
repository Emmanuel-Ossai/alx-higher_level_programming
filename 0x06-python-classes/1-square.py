#!/usr/bin/python3


"""A module that defines the Square class."""


class Square:
    """Represents a square.

    Attributes:
        __size (int): size of a side of the square
    """

    def __init__(self, size):
        """Initialize a new Square object.

        Args:
            size (int): size of a side of the square

        Returns:
            None
        """
        self.__size = size
