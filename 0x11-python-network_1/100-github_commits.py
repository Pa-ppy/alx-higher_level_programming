#!/usr/bin/python3
"""This module lists the ten(10) most recent commits on a given repo."""
import requests
import sys


def list_commits(repo, owner):
    """List 10 commits of the specified repository by the specified owner."""
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit.get('sha')
            author = commit.get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    list_commits(sys.argv[1], sys.argv[2])
