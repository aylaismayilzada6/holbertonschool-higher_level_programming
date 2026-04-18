#!/usr/bin/python3

"""
Module for converting Python objects
to JSON strings.
This module provides a function to
return the JSON representation of an object (as a string).
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    Args:
        my_obj: The object to convert to a JSON string.
    Returns:
        str: The JSON string representation of the object.
    Raises:
        TypeError: If the object is not serializable to JSON.
    Example:
        >>> to_json_string({'a': 1, 'b': 2})
        '{"a": 1, "b": 2}'
    """
    return json.dumps(my_obj)
