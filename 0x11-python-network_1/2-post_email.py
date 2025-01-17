#!/usr/bin/python3
"""
This module sends a POST request with email
"""
import urllib.parse
import urllib.request
import sys


def send_email(url, email):
    """Send POST request with email and display the body of the response."""
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data) as response:
        body = response.read().decode('utf-8')
        print(f"Your email is: {body}")

if __name__ == "__main__":
    send_email(sys.argv[1], sys.argv[2])
