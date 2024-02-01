#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    mylist = []
    for i in range(list_length):
        try:
            mylist.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            mylist.append(0)
            print("wrong type")
            pass
        except ZeroDivisionError:
            mylist.append(0)
            print("division by 0")
            pass
        except IndexError:
            mylist.append(0)
            print("out of range")
    return mylist
