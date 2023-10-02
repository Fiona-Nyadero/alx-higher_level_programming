#!/usr/bin/python3

"""Defines a fx that prnts '\n'"""


def text_indentation(text):
    """Prints text with two new lines after each '.', '?', and ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lines = text.split('\n')

    for line in lines:
        line = line.strip()
        if line.endswith(('.', '?', ':')):
            print(line)
            print()
        else:
            print(line)
