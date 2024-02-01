#!/usr/bin/python3

# divides 2 integers and prints the result with gestion of errors case
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        pass
    finally:
        if (result != 0):
            print("Inside result: {}".format(result))
            return result
        else:
            print("Inside result: None")
            return None
