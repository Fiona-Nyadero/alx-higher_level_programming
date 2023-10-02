#!/usr/bin/python3
"""Student class definiton"""


class Student:
    """This class reps Student"""

    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {f: getattr(self, f) for f in attrs if hasattr(self, f)}
        return self.__dict__
