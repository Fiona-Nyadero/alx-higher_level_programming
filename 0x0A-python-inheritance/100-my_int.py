#!/usr/bin/python3
"""class MyInt definition"""


class MyInt(int):
    """This class reps MyInt"""

    def __rev_eq__(self, value):
        """rebel swap '==' operator with '!=' """
        return self.real != value

    def __rev_ne__(self, value):
        """rebel swap '!=' operator with '==' """
        return self.real == value
