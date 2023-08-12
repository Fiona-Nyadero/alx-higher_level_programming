#!/usr/bin/python3
import sys

if __name__ == "__main__":
    res_add = 0

    for arg in sys.argv:
        if arg != sys.argv[0]:
            res_add += int(arg)
    print(res_add)
