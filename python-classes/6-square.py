#!/usr/bin/python3
"""Module that defines a Square class"""


class Square:
    """Defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square with validated size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position with validation"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) and i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with # characters considering position"""
        if self.__size == 0:
            print()
            return

        # vertical offset (position[1])
        for _ in range(self.__position[1]):
            print()

        # square lines
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
