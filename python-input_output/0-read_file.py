#!/usr/bin/python3

"""
Module for reading and printing the contents of
a text file.
This module provides a function to read a text
file (UTF-8) and print its content
to the standard output (stdout).
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and
    prints its content to standard output.
    This function opens the specified file
    in read mode with UTF-8 encoding and prints
    its entire content to the standard output
    (usually the console). Each line is printed
    exactly as it appears in the file.
    Args:
        filename (str): The path to the file to
        read. Defaults to an empty string.
    Returns:
        None
    Raises:
        FileNotFoundError: If the file does not exist.
        PermissionError: If the file cannot be accessed
        due to permissions.
        OSError: For other issues related to file access.

    Example:
        >>> read_file('my_file.txt')
        (prints the content of 'my_file.txt' to stdout)
    """
    with open(filename, 'r', encoding="utf-8") as f:
        for char in f:
            print(char, end='')
