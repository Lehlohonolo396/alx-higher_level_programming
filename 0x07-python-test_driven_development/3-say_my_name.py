#!/usr/bin/python3

def say_my_name(first_name, last_name=""):

    if not isinstance(first_name, str):
        raise TypeError
    if not isinstance(last_name, str):
        raise TypeError
    print("My name is {} {}".format(first_name, last_name))
