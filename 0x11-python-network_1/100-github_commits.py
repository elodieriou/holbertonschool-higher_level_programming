#!/usr/bin/python3
"""This modules defines a script that takes 2 arguments in order to solve
this challenge"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    req = requests.get(url)
    my_dict = req.json()
    for i in range(0, 10):
        sha = my_dict[i].get("sha")
        name = my_dict[i].get("commit").get("author").get("name")
        print("{}: {}".format(sha, name))
