#!/usr/bin/python3
"""This module defines script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and displays the body
of the response (decoded in utf-8)"""

if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv

    url = argv[1]
    data = parse.urlencode({'email': argv[2]}).encode('ascii')
    req = request.Request(url, data)

    with request.urlopen(req) as response:
        page = response.read().decode('utf-8')
        print(page)
