#!/usr/bin/python3
"""
Module 7-base_geometry

Defines the BaseGeometry class with an unimplemented area method
and a method to validate integer attributes.
"""


class BaseGeometry:
    """
    BaseGeometry class with area and integer validator.
    """

    def area(self):
        """Raise an Exception indicating area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that 'value' is a positive integer.

        Args:
            name (str): The name of the parameter to validate.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
