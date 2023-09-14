#!/usr/bin/python3
"""Fx checks for class and inherited class"""


def is_kind_of_class(obj, a_class):
    """Checks for a class instance or inherited class instance
    Args:
        obj (any): object to check
        a_class (type): class to compare
    Returns:
        Boolean
    """
    if isinstance(obj, a_class):
        return True
    return False
