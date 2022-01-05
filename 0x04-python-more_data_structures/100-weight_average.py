#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    sum_coeff = 0
    average = 0
    for i in range(len(my_list)):
        sum_coeff += my_list[i][1]
        average += my_list[i][0] * my_list[i][1]
    return average / sum_coeff
