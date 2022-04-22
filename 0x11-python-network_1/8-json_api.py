#!/usr/bin/python3
"""This module defines a script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter."""

if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) == 1:
        data = {'q': ''}
    else:
        data = {'q': argv[1]}
    url = "http://5771634acedf.c90a0b50.hbtn-cod.io:5000/search_user"
    req = requests.post(url, data)

    try:
        my_dict = req.json()
        if my_dict == {}:
            print("No result")
        else:
            print("[<{}>] <{}>".format(my_dict.get("id"), my_dict.get("name")))
    except Exception:
        print("Not a valid JSON")
