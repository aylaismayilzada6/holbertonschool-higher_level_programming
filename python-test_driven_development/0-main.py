#!/usr/bin/python3
"""
0-main.py for testing add_integer
"""

add_integer = __import__('0-add_integer').add_integer

if __name__ == "__main__":
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))           # default b=98
    print(add_integer(100.3, -2))   # floats cast to int
    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)
    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
    print(add_integer(3.9, 5.1))    # floats cast to int
    print(add_integer(-2, -3))
