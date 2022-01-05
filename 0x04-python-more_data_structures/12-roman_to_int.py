#!/usr/bin/python3
def roman_to_int(roman_string):
    rs = roman_string
    if isinstance(rs, str) == 0 or rs is None:
        return 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    for i in range(len(rs)):
        if i > 0 and dict[rs[i]] > dict[rs[i - 1]]:
            result += dict[rs[i]] - 2 * dict[rs[i - 1]]
        else:
            result += dict[rs[i]]
    return result
