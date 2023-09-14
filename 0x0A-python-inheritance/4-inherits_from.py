#!/usr/bin/python3
"""Fx checks if object is an inherited class instance"""


def inherits_from(obj, a_class):
    """Checks if object is an inherited class instance
    Args:
        obj (any): object to check
        a_class (type): class to compare
    Returns:
        Boolean
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
