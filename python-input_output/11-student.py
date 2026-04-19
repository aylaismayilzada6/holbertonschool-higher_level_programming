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
        Initializes a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary representation of the Student.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): Dictionary containing attributes
        """
        for key, value in json.items():
            self.__dict__[key] = value
