#!/usr/bin/python3

# Print the numbers from 1 to 100 and replace multiple of 3 for Fizz,
# 5 for buzz and multiple of both for FizzBuzz.

def fizzbuzz():
    for numbers in range(1, 101):
        if (numbers % 3 == 0 and numbers % 5 == 0):
            print("FizzBuzz", end=" ")
            continue
        elif (numbers % 3 == 0):
            print("Fizz", end=" ")
            continue
        elif (numbers % 5 == 0):
            print("Buzz", end=" ")
            continue

        print(numbers, end=" ")
