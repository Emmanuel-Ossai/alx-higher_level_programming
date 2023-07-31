#!/usr/bin/python3

"""This is a Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
            TypeError: If x or y is not an integer.
            ValueError: If x or y is less than 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the Rectangle.

        Args:
            value (int): The new width value to set for the Rectangle.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the Rectangle.

        Args:
            value (int): The new height value to set for the Rectangle.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get or set the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Set the x coordinate of the Rectangle.

        Args:
            value (int): The new x coordinate value to set for the Rectangle.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get or set the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Set the y coordinate of the Rectangle.

        Args:
            value (int): The new y coordinate value to set for the Rectangle.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """
        Update the Rectangle attributes.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute.
                - 2nd argument represents width attribute.
                - 3rd argument represents height attribute.
                - 4th argument represents x attribute.
                - 5th argument represents y attribute.
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the Rectangle.

        Returns:
            dict: A dictionary representation of the Rectangle object.
                Contains keys: 'id', 'width', 'height', 'x', and 'y'.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Return the string representation of the Rectangle.

        Returns:
            str: A formatted string representation of the Rectangle object.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
