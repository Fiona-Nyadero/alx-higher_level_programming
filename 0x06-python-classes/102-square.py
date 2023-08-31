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
        self.size = size

    @property
    def size(self):
        """return new sq size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """return sq area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Checks for equal areas"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Checks for different areas"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Checks if current sq area > another"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Checks if current sq area >= another"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Checks if current sq area < another"""
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if current sq area <= another"""
        return self.area() <= other.area()
