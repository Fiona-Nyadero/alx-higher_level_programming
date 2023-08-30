#!/usr/bin/python3
"""Square class definition"""
class Square:
    """This class reps a square shape."""

    def __init__(self, size=0):
        """Inits a private instance attribute.

        Args:
            size (int): The size of the square. Defaults to 0.
        
        Raises:
            TypeError: If size != integer.
            ValueError: If size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calcs area of the square.

        Returns: The area of the square.
        """
        return self.__size ** 2
