#!/usr/bin/python3

# replaces all occurences of an element by another in a new list
# my_list is the list
# search is the element to replace
# replace is the new element
def search_replace(my_list, search, replace):
    new_list = my_list[:]

    for index in range(len(new_list)):
        if (new_list[index] == search):
            new_list[index] = replace

    return new_list
