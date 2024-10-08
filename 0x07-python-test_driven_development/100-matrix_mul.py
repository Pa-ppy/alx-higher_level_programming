#!/usr/bin/python3
"""
This module defines a function that multiplies two matrices.
"""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): Matrix A, a lits of lists of integers or floats.
        m_b (list of lists): Matrix B, a list of lists of integers or floats.

    Returns:
        list of lists: The resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers or floats.
        ValueError: If m_a or m_b is empty or can't be multiplied.
    """
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not m_a or not all(m_a):
        raise ValueError("m_a can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row):
        raise TypeError("m_a should contain only integers or floats")
    if len({len(row) for row in m_a}) > 1:
        raise TypeError("each row of m_a must be of the same size")

    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_b or not all(m_b):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_b should contain only integers or floats")
    if len({len(row) for row in m_b}) > 1:
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            row.append(sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b))))
        result.append(row)

    return result
