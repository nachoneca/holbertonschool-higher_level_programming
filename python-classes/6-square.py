#!/usr/bin/python3
"""This module defines a class named 'Square'."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = size

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Get the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, size):
        """Set the size of the square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """ Gets position
        return position
        """
        return self.__position

    @position.setter
    def position(self, position):
        """possition setter and ifs
        """

        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or position[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[1]) is not int or position[1]:
            raise ("position must be a tuple of 2 positive integers")
        self.__position = position

        def my_print(self):
            """
        Print a square
        """
        if self.__size == 0:
            print("")
            return
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
