#!/usr/bin/python3
"""This module defines an empty class named 'Square'"""
class Square:
    """This is the definition of the 'Square' class"""
    def __init__(self, size=0):
        """Instance of Size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Definition of Area"""
        return int(self.__size) * int(self.__size)
