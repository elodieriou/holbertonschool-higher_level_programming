#!/usr/bin/python3
"""Write a Python script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://api.github.com/user"
    username = argv[1]
    pwd = argv[2]
    req = requests.get(url, auth=(username, pwd))
    my_dict = req.json()
    print(my_dict.get("id"))
