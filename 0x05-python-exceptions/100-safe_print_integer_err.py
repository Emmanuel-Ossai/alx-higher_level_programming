#!/usr/bin/python3


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as error:
        print("Exception: {}".format(error))
        return False
    finally:
        import sys
        sys.stdout.flush()

    return True
