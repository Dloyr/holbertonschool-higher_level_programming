#!/usr/bin/python3

# prints a dictionary by ordered keys
def print_sorted_dictionary(a_dictionary):
    sorted_dictionnary = sorted(a_dictionary)

    for index in sorted_dictionnary:
        print("{} : {}".format(index, a_dictionary[index]))
