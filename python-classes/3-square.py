#!/usr/bin/python3
"""This module defines an empty class named 'Square'"""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return int(self.__size) * int(self.__size)
