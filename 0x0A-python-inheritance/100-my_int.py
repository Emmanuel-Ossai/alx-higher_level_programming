#!/usr/bin/python3

"""
The class MyInt
"""


class MyInt(int):
    """Class representing a rebellious integer."""

    def __eq__(self, other):
        """Override the == operator to invert its behavior.

        Args:
            other (Any): The object to compare with.

        Returns:
            bool: True if self is not equal to other, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator to invert its behavior.

        Args:
            other (Any): The object to compare with.

        Returns:
            bool: True if self is equal to other, False otherwise.
        """
        return super().__eq__(other)


if __name__ == "__main__":
    """Module defining the MyInt class inheriting from int.

    Usage:
        from module_name import MyInt
        num1 = MyInt(5)
        num2 = MyInt(10)
        print(num1 == num2)
        print(num1 != num2)
    """
    num1 = MyInt(5)
    num2 = MyInt(10)
    print(num1 == num2)  # Output: False
    print(num1 != num2)  # Output: True
