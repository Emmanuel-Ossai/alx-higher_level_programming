#!/usr/bin/python3

"""
Contains a script that adds all arguments to a Python list,
and then save them to a file
"""

import sys
from typing import List
from load_from_json_file import load_from_json_file
from save_to_json_file import save_to_json_file


def add_arguments_to_list(arguments: List[str]):
    """
    Add arguments to a Python list and save them to a file

    """
    try:
        # Checks and load existing list from file, or create a new empty list
        my_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        my_list = []

    # Then adds arguments to the list
    my_list.extend(arguments)

    # Save the updated list to the file
    save_to_json_file(my_list, 'add_item.json')


if __name__ == '__main__':
    # Get the arguments from command-line excluding the script name
    arguments = sys.argv[1:]

    # Add arguments to the list and save to file
    add_arguments_to_list(arguments)
