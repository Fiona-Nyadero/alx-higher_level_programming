#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    for item in range(0, x):
        try:
            print("{:d}".format(my_list[item]), end="")
            cnt += 1
        except (ValueError, TypeError):
            pass
    print()
    return cnt
