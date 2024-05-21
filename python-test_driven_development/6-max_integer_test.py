#!/usr/bin/python3
""" """


def max_integer(list=[]):
    if not list:
        return None
    result = list[0]
    for i in range(len(list)):
        if list[i] > result:
            result = list[i]
    return result
