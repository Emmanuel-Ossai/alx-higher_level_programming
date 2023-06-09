#!/usr/bin/python3
import os


def write_python_is_cool():
    os.write(1, "#pythoniscool\n".encode("UTF-8"))


if __name__ == "__main__":
    write_python_is_cool()
