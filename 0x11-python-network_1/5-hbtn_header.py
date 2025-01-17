#!/usr/bin/python3
"""This module takes in a URL and sends a request to the URL."""
import requests
import sys


def fetch_request_id(url):
    """Fetch and display the value of X-Request-Id header."""
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))


if __name__ == "__main__":
    fetch_request_id(sys.argv[1])
