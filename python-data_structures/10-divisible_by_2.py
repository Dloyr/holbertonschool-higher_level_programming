#!/usr/bin/python3

# find all multiples of 2 in a list
def divisible_by_2(my_list=[]):
    multiple_2 = []

    for number in my_list:
        if (number % 2 == 0):
            multiple_2.append(True)
        else:
            multiple_2.append(False)

    return multiple_2
