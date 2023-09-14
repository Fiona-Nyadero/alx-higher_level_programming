#!/usr/bin/python3
"""Fx appends str at end of textfile"""


def append_write(filename="", text=""):
    """Appends string to end of a UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as my_file:
        return my_file.write(text)
