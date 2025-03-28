#!/usr/bin/python3

"""
a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """ a function that divides all elements of a matrix """

    if (not isinstance(div, int) and not isinstance(div, float)):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    row_length = len(matrix[0])
    row_counter = 0  # starts from 0
    for i in matrix:
        new_matrix.append([])
        for j in i:
            if (not isinstance(j, int) and not isinstance(j, float)):
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            if (len(i) != row_length):
                raise TypeError("Each row of the matrix"
                                " must have the same size")
            new_matrix[row_counter].append(round(j / div, 2))
        row_counter = row_counter + 1
    return(new_matrix)


if (__name__ == "__main__"):
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
