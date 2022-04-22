#!/usr/bin/python3
"""This module defines a script that fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    url = "https://intranet.hbtn.io/status"
    req = requests.get(url)
    page = req.text
    print("Body response:")
    print("\t- type: {}".format(type(page)))
    print("\t- content: {}".format(page))
