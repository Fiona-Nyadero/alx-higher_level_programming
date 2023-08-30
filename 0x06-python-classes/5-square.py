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

    def my_print(self):
        """Prints the square using '#'"""
        if self.__size == 0:
            print("")
        else:
            for y in range(self.__size):
                print("#" * self.__size)
