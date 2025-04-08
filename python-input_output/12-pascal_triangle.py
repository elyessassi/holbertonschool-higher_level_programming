#!/usr/bin/python3
""" Function that prints pascal triangle"""


def pascal_triangle(n):
    """ The function """
    if (n <= 0):
        return ([])
    the_list = [[1]]
    if (n == 1):
        return(the_list)
    for i in range(1, n):
        new_list = []
        for j in range(len(the_list[len(the_list) - 1])):
            if (j == 0):
                new_list.append(the_list[len(the_list) - 1][0])
            if (j == len(the_list[len(the_list) - 1]) - 1):
                new_list.append(the_list[len(the_list) - 1][-1])
            else:
                new_list.append(the_list[len(the_list) - 1][j] +
                                the_list[len(the_list) - 1][j + 1])
        the_list.append(new_list)
    return(the_list)
