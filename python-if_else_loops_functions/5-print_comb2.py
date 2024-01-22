#!/usr/bin/python3
# print numbers from 0 to 99

for numbers in range(0, 100):
    if (numbers < 99):
        print("{:02}".format(numbers), end=", ")
    else:
        print(numbers)
