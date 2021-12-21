#!/usr/bin/python3
def uppercase(str):
    string = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            string += chr(ord(i) - 32)
        else:
            string += chr(ord(i))
    print("{}".format(string))
