#!/usr/bin/python3
"""This module defines a script that take in a URL, sends a resquest to the URL
and diplays the value of the "X-Request-Id" variable foud in the header of the
response"""

if __name__ == "__main__":
    from urllib.request import urlopen
    from sys import argv

    with urlopen(argv[1]) as response:
        header = response.getheader('X-Request-Id')
        print("{}".format(header))
