#!/usr/bin/python3
"""
This module defines a function that multiplies two matrices using Numpy.
"""

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using Numpy.

    Args:
        m_a (list of lists): Matrix A, a list of lists of integersor floats.
        m_b (list of lists): Matrix B, a list of lists of integersor floats.

    Returns:
        list of lists: The resulting matrix.
    """
    return np.dot(m_a, m_b).tolist()
