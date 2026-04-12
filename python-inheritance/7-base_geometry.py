#!/usr/bin/python3
"""Module for BaseGeometry class."""


class BaseGeometry:
    """A BaseGeometry class."""

    def area(self):
        """Method to calculate the area.
        
        Raises:
            Exception: Always raises an Exception indicating it is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if a value is a strict integer greater than 0.

        Args:
            name (str): The name of the parameter (always assumed to be a string).
            value (int): The parameter to validate.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
