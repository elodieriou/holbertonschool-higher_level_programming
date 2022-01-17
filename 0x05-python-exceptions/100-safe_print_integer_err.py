#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as error_integer:
        print("Exception: {}".format(error_integer), file=sys.stderr)
        return False
