#!/usr/bin/python3
"""
This module contains a function that reads a UTF8 text file and prints it.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The path to the file. Default is an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
