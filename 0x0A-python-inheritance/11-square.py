#!/usr/bin/python3
"""Imports Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This class reps Square"""

    def __init__(self, size):

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
