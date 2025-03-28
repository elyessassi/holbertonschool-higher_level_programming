#!/usr/bin/python3

"""  a function that prints a text with 2 new
    lines after each of these characters: ., ? and : """


def text_indentation(text):
    """ a function that prints a text with 2
      new lines after each of these characters: ., ? and : """

    new_line_chars = [".", "?", ":"]
    if (not isinstance(text, str)):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if (text[i] == " " and text[i - 1] in new_line_chars):
            continue
        print(text[i], end="")
        if (text[i] in new_line_chars):
            print("")
            print("")


if (__name__ == "__main__"):
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
