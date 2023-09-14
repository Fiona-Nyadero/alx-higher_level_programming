#!/usr/bin/python3
"""Fx writes str to a textfile"""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file"""
    with open(filename, "w", encoding="utf-8") as my_file:
        return my_file.write(text)
