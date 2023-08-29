#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    cnt = 0
    for y in range(x):
        try:
            print(f"{my_list[y]}", end="")
            cnt += 1
        except IndexError:
            break
    print()
    return cnt
