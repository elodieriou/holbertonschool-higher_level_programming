#!/usr/bin/python3
"""
The function that prints a text with 2 new lines after each of these
characters: ., ? and :
"""


def text_indentation(text):
    """
    The function prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        - text (str):
            . must be a string
            . should be no space at the beginning or at the end of
              each printed line

    Return:
        Nothing
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    else:
        new_text = ""
        i = 0
        while i < len(text) - 1 and text[i] == " ":
            i += 1

        j = len(text) - 1
        while text[j] == " ":
            j -= 1

        while i <= j:
            if text[i] == "." or text[i] == "?" or text[i] == ":":
                new_text += text[i]
                new_text += "\n"
                new_text += "\n"
                i += 1

                if text[i] == "\n":
                    i += 1

                while i < j and text[i] == " ":
                    i += 1
                continue

            else:
                new_text += text[i]
                i += 1

        print("{}".format(new_text), end="")
