#!/usr/bin/python3
def multiple_returns(sentence):
    string_len = len(sentence)
    if sentence == "":
        first_char = None
    else:
        first_char = sentence[0]
    return string_len, first_char
