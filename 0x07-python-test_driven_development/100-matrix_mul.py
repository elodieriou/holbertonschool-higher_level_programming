#!/usr/bin/python3
"""
The function that multiplies two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    The function multiplies two matrices.

    Args:
        - m_a (list, int, float):
            . must be an list of lists of integers or floats
            . if is not a list, raise a TypeError
            . if one element of those list of lists is not an integer or a
              float, raise a TypeError
            . if is empty, raise a ValueError
            . if is not a rectangle, raise a TypeError
            . if can’t be multiplied with m_b, raise a Value Error

        - m_b (list, int, float):
            . must be an list of lists of integers or floats
            . if is not a list, raise a TypeError
            . if one element of those list of lists is not an integer or a
              float, raise a TypeError
            . if is empty, raise a ValueError
            . if is not a rectangle, raise a TypeError
            . if can’t be multiplied with m_b, raise a Value Error

    Return:
        The result
    """

    if isinstance(m_a, list) is False:
        raise TypeError('m_a must be a list')
    elif isinstance(m_b, list) is False:
        raise TypeError('m_b must be a list')

    for list_of_list_a in m_a:
        if isinstance(list_of_list_a, list) is False:
            raise TypeError('m_a must be a list of lists')
    for list_of_list_b in m_b:
        if isinstance(list_of_list_b, list) is False:
            raise TypeError('m_b must be a list of lists')

    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    elif m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')

    for list_a in m_a:
        for value_a in list_a:
            if isinstance(value_a, (int, float)) is False:
                raise TypeError('m_a should contain only integers or floats')
    for list_b in m_b:
        for value_b in list_b:
            if isinstance(value_b, (int, float)) is False:
                raise TypeError('m_b should contain only integers or floats')

    for row_a in m_a:
        if len(row_a) != len(m_a[0]):
            raise TypeError('each row of m_a must be of the same size')
    for row_b in m_b:
        if len(row_b) != len(m_b[0]):
            raise TypeError('each row of m_b must be of the same size')

    nb_column_a = 0
    for column_a in m_a[0]:
        nb_column_a += 1
    nb_row_b = 0
    for row_b in m_b:
        nb_row_b += 1
    if nb_column_a != nb_row_b:
        raise ValueError('m_a and m_b can\'t be multiplied')

    result = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
