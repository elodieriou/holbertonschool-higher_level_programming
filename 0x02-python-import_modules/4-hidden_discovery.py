#!/usr/bin/python3
import hidden_4
for name in dir(hidden_4):
    if name[0:2] != "__":
        print("{:s}".format(name))

if __name__ == "__main__":
    hidden_4
