#!/usr/bin/python3
from sys import argv


def inf_add():
    i = 1
    sum = 0
    while (i < (len(argv))):
        sum = sum + int(argv[i])
        i = i + 1
    print(sum)


if (__name__ == "__main__"):
    inf_add()
