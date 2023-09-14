#!/usr/bin/python3
"""returns the dict description"""


def class_to_json(obj):
    """Returns the dictionary description of JSON"""
    return obj.__dict__
