#!/usr/bin/python3
""" Devide the Matrix """


def matrix_divided(matrix, div):
    """list of list of int div by int"""
    ty_error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(ty_error)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(ty_error)
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise TypeError(ty_error)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result_matrix = []
    for row in matrix:
        new_row = []
        for elem in row:
            divided_elem = round(elem / div, 2)
            new_row.append(divided_elem)
        result_matrix.append(new_row)
    return result_matrix
