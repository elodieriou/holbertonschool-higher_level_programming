#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        max_value = sorted(my_list)[-1]
        return max_value
