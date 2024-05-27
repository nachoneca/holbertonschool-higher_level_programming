#!/usr/bin/python3
"""File writer"""


def write_file(filename="", text=""):
    """Writes in a File"""
    with open(filename, mode="w", encoding="utf-8") as my_file:
        my_file.write(text)
