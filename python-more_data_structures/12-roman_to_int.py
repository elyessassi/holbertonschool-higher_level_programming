#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False:
        return 0
    d = {"I": 1, "V": 5, 'X': 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    x = 0
    px = 0
    for i in roman_string:
        for key in d:
            if key == i:
                if d[key] > px:
                    x = x + d[key] - 2 * px
                    px = d[key]
                else:
                    x = x + d[key]
                    px = d[key]
                continue
    return x
