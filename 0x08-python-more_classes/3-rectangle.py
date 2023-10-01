#!/usr/bin/python3
"""Rectangle class def"""


class Rectangle:
    """This class reps a Rectamgle shape"""

    def __init__(self, width=0, height=0):
        """Inits a Rectangle instance"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width attribute of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute of Rectangle
        Args:
            value: width must be a +ve int
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute of Rectangle
        Args:
            value: height must be a +ve int
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Gets area of a Rectangle object
        Returns:
            Height * Width
        """

        return self.__width * self.__height

    def perimeter(self):
        """Gets perimeter of a Rectangle object
        Returns:
            Perimeter = (2 * Height) + (2 * Width)
        """

        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns an infrmal str rep"""

        if self.__height == 0 or self.__width == 0:
            return ''

        printed_str = ''

        for t in range(self.__height):
            for s in range(self.__width):
                printed_str += '#'
            printed_str += '\n'
        return printed_str[:-1]
