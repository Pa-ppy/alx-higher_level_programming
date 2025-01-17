#!/usr/bin/python3
"""This module takes in a URL and sends a request to the URL."""
import requests
import sys


def fetch_url(url):
    """Fetch URL and handle error codes."""
    response = requests.get(url)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)

if __name__ == "__main__":
    fetch_url(sys.argv[1])
