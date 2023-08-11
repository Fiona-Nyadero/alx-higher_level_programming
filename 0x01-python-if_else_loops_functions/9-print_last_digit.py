#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        l_dgt = number % 10
    else:
        l_dgt = number % -10
        l_dgt *= -1

    print("{:d}".format(l_dgt), end='')
    return (l_dgt)
