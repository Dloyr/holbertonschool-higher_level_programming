#!/usr/bin/python3
# print the alphabet in lowercase execpt e and q

for letter in range(97, 123):
    if (letter == 101 or letter == 113):
        continue

    print(chr(letter), end="")
