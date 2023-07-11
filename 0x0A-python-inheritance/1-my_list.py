#!/usr/bin/python3

"""
This python class contains the MyList class
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    This class provides an additional method for printing the list

    in sorted order.

    """

    def __init__(self):
        """
        initializes the object
        """
        super().__init__()

    def print_sorted(self):
        """
        Prints the list in sorted (ascending) order.
        """
        print(sorted(self))
