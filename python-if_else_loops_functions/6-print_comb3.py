#!/usr/bin/python3
for i in range(0, 9):
    for i2 in range(i + 1, 10):
        if i == 8:
            print("{:d}{:d}".format(i, i2))
            break
        print("{:d}{:d}".format(i, i2), end=", ")
