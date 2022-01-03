#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        new_list = my_list[::-1]
        for i in range(0, len(new_list)):
            print("{}".format(new_list[i]), end="\n")
