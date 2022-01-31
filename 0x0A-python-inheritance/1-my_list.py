#!/usr/bin/python3
"""
The module that define the class MyList
"""


class MyList(list):
    """
    The class MyList inherits from list and contains a public instance method
    print_sorted
    """
    def print_sorted(self):
        """
        This function prints the list, but sorted with ascending sort
        """
        print("{}".format(sorted(self)))
