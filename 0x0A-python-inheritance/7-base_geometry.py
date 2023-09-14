#!/usr/bin/python3
"""Defines class BaseGeometry."""


class BaseGeometry:
    """This class reps BaseGeometry"""

    def area(self):
        """Public instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates 'value'
            TypeError: if value != integer
            ValueError: if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
