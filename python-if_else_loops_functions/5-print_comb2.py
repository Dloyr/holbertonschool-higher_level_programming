#!/usr/bin/python3
# print numbers from 0 to 99

for numbers in range(0, 100):
    if (numbers < 99):
        print(f"{numbers:02d}", end=", ")
    else:
        print(numbers)
