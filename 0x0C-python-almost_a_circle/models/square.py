#!/usr/bin/python3
"""This is a square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the Square.

        Args:
            value (int): The new size value to set for the Square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square attributes.

        Args:
            *args (int): New attribute values.
                - 1st argument represents id attribute.
                - 2nd argument represents size attribute.
                - 3rd argument represents x attribute.
                - 4th argument represents y attribute.
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square.

        Returns:
            dict: A dictionary representation of the Square object.
                Contains keys: 'id', 'size', 'x', and 'y'.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return the string representation of a Square.

        Returns:
            str: A formatted string representation of the Square object.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

