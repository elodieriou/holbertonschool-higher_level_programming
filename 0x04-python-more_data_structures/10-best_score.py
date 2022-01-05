#!/usr/bin/python3
def best_score(a_dictionary):
    max_value = None
    if a_dictionary:
        for key in a_dictionary:
            if max_value is None or a_dictionary[key] > max_value:
                max_value = a_dictionary[key]
                max_key = key
        return max_key
