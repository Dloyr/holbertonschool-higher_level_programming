#!/usr/bin/python3
if __name__ == "__main__":
    import sys

# print the number and the list of word in the input
argv = sys.argv[1:]
counter = 0

if (len(argv) > 1):
    print(f"{len(argv)} arguments:")
elif (len(argv) == 1):
    print(f"{len(argv)} argument:")
else:
    print(f"{len(argv)} arguments.")

for argc in argv:
    counter += 1
    print(f"{counter}: {argc}")
