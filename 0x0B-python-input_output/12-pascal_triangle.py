#!/usr/bin/python3
"""
The module define the function 'pascal_triangle()'
"""


def pascal_triangle(n):
    """
    The method returns a list of lists of integers representing
    the Pascal’s triangle of n.
    Args:
        - n (int)
            . n less or equal to zero, return an empty list
    """
    triangle = [[]]
    number_add = 0

    if n <= 0:
        return []

    for i in range(n):
        add1 = 0
        add2 = 0
        triangle[i].append(1)
        if i >= 2:
            for j in range(number_add):
                triangle[i].append(triangle[i - 1][add1] +
                                   triangle[i - 1][add2 + 1])
                add1 += 1
                add2 += 1
        if i >= 1:
            triangle[i].append(1)
            number_add += 1
        if i != n - 1:
            triangle.append([])

    return triangle
