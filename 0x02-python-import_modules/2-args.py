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
        
    if y >=1:
        y = 0
        for arg in sys.argv:
            if y != 0:
                print("{}: {}".format(y, arg)
            y += 1

