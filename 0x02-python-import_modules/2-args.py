#!/usr/bin/python3
import sys

if __name__ == "__main__":
    av = sys.argv[1:]
    ac = len(av)

    if ac == 0:
        print("0 arguments.")
    elif ac == 1:
        print("1 argument:")
        print("1:", av[0])
    else:
        print(ac, "arguments:")
        for y, arg in enumerate(av, start=1):
            print(y, ":", arg)
