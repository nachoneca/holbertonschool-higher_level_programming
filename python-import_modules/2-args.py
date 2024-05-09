#!/usr/bin/python3

import sys
if __name__ = "__main__":
    numarg = len(argv)
    if numarg == 0:
        print("{} arguments.".format(numarg))
    elif numarg == 1:
        print("{} argument:\n{}: {}".format(numarg, numarg, sys.argv[1:]))
    elif numarg > 1:
        print("{} arguments:\n")
        for i in range(numarg)
            print("{}: {}".format(i, sys.argv[i]))



