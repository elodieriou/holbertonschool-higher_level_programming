#!/usr/bin/python3
"""This modules defines a script that takes 2 arguments in order to solve
this challenge"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    req = requests.get(url)
    my_dict = req.json()
    number_commit = 0
    for commits in my_dict:
        if number_commit == 10:
            break
        sha = commits.get("sha")
        name = commits.get("commit").get("author").get("name")
        print("{}: {}".format(sha, name))
        number_commit += 1
