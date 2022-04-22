#!/usr/bin/python3
"""This module defines a script that takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8)."""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    req = requests.get(url)

    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
