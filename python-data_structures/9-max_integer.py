#!/usr/bin/python3

# find the biggest integer of a list
def max_integer(my_list=[]):
    my_list.sort()

    return my_list[-1]
