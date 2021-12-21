#!/usr/bin/python3
for alphabet in range(122, 96, -1):
    if (alphabet % 2) != 0:
        upper = alphabet - 32
    else:
        upper = alphabet
    print("{}".format(chr(upper)), end="")
