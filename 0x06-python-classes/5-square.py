#!/usr/bin/python3


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size (int): Size of a side of the square. Default is 0.

        Returns:
            None

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.ue is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my
    """ definition """
    return self.size ** 2

    @property
    def size(self):
        """Getter for the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute.

        Args:
            value (int): The size of a side of the square.

        Returns:
        None

        Raises:
            TypeError: If value is not an integer.
            ValueError: If val_print(self):
        """Prints the square.

        Returns:
            None
        """
        if self.size == 0:
            print()
            return
        for _ in range(self.size):
            print("#" * self.size)
