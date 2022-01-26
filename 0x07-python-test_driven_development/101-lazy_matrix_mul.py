#!/usr/bin/python3
"""
The function that multiplies 2 matrices by using the module NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """
    The function multiplies 2 matrices with the module NumPy.

    Args:
        - m_a (list, int, float)
        - m_b (list, int, float)

    Return:
        The result
    """
    return numpy.dot(m_a, m_b)
