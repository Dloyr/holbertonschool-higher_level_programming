#!/usr/bin/python3

# prints all possible different combinations of two digits
separator = ", "
for digit_1 in range(0, 10):
    for digit_2 in range(digit_1 + 1, 10):
        if (digit_1 == 8 and digit_2 == 9):
            separator = "\n"

        print("{}{}".format(digit_1, digit_2), end=separator)
