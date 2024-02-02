#!/usr/bin/python3

# replace an element at a index in a copy of the list
def new_in_list(my_list, idx, element):
    copy_list = ""

    if (idx < 0 or idx >= len(my_list)):
        return my_list[:]
    else:
        copy_list = my_list[:]
        copy_list[idx] = element
        return copy_list
