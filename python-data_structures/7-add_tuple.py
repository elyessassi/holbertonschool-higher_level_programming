#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = 0
    a2 = 0
    b = 0
    b2 = 0
    if len(tuple_a) >= 1:
        a = tuple_a[0]
    if len(tuple_b) >= 1:
        b = tuple_b[0]
    if len(tuple_a) >= 2:
        a2 = tuple_a[1]
    if len(tuple_b) >= 2:
        b2 = tuple_b[1]
    tuple_c = (a + b, a2 + b2)
    return tuple_c
