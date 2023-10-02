#!/usr/bin/python3
"""Defines locked class"""


class LockedClass:
    """prevents the user from dynamically creating new inst attributes"""
    __slots__ = ["first_name"]
