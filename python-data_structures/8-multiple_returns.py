#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None or sentence == "":
        tup = (0, None)
        return tup
    else:
        tup = (len(sentence), sentence[0])
        return tup
