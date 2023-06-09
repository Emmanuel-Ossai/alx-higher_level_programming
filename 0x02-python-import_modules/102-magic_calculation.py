#!/usr/bin/python3

from magic_calculation_102 import add, sub


def magic_calculation(a, b):

    if a < b:
        c = add(a, b)
        c = add(c, 4)
        c = add(c, 5)
        return c
    else:
        return sub(a, b)
