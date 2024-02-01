#!/usr/bin/python3

# print integer with .format and gestion of error case
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    return True
