#!/usr/bin/python3
"""
Module that contains a function that returns the dictionary
description of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object.

    Args:
        obj: An instance of a class

    Returns:
        dict: Dictionary representation of the object
    """
    return obj.__dict__
