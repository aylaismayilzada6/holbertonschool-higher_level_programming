#!/usr/bin/python3
"""
Module that defines a Student class.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The student's first name
            last_name (str): The student's last name
            age (int): The student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.

        If attrs is a list of strings, only attributes whose names
        are included in this list will be returned.
        Otherwise, all attributes are returned.

        Args:
            attrs (list, optional): List of attribute names to retrieve

        Returns:
            dict: Dictionary containing selected or all attributes
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            new_dict = {}

            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]

            return new_dict

        return self.__dict__
