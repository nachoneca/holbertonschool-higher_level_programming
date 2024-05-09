#!/usr/bin/python3

import sys
if __name__ == "__main__":
    numarg = len(sys.argv) - 1
    if numarg == 0:
        print("{} arguments.".format(numarg))
    elif numarg == 1:
        print("{} argument:\n{}: {}".format(numarg, numarg, sys.argv[1]))
    elif numarg > 1:
        print("{} arguments:\n".format(numarg))
        for i in range(1, numarg):
            print("{}: {}".format(i, sys.argv[i + 1]))



