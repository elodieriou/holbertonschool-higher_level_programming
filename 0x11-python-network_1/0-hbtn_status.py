#!/usr/bin/python3
"""THis module defines a script that fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    from urllib.request import urlopen

    url = "https://intranet.hbtn.io/status"
    with urlopen(url) as response:
        page = response.read()
        utf = page.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(page)))
        print("\t- content: {}".format(page))
        print("\t- utf8 content: {}".format(utf))
