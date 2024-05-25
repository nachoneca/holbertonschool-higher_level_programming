#!/usr/bin/python3
"""
    inherits from
"""


def inherits_from(obj, a_class):
    """Chekea si obj es una instancia de a_class
    o si hereda de a_class"""

    return isinstance(obj, a_class) and type(obj) is not a_class
