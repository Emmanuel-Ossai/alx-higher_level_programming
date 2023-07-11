#!/usr/bin/python3

"""
The base class BaseGeometry
"""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Compute the area of the geometry object.

        Raises:
            Exception: Indicates that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    """Module defining the BaseGeometry class with the area() method.

    Usage:
        from module_name import BaseGeometry
        geometry = BaseGeometry()
        geometry.area()
    """
    pass
