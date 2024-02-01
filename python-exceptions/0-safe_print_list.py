#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
        print("")
    except TypeError:
        return (i + 1)
    except IndexError:
        print("")
        return (i)
    return (i + 1)
