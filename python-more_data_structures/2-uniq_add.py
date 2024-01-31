#!/usr/bin/python3

# adds all unique integers in a list
def uniq_add(my_list=[]):
    unique_list = []
    result = 0

    for index in my_list:
        if index not in unique_list:
            unique_list.append(index)
            result += index

    return result
