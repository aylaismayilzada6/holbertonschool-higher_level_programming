#!/usr/bin/python3

"""
Module for saving Python objects to a file in
JSON format.

This module provides a function to write an
object to a text file using its JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON
    representation.

    Args:
        my_obj: The object to be serialized and saved.
        filename (str): The name of the file to
        write the JSON string to.

    Returns:
        None

    Raises:
        TypeError: If the object is not serializable to JSON.
        OSError: If the file cannot be opened or written.

    Example:
        >>> save_to_json_file({'a': 1, 'b': 2}, 'my_file.json')
    """
    json_str = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json_str)
