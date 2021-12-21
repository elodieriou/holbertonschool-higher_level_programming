#!/usr/bin/python3
for alphabet in range(122, 96, -1):
    if not alphabet % 2:
        upper = alphabet
    else:
        upper = alphabet - 32
    print("{}".format(chr(upper)), end="")
