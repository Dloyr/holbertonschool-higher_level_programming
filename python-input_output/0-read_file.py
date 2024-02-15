#!/usr/bin/python3

"""read a file"""


def read_file(filename=""):
    """function for read a file"""
    with open(filename, "r") as file:
        print(file.readlines())
        file.close
