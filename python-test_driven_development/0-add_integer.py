#!/usr/bin/python3
"""
    Suma dos enteros o flotantes (después de convertirlos a enteros).

    Args:
        a: Entero o flotante.
        b: Entero o flotante, por defecto 98.

    Returns:
        Entero: La suma de a y b.

    Raises:
        TypeError: Si a o b no son enteros ni flotantes.
"""


def add_integer(a, b=98):
    """ add two integers or flots """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)
