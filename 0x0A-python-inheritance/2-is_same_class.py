#!/usr/bin/python3
"""Fx checks for instance of specified class"""


def is_same_class(obj, a_class):
    """Checks for an instance of a given class
    Args:
        obj (any): object to check
        a_class (type): class to compare
    Returns:
        Boolean
    """
    return isinstance(obj, a_class)
