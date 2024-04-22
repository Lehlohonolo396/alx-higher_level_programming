#!/usr/bin/python3

def add_integer(a, b=98):

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError
    return (int(a) + int(b))
