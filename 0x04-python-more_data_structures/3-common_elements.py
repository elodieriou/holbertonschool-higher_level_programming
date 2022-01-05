#!/usr/bin/python3
def common_elements(set_1, set_2):
    result = []
    for element in set_1:
        if element in set_2:
            result.append(element)
    return result
