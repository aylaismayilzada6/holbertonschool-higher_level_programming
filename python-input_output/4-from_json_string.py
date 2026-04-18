#!/usr/bin/python3
"""
Module for converting JSON strings to
Python objects.

This module provides a function to return the
Python object represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """
    Returns the Python object represented by
    a JSON string.

    Args:
        my_str (str): The JSON string
        to convert.

    Returns:
        object: The Python object represented
        by the JSON string.

    Raises:
        json.JSONDecodeError: If the string
        is not a valid JSON document.

    Example:
        >>> from_json_string('{"a": 1, "b": 2}')
        {'a': 1, 'b': 2}
    """
    return json.loads(my_str)
