#!/usr/bin/python3

# returns a key with the biggest integer value
def best_score(a_dictionary):
    if (a_dictionary is not None):
        max_key = max(a_dictionary)
        return max_key
    else:
        return None
