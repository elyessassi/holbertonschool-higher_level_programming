#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    temp = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > temp:
            temp = my_list[i]
    return temp
