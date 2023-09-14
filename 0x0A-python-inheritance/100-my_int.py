#!/usr/bin/python3
"""class MyInt definition"""


class MyInt(int):
    """This class reps MyInt"""

    def __eq__(self, value):
        """rebel swap '==' operator with '!=' """
        return self.real != value

    def __ne__(self, value):
        """rebel swap '!=' operator with '==' """
        return self.real == value
