#!/usr/bin/python3
"""File writer"""


def append_write(filename="", text=""):
    """Writes in a File"""
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
