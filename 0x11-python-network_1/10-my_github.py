#!/usr/bin/python3
"""This module uses an API key from GITHUB to display a GITHUB ID."""
import requests
import sys


def get_github_id(username, token):
    """Fetch GitHub user ID using Basic Authentication."""
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("None")


if __name__ == "__main__":
    get_github_id(sys.argv[1], sys.argv[2])
