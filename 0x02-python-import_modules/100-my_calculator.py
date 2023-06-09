#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys


def handle_arithmetic_operations():
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    operator = sys.argv[2]
    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = ops[operator](a, b)
    print("{} {} {} = {}".format(a, operator, b, result))


if __name__ == "__main__":

    handle_arithmetic_operations()
