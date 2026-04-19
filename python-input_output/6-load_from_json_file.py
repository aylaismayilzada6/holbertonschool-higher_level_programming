#!/usr/bin/python3
"""
Module for loading Python objects from a JSON file.

This module provides a function to create a Python object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        object: The Python object represented by the JSON file.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file does not contain valid JSON.
        OSError: If the file cannot be opened or read.

    Example:
        >>> load_from_json_file('my_file.json')
        {'a': 1, 'b': 2}
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return json.loads(f.read())
