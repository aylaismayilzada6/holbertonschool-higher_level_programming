#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase followed by a new line."""
    for c in str:
        print("{}".format(chr(ord(c) - 32) if 'a' <= c <= 'z' else c), end="")
    print("{}".format(""))
