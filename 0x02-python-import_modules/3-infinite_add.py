#!/usr/bin/python3

import sys


def calculate_total(arguments):
    total = sum(int(arg) for arg in arguments)
    return total


if __name__ == "__main__":

    arguments = sys.argv[1:]
    total = calculate_total(arguments)
    print("{}".format(total))
