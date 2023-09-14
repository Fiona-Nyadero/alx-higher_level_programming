#!/usr/bin/python3
"""MyList class inherits from list class"""


class MyList(list):
    """This class inherits from list"""
    def print_sorted(self):
        """prints list(sorted)"""
        print(sorted(self))
