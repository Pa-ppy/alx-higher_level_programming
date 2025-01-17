#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status
"""
import urllib.request


def fetch_status():
    """Fetch and display the body response."""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') \
            as response:
        body = response.read()
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")


if __name__ == "__main__":
    fetch_status()
