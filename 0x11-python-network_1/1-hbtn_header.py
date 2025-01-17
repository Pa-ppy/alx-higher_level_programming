#!/usr/bin/python3
"""
This module takes a URL and sends a request of X-Request-Id
"""
import urllib.request
import sys


def fetch_request_id(url):
    """Fetch the value of X-Request-Id header."""
    with urllib.request.urlopen(url) as response:
        headers = response.getheaders()
        for header in headers:
            if header[0] == 'X-Request-Id':
                print(header[1])

if __name__ == "__main__":
    fetch_request_id(sys.argv[1])
