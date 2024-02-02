#!/usr/bin/python3

# addition 2 tuples
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ""

# add (0, 0) for a tuple (usefull in case or a tuple has an index > 2)
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return new_tuple
