#!/usr/bin/python3


"""
Module: square

Define a class Square.

Classes:

Square: Represent a square.
"""


class Square:
    """Represent a square."""


def __init__(self, size=0, position=(0, 0)):
    """
    Initialize a new square.

    Args:
        size (int): The size of the new square.
        position (tuple): The position of the new square.
    """
    self.size = size
    self.position = position


@property
def size(self):
    """Get/set the current size of the square."""
    return self.__size


@size.setter
def size(self, value):
    """
    Set the size of the square.

    Args:
        value (int): The value to set as the size.
    Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than 0.
    """
    if not isinstance(value, int):
        raise TypeError("size must be an integer")
    elif value < 0:
        raise ValueError("size must be >= 0")
    self.__size = value


@property
def position(self):
    """Get/set the current position of the square."""
    return self.__position


@position.setter
def position(self, value):
    """
    Set the position of the square.

    Args:
        value (tuple): The value to set as the position.
    Raises:
        TypeError: If the value is not a tuple of 2 positive integers.
    """
    if (
        not isinstance(value, tuple)
        or len(value) != 2
        or not all(isinstance(num, int) for num in value)
        or not all(num >= 0 for num in value)
    ):
        raise TypeError("position must be a tuple of 2 positive integers")
    self.__position = value


def area(self):
    """
    Calculate the area of the square.

    Returns:
        int: The area of the square.
    """
    return self.__size ** 2


def my_print(self):
    """Print the square with the '#' character."""
    if self.__size == 0:
        print("")
        return

    for _ in range(self.__position[1]):
        print("")

    for _ in range(self.__size):
        print(" " * self.__position[0], end="")
        print("#" * self.__size)


def __str__(self):
    """
    Return the string representation of the square.

    Returns:
        str: The string representation of the square.
    """
    result = ""
    if self.__size != 0:
        result += "\n" * self.__position[1]
    for _ in range(self.__size):
        result += " " * self.__position[0]
        result += "#" * self.__size
        if _ != self.__size - 1:
            result += "\n"
    return result
