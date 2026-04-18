#!/usr/bin/python3
"""
Module for writing a string to a text file.
This module provides a function to write a
string to a text file (UTF-8)
and return the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and
    returns the number of characters written.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        int: The number of characters written.
    Raises:
        OSError: If the file cannot be opened
        or written.
    Example:
        >>> write_file('my_file.txt', 'Hello, World!')
        13
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
