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
    if a_class is object and obj is None:
        return True
    elif a_class is list and isinstance(obj, list):
        return True
    else:
        return isinstance(obj, a_class)
