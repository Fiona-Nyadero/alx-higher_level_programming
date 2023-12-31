#!/usr/bin/python3
"""Square class definition"""


class Square:
    """This class reps a square shape"""

    def __init__(self, size=0):
        """Inits a private instance attribute.

        Args:
            size (int): The size of the square. 0 by default.

        Raises:
            ValueError: If size < 0.
            TypeError: If size != int.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
