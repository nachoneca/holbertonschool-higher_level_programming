#!/usr/bin/python3
"""Creation of filereder"""


def read_file(filename=""):
    """File reader"""
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())
