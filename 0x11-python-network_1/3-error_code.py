#!/usr/bin/python3
"""This module handles HTTP errors and displays error code."""
import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """Fetch URL and display body or error code."""
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    fetch_url(sys.argv[1])
