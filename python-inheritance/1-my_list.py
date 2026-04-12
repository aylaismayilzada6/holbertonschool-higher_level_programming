#!/usr/bin/python3

class MyList(list):
    """Inherits from list and adds a sorted print method"""

    def print_sorted(self):
        """Prints the list in ascending order"""
        print(sorted(self))
