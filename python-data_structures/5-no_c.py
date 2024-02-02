#!/usr/bin/python3

# remove all characters "c" and "C" from a string
def no_c(my_string):
    new_string = ""

    for index in my_string:
        if (index != 'c' and index != 'C'):
            new_string += index

    return new_string
