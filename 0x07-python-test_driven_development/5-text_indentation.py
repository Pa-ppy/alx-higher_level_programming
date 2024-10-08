#!/usr/bin/python3
"""
This module defines function that prints a text with 2 new lines after '.', '?', and ':'.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = {'.', '?', ':'}
    result = ""
    for char in text:
        result += char
        if char in special_chars:
            result += "\n\n"

    print(result.strip())
