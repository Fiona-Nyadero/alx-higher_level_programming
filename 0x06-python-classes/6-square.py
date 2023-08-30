#!/usr/bin/python3
"""Square class definition"""


class Square:
    """This class reps a square shape."""
    def __init__(self, size=0, position=(0, 0)):
        """Inits a private instance attribute.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple):Pstn of the printsquare dfaults to (0, 0).
            """
        self.size = size
        self.position = position

    @property
    def size(self):
        """return(int) new sq size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets Sq size

        Args:
            value (int): size
        Raises:
            TypeError: If size != integer.
            ValueError: If size < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """return new sq position(tuple)"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets Sq position

        Args:
            value (tuple): sq position
        Raises:
            TypeError: If the position != tuple of 2 +ve int.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return sq area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#'"""
        if self.__size == 0:
            print("")
            return

        for y in range(self.__position[1]):
            print()

        for y in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
