#!/usr/bin/python3
"""
The function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    The function divides all elements of a matrix.

    Args:
        - matrix (list):
            . must be a list of lists of integers or floats
        - div (int, float):
            . must be a number (integer or float)
            . if equal to 0, raise ZeroDivisionError

    Return:
        A new matrix
    """
    if isinstance(matrix, list) is False:
        raise TypeError('matrix must be a matrix (list of lists) of \
integers/floats')
    elif isinstance(div, (int, float)) is False:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    else:
        new_matrix = matrix.copy()
        for i in range(len(matrix)):
            if len(matrix[i]) != len(matrix[i - 1]):
                raise TypeError('Each row of the matrix must have the \
same size')
            new_matrix[i] = matrix[i].copy()
            for j in range(len(matrix[i])):
                if isinstance(matrix[i][j], (int, float)) is False:
                    raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
                new_matrix[i][j] = round((matrix[i][j] / div), 2)
        return new_matrix
