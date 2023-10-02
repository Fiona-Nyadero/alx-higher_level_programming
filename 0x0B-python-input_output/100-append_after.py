#!/usr/bin/python3
"""Defines append_after module"""


def append_after(filename="", search_string="", new_string=""):
    """Appends text to a file after each specified line"""

    a_text = ""
    with open(filename) as r:
        for line in r:
            a_text += line
            if search_string in line:
                a_text += new_string
    with open(filename, "w") as w:
        w.write(a_text)
