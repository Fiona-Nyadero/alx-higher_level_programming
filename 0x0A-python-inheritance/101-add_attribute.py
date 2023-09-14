#!/usr/bin/python3
"""Fx adds new attribute to object if possible"""


def add_attribute(obj, attri, value):
    """Adds a new attribute to object if possible
        TypeError: If attribute can't be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attri, value)
