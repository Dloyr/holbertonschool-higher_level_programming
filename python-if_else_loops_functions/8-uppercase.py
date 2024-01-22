#!/usr/bin/python3
# print a string in uppercase

def uppercase(str):
    upper_string = ""

    for letter in str:
        if (97 <= ord(letter) <= 122):
            upper_string += chr(ord(letter) - 32)
        else:
            upper_string += letter

    print("{:s}".format(upper_string))
