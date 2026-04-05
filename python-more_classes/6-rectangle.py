#!/usr/bin/python3
"""Module that defines a Rectangle class."""


class Rectangle:
    """Class that defines a rectangle."""

    number_of_instances = 0  # class attribute

    def __init__(self, width=0, height=0):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    # ----- WIDTH -----
    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    # ----- HEIGHT -----
    @property
    def height(self):
        """Retrieve the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # ----- AREA -----
    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    # ----- PERIMETER -----
    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    # ----- STRING REPRESENTATION -----
    def __str__(self):
        """Return the rectangle using # characters."""
        if self.__width == 0 or self.__height == 0:
            return ""

        rows = []
        for _ in range(self.__height):
            rows.append("#" * self.__width)

        return "\n".join(rows)

    # ----- OFFICIAL REPRESENTATION -----
    def __repr__(self):
        """Return a string to recreate the rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    # ----- DESTRUCTOR -----
    def __del__(self):
        """Print message when instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
