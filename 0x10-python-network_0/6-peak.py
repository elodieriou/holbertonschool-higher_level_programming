#!/usr/bin/python3
"""This module difines the function "find_peak" in a list
of unsorted integers"""


def find_peak(list_of_integers):
    """Get the peak of a list"""

    if not list_of_integers:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)

    mid = int(len(list_of_integers) / 2)
    if list_of_integers[mid] > list_of_integers[mid - 1] and\
       list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]
    elif list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
