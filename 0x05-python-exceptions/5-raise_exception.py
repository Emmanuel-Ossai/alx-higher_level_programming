#!/usr/bin/python3


def raise_exception():
    try:
        value = 10 / 0
    except ZeroDivisionError:
        raise TypeError
