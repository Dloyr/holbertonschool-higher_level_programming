#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
enddigit = abs(number) % 10

# print a different message if enddigit is > 5 , < 6 or == 0
if (number < 0):
    enddigit = -enddigit
if (enddigit > 5):
    print(f"Last digit of {number} is {enddigit} and is greater than 5")
elif (enddigit != 0):
    print(f"Last digit of {number} is {enddigit} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {enddigit} and is 0")
