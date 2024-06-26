#!/usr/bin/python3
"""Def a square and print it"""


def print_square(size):
    """ print a square """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size, end="")
        print()
