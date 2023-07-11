#!/usr/bin/python3

"""
The class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Compute the area of the geometry object.

        Raises:
            Exception: Indicates that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")


class Rectangle(BaseGeometry):
    """
    Class representing a rectangle.
    """
    return self.__width * self.__height


def __str__(self):
    """Return the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle inectangle.
    """

    def __init__(self, width, height):
        """Initialize a Rectangle instance with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            ValueError: If width or height is not a positive integer.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Compute the area of the rectangle.

        Returns:
            int: Th the format [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """Class representing a square.

    Attributes:
        __side (int): The length of each side of the square.
    """

    def __init__(self, side):
        """Initialize a Square instance with side length.

        Args:
            side (int): The length of each side of the square.

        Raises:
            ValueError: If side is not a positive integer.
        """
        self.__side = side
        self.integer_validator("side", side)
        super().__init__(side, side)


if __name__ == "__main__":
    """Module defining the Square class inheriting from Rectangle.

    Usage:
        from module_name import Square
        square = Square(5)
        print(square)
        print(str(square))
        print(square.area())
    """
    square = Square(5)
    print(square)
    print(str(square))
    print(square.area())
