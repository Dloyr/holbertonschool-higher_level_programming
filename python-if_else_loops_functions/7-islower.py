#!/usr/bin/python3
# return true if the alpahabet is in lowercase or false if is not

def islower(c):
    if (ord(c) >= 97 and ord(c) <= 122):
        return True
    else:
        return False
