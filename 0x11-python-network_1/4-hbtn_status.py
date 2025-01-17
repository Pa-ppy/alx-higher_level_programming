#!/usr/bin/python3
"""
This module fetches URL with requests."""
import requests


def fetch_status():
    """Fetch and display the body response."""
    response = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
    print(f"\t- utf8 content: {response.text}")


if __name__ == "__main__":
    fetch_status()
