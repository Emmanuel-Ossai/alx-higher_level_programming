#!/usr/bin/python3
for x in range(1, 9):
    for y in range(x + 2, 11):
        print("{:d}{:d}".format(x, y), end=', ')
print("{:d}{:d}".format(x + 1, y))
