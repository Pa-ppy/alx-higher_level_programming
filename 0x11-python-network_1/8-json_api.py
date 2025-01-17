#!/usr/bin/python3
"""This module sends a POST request to http://0.0.0.0:5000/search_user."""
import requests
import sys


def search_user(letter):
    """Send POST request with letter and handle JSON response."""
    if not letter:
        letter = ""
    response = requests.post('http://0.0.0.0:5000/search_user',
                             data={'q': letter})

    try:
        data = response.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user(sys.argv[1] if len(sys.argv) > 1 else "")
