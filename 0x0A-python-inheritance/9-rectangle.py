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
    """Class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
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
            int: The computed area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle in the
            format [Rectangle] <width>/<height>.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


if __name__ == "__main__":
    """Module defining the Rectangle class inheriting from BaseGeometry.

    Usage:
        from module_name import Rectangle
        rectangle = Rectangle(10, 5)
        print(rectangle)
        print(str(rectangle))
        print(rectangle.area())
    """
    rectangle = Rectangle(10, 5)
    print(rectangle)
    print(str(rectangle))
    print(rectangle.area())
