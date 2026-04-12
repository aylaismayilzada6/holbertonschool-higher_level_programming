#!/usr/bin/python3
"""Module that defines a MyList class"""


class MyList(list):
    """Inherits from list and adds a sorted print method"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
