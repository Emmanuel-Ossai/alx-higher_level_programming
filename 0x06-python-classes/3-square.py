#!/usr/bin/python3


"""
A module that defines the Square class.

This module provides a class called Square with private instance attribute.
"""


class Square:
    """Represents a square with a private instance attribute 'size'.

    Attributes:
        __size (int): size of the square
    """

    def __init__(self, size=0):
        """
        Initializes a square with a given size.

        Args:
            size (int): Size of the square. Default is 0.

        Raises:
            ValueError: If size is less than 0.
            TypeError: If size is not an integer.
        """
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
