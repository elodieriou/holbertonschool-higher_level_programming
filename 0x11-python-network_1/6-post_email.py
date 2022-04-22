#!/usr/bin/python3
"""This module defines a script that takes in a URL and an email address, sends
a POST request to the passed URL with the email as a parameter, and finally
displays the body of the response."""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = argv[1]
    data = {'email': argv[2]}
    req = requests.post(url, data)

    print(req.text)
