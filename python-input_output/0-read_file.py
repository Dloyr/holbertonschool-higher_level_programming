#!/usr/bin/python3

"""read a file"""


def read_file(filename=""):
    with open(filename, "r") as file:
        print(file.readlines())
        file.close
