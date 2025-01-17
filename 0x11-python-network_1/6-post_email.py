#!/usr/bin/python3
"""This module takes in a URL and an email address."""
import requests
import sys


def send_email(url, email):
    """Send POST request with email and display the body of the response."""
    response = requests.post(url, data={'email': email})
    print(f"Your email is: {response.text}")


if __name__ == "__main__":
    send_email(sys.argv[1], sys.argv[2])
