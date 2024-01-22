#!/usr/bin/python3
# print numbers from 0 to 99

separator = ", "
for numbers in range(0, 100):
    if (numbers == 99):
        separator = "\n"
    print("{:02}".format(numbers), end=separator)
