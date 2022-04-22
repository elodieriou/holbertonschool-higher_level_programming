#!/usr/bin/python3
"""This module defines a script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    url = argv[1]
    req = request.Request(url)

    try:
        request.urlopen(req)
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
