#!/usr/bin/python3

# remove character in a string a the position n
def remove_char_at(str, n):

    character_remove = ""

    if (0 <= n < len(str)):
        character_remove = str[: n] + str[n + 1:]
        return character_remove
    else:
        return str
