#!/usr/bin/python3
from sys import argv


def print_args():
    if (len(argv) == 1):
        print("0 arguments.")
    elif (len(argv) == 2):
        print("1 argument:")
        print("1: {}".format(argv[1]))
    elif (len(argv) > 2):
        print("{} arguments:".format(len(argv) - 1))
        i = 1
        while(i < len(argv)):
            print("{}: {}".format(i, argv[i]))
            i = i + 1


if (__name__ == "__main__"):
    print_args()
