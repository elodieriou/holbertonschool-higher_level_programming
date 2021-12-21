#!/usr/bin/python3
for n1 in range(0, 10):
    for n2 in range(0, 10):
        if n1 < n2 and n1 < 8:
            print("{:d}".format(n1), end="")
            print("{:d}".format(n2), end=", ")
print("89")
