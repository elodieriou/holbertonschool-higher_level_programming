#!/usr/bin/python3
from sys import argv
if len(argv) == 1:
    print("0")
if len(argv) > 1:
    add_argument = 0
    for argument in range(1, len(argv)):
        add_argument += int(argv[argument])
    print("{:d}".format(add_argument))

    if __name__ == "__main__":
        argv
