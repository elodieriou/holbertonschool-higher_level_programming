#!/usr/bin/python3
def check_tuple(tuple_c=()):
    if len(tuple_c) > 2:
        tuple_c = (tuple_c[0], tuple_c[1])
    elif len(tuple_c) <= 1:
        if len(tuple_c) == 0:
            tuple_c = (0, 0)
        if len(tuple_c) == 1:
            tuple_c = (tuple_c[0], 0)
    return tuple_c

def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = check_tuple(tuple_a)
    tuple_b = check_tuple(tuple_b)
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
