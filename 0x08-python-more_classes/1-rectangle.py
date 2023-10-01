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
