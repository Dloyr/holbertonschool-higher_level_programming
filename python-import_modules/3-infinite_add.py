#!/usr/bin/python3
if __name__ == "__main__":
    import sys
# sum of arguments

argv = sys.argv[1:]
sum = 0

if (len(argv) == 0):
    print("0")

for argc in argv:
    sum += int(argc)

print(sum)
