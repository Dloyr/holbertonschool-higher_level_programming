#!/usr/bin/python3

# print alphabet in reverse, alternating lowercase and uppercase
for alphabet in reversed(range(97, 123)):
    if (alphabet % 2):
        print("{}".format(chr(alphabet).upper()), end="")
    else:
        print("{}".format(chr(alphabet).lower()), end="")
