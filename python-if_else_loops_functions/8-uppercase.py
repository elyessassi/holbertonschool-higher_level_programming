#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        print(chr(ord(str[i]) - 32), end="")
