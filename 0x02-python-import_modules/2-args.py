#!/usr/bin/python3
import sys

if __name__ == "__main__":
    av = sys.argv[1:]
    ac = len(av)

    if ac == 0:
        print("0 arguments.")
    elif ac == 1:
        print("1 argument:")
    else:
        print(ac, "arguments:")

    if ac >= 1:
        ac = 0
        for arg in sys.argv:
            if ac != 0:
                print("{}: {}".format(ac, arg))
            ac += 1
