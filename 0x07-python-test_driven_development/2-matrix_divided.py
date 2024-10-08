#!/usr/bin/python3
"""
This module defines a funtion that divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """
    Divides all the elements of a given matrix by a given number.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int, float): The divisor.

    Returns:
        list: A new matrix with all the elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix elements are not integers or floats, or if rows have different sizes.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len({len(row) for row in matrix}) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
